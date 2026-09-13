---
title:
date: 2026-09-13
type: landing

sections:
  - block: hero
    content:
      title: |
        신경인공지능 연구실
      image:
        filename: welcome.jpg
      text: |
        <br>

        부산대학교 의과대학 생리학교실 **신경인공지능 연구실(NeuroAI Lab)**에 오신 것을 환영합니다.
        신경과학과 인공지능의 교차점에서 생물학적 기반의 강화학습, 뇌와 신경질환의 계산 모델, AI 신약 개발, 임상 의사결정 지원을 연구합니다.

        학부 인턴과 대학원생을 모집 중입니다. [모집 안내](join/)를 확인하세요.
      cta:
        label: 연구 소개
        url: research/
      cta_alt:
        label: 구성원
        url: people/

  - block: markdown
    content:
      title: 연구 주제
      text: |
        1. **AI 기반 신약 개발** — 생성 모델, 가상 스크리닝, 물리 기반 시뮬레이션으로 새로운 치료 후보물질을 찾습니다.
        2. **뇌 데이터와 신경정신의학** — 전기생리 데이터의 해석 가능한 기계학습, in-silico 뇌전증 모델, 면역–신경 상호작용.
        3. **AI 임상 의사결정 지원** — 이상반응 예측, 시술 최적화, 대형언어모델을 이용한 임상 언어 지능.
        4. **해마 × 강화학습** — 해마를 Successor Representation 에이전트로 보는 가설을 검증합니다.

        {{% cta cta_link="research/" cta_text="자세히 보기 →" %}}
    design:
      columns: '1'

  - block: collection
    content:
      title: 최근 소식
      count: 5
      filters:
        folders:
          - post
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'

  - block: collection
    content:
      title: 최근 논문
      count: 5
      filters:
        folders:
          - publication
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      text: |
        {{% cta cta_link="people/" cta_text="구성원 보기 →" %}}
    design:
      columns: '1'
---
