# neuroailab.com

부산대학교 의과대학 생리학교실 **신경인공지능 연구실(NeuroAI Lab)** 홈페이지 소스입니다.
[Hugo Blox](https://hugoblox.com) research-group 템플릿 기반의 정적 사이트로, `main`에 머지되면 GitHub Actions가 GitHub Pages에 자동 배포합니다.

- 사이트: https://neuroailab.com (도메인 연결 전에는 https://neuroai-pnu.github.io/neuroailab.com/)
- 언어: 한국어 `content/ko/` (기본), 영어 `content/en/`
- 수정 방법: [CONTRIBUTING.md](CONTRIBUTING.md)

## 구조

| 경로 | 내용 |
|---|---|
| `content/{ko,en}/_index.md` | 첫 화면 |
| `content/{ko,en}/research/` | 연구 소개 |
| `content/{ko,en}/people/` | 구성원 페이지 (그룹 목록) |
| `content/{ko,en}/authors/<slug>/` | 개인 프로필 (한 사람 = 두 언어 폴더) |
| `content/{ko,en}/publication/<slug>/` | 논문 |
| `content/{ko,en}/post/` | 소식 |
| `content/{ko,en}/join/`, `contact/` | 모집, 연락 |
| `publications.bib` | 논문 BibTeX 원본 |
| `config/_default/` | 사이트 설정 (`languages.yaml`에 언어별 메뉴) |

## 로컬 빌드

Hugo extended 0.166 이상과 Go가 필요합니다.

```bash
hugo server            # http://localhost:1313/ko/
hugo --minify          # public/ 생성
```
