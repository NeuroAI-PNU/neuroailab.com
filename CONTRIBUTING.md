# 홈페이지 수정 방법

모든 수정은 브랜치 + Pull Request로 합니다. `main`에 머지되면 1~2분 안에 사이트에 반영됩니다.

## 공통 절차

```bash
git clone git@github.com:NeuroAI-PNU/neuroailab.com.git
cd neuroailab.com
git switch -c update-profile-<이름>
# 파일 수정
git add -A && git commit -m "people: <이름> 프로필 추가"
git push -u origin HEAD
```

GitHub에서 PR을 열면 됩니다. 로컬에 Hugo가 없어도 됩니다. PR의 Actions 빌드가 통과하면 지도교수가 확인 후 머지합니다.

## 내 프로필 추가·수정

한 사람당 두 파일입니다. 기존 파일을 복사해서 고치세요.

- `content/ko/authors/<이름-slug>/_index.md` (한국어)
- `content/en/authors/<이름-slug>/_index.md` (영어)

`user_groups`는 두 언어의 `people/index.md`에 있는 그룹 이름과 정확히 같아야 표시됩니다.
`weight`는 그룹 안 정렬 순서입니다(작을수록 위).

사진은 같은 폴더에 `avatar.jpg`(정방형, 400×400 정도)로 넣으면 자동으로 표시됩니다. 두 언어 폴더에 각각 넣어야 합니다.

## 소식(News) 글 쓰기

`content/ko/post/<YYYY-MM-DD-slug>/index.md`를 만들고, 영어판이 있으면 `content/en/post/` 에 같은 폴더명으로 만듭니다.

```markdown
---
title: 글 제목
date: 2026-09-13
authors:
  - Hyunsu Lee
summary: 한 줄 요약
---

본문
```

이미지는 글 폴더 안에 두고 `![설명](image.jpg)`로 넣습니다.

## 논문 추가

1. `publications.bib`에 BibTeX 항목을 추가합니다.
2. `content/ko/publication/<slug>/index.md`와 `content/en/...`을 기존 항목을 복사해 만듭니다. `authors`의 이름이 프로필 `title`과 같으면 자동으로 링크됩니다.

## 적지 말아야 할 것

- 학생 개인 연락처, 학번, 내부 서버 주소·포트, 비밀번호.
- 다른 사람 사진은 본인 동의 후에만.
