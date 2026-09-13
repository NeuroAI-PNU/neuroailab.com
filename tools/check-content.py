#!/usr/bin/env python3
"""소식(post) 글의 front matter 검사.

- authors 가 비어 있으면 실패
- authors 의 각 이름이 같은 언어의 프로필(content/<lang>/authors/*/_index.md 의 title)과 일치해야 함
GitHub Actions 의 build 단계에서 hugo 빌드 전에 실행된다.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1] / "content"
errors = []

def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""

def authors_of(fm):
    m = re.search(r"^authors:\s*\n((?:[ \t]+-[^\n]*\n?)+)", fm, re.M)
    if m:
        return [re.sub(r"^\s*-\s*", "", l).strip().strip("'\"") for l in m.group(1).splitlines() if l.strip()]
    m = re.search(r"^authors:\s*\[(.*?)\]", fm, re.M)
    if m:
        return [a.strip().strip("'\"") for a in m.group(1).split(",") if a.strip()]
    return []

for lang_dir in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    profiles = {}
    for f in (lang_dir / "authors").glob("*/_index.md"):
        m = re.search(r"^title:\s*(.+)$", front_matter(f), re.M)
        if m:
            profiles[m.group(1).strip().strip("'\"")] = f.parent.name
    for f in sorted((lang_dir / "post").glob("*/index.md")):
        rel = f.relative_to(ROOT.parent)
        names = authors_of(front_matter(f))
        if not names:
            errors.append(f"{rel}: authors 가 비어 있습니다. 프로필 이름을 적어 주세요 (예: authors: [Hyunsu Lee])")
            continue
        for n in names:
            if n not in profiles:
                close = [p for p in profiles if p.split()[-1] == n.split()[-1]] if n.split() else []
                hint = f" (비슷한 프로필: {', '.join(close)})" if close else ""
                errors.append(f"{rel}: authors '{n}' 에 해당하는 프로필이 {lang_dir.name}/authors 에 없습니다{hint}")

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)}개 문제. 프로필 이름은 content/<lang>/authors/<slug>/_index.md 의 title 과 같아야 합니다.")
    sys.exit(1)
print("check-content: OK")
