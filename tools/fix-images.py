#!/usr/bin/env python3
"""content/ 안의 사진을 웹에서 보이는 JPEG/PNG로 고친다.

    python3 tools/fix-images.py          # 고치기
    python3 tools/fix-images.py --check  # 고칠 게 있으면 목록만 찍고 종료코드 1

- iPhone HEIC/HEIF·AVIF·WebP 등 브라우저가 못 띄우거나 확장자와 실제 형식이 다른 파일 → 진짜 JPEG로 변환
- 긴 변 2000px 넘으면 줄이고, 휴대폰 방향(EXIF) 반영
- 확장자는 그대로 둔다(index.md 의 그림 이름이 바뀌지 않게). .heic 파일은 .jpg 로 바꾸고 index.md 참조도 고친다.
필요: pip install pillow pillow-heif
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1] / "content"
EXT = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".webp", ".avif"}
MAX = 2000


def sniff(p: pathlib.Path) -> str:
    h = p.read_bytes()[:16]
    if h[:3] == b"\xff\xd8\xff":
        return "jpeg"
    if h[:8] == b"\x89PNG\r\n\x1a\n":
        return "png"
    if h[4:8] == b"ftyp":
        return h[8:12].decode("ascii", "replace")  # heic, mif1, avif …
    if h[:4] == b"RIFF" and h[8:12] == b"WEBP":
        return "webp"
    return "unknown"


def problems():
    for p in sorted(ROOT.rglob("*")):
        if p.suffix.lower() not in EXT or not p.is_file():
            continue
        kind = sniff(p)
        want = "png" if p.suffix.lower() == ".png" else "jpeg"
        if p.suffix.lower() in (".heic", ".heif") or kind != want:
            yield p, kind


def main():
    found = list(problems())
    if "--check" in sys.argv:
        for p, kind in found:
            print(f"{p.relative_to(ROOT.parent)}: 실제 형식 {kind} — 웹에서 안 보일 수 있음. tools/fix-images.py 로 변환")
        sys.exit(1 if found else 0)
    from PIL import Image, ImageOps
    import pillow_heif
    pillow_heif.register_heif_opener()
    for p, kind in found:
        im = ImageOps.exif_transpose(Image.open(p))
        if max(im.size) > MAX:
            im.thumbnail((MAX, MAX))
        dst = p.with_suffix(".jpg") if p.suffix.lower() in (".heic", ".heif", ".webp", ".avif") else p
        if dst.suffix.lower() == ".png":
            im.save(dst, optimize=True)
        else:
            im.convert("RGB").save(dst, "JPEG", quality=85, optimize=True)
        if dst != p:
            p.unlink()
            idx = p.parent / "index.md"
            if idx.exists():
                idx.write_text(idx.read_text(encoding="utf-8").replace(p.name, dst.name), encoding="utf-8")
        print(f"converted {p.relative_to(ROOT.parent)} ({kind}) -> {dst.name}")


if __name__ == "__main__":
    main()
