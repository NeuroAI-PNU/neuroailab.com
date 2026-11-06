#!/usr/bin/env python3
"""content/ 안의 사진을 웹에서 보이는 JPEG/PNG로 고친다.

    python3 tools/fix-images.py          # 고치기
    python3 tools/fix-images.py --check  # 고칠 게 있으면 목록만 찍고 종료코드 1

- iPhone HEIC/HEIF·AVIF·WebP 등 브라우저가 못 띄우거나 확장자와 실제 형식이 다른 파일 → 진짜 JPEG로 변환
- 휴대폰 방향(EXIF Orientation)을 픽셀에 반영 (Hugo는 EXIF 회전을 무시함)
- 긴 변 2000px 넘거나 1.5MB 넘으면 줄임
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


def exif_orientation(p: pathlib.Path) -> int:
    """JPEG EXIF Orientation 태그(1=정상). 표준 라이브러리만으로 읽는다."""
    b = p.read_bytes()[:65536]
    i = b.find(b"Exif\x00\x00")
    if i < 0:
        return 1
    t = i + 6
    le = b[t:t + 2] == b"II"
    u16 = lambda o: int.from_bytes(b[o:o + 2], "little" if le else "big")
    u32 = lambda o: int.from_bytes(b[o:o + 4], "little" if le else "big")
    ifd = t + u32(t + 4)
    for k in range(u16(ifd)):
        e = ifd + 2 + 12 * k
        if u16(e) == 0x0112:
            return u16(e + 8)
    return 1


def too_big(p: pathlib.Path) -> bool:
    return p.stat().st_size > 1_500_000


def problems():
    for p in sorted(ROOT.rglob("*")):
        if p.suffix.lower() not in EXT or not p.is_file():
            continue
        kind = sniff(p)
        want = "png" if p.suffix.lower() == ".png" else "jpeg"
        if p.suffix.lower() in (".heic", ".heif") or kind != want:
            yield p, kind
        elif kind == "jpeg" and exif_orientation(p) != 1:
            # Hugo가 줄일 때 EXIF 회전을 무시해서 사이트에서 옆으로 누운다
            yield p, "jpeg(EXIF 회전)"
        elif too_big(p):
            yield p, f"{kind}(큰 파일)"


def main():
    found = list(problems())
    if "--check" in sys.argv:
        for p, kind in found:
            print(f"{p.relative_to(ROOT.parent)}: {kind} — 사이트에서 안 보이거나 돌아가 보일 수 있음. tools/fix-images.py 로 변환")
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
