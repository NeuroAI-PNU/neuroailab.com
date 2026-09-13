---
title: 연구
date: 2026-09-13
type: landing

sections:
  - block: markdown
    content:
      title: 연구
      text: |
        <img class="research-map-wide" src="research-map.svg" alt="연구 지도: 분자→행동 × 계산 모델→임상 데이터" data-zoomable>
        <img class="research-map-mobile" src="research-map-mobile.svg" alt="연구 지도: 분자→행동 × 계산 모델→임상 데이터" data-zoomable>
        <p style="text-align:center;font-size:0.85em;color:#666">그림 출처: FAK 활성화제 그래픽 초록 ([Comput Biol Chem 2025](../publication/yoon-2025/), © Elsevier), KMU-11342 ([Pharmaceuticals 2026](../publication/jeon-2026/), CC BY 4.0), ACh 이득 지형도, 보충 그림 S1 ([Cognitive Neurodynamics 2026](../publication/seo-2026/), open access), T-미로 과제와 누적 보상 ([Sensors 2024](../publication/seo-2024/), CC BY 4.0), CASCADE ([Bioinformatics 2026](../publication/avila-2026/), CC BY 4.0), SNOMED-CT 매핑 ([Med Biol Eng Comput 2026](../publication/oh-2026/), open access), symbolic regression vs 기계학습 분류기 ROC ([Biomedicines 2026](../publication/oh-2026-2/), CC BY 4.0).</p>

        ## 1. AI 기반 신약 개발

        가상 스크리닝, AI 물성 예측, 물리 기반 시뮬레이션을 결합해 새로운 치료 후보물질을 찾고 그 작용을 설명한 뒤, 실험 협력 연구실과 함께 검증합니다. FAK 활성화제 연구에서는 유사성 기반 스크리닝, 도킹, 딥러닝 예측 모델과 분자동역학을 이어 붙여 기준 화합물보다 결합 특성이 나은 후보를 골라냈습니다([Comput Biol Chem 2025](../publication/yoon-2025/)). 계명대학교와의 공동 연구로 인돌린-2-온 계열 키나아제 억제제 두 종을 규명했습니다. KMU-11342는 2D·3D 스페로이드·환자 유래 오가노이드 모델에서 대장암 세포의 증식·이동·줄기세포성을 억제하며, 키나아제 프로파일링과 도킹 분석은 p53/NF-κB 및 FoxO1 경로를 통한 GSK3β/CDK1 조절을 가리켰습니다([Pharmaceuticals 2026](../publication/jeon-2026/)). KMU-11361은 TAK1–NF-κB–NLRP3 축을 억제해 류마티스 관절염을 완화합니다([Inflammation Research 2026](../publication/baek-2026/)). 진행 중인 연구는 신경계 질환을 향합니다. 리소좀 이온채널 TMEM175의 선택적 조절제 발굴과 렘수면행동장애 신약 개발이 그 예입니다.

        ## 2. 뇌 데이터와 신경정신의학

        단일 세포 전기생리부터 집단 기록까지, 해석 가능한 분석 파이프라인을 여러 스케일에 걸쳐 만듭니다. 전기생리 특성만으로 신경세포의 유전자 마커를 예측할 수 있음을 보였고([Brain Res Bull 2019](../publication/seo-2019/)), 사람 대뇌피질 기록에서 FCD I형 뇌전증의 fast-spiking 억제성 신경세포로 들어오는 순 시냅스 입력이 억제 쪽으로 반전되어 있음을 밝혔습니다([Nature Communications 2024](../publication/cho-2024/)). 다전극 어레이(MEA) 제조사마다 폐쇄형 소프트웨어를 쓰는 문제를 풀기 위해, 다섯 제조사의 기록을 한 파이프라인에서 읽어 표준 네트워크 지표와 함께 임계성(criticality)·눈사태(avalanche) 통계를 계산하는 오픈소스 파이썬 도구 CASCADE를 공개했습니다([Bioinformatics 2026](../publication/avila-2026/)). 면역세포 농축 단일세포 RNA-seq로 알츠하이머병의 면역–신경 상호작용을 분석하고([J Neuroimmunol 2025](../publication/kang-2025/)), 뇌파 기반 스트레스 검출의 종단간 벤치마크를 제시했습니다([IEEE Access 2026](../publication/kim-2026/)). NEURON과 NetPyNE로 in-silico 뇌전증 모델을 구축하고 있으며, 발달성 뇌전증성 뇌병증과 관련된 Nav1.2 변이의 기전 분석도 그 일부입니다. 신경생성에 기반한 패턴 분리와 기분장애를 연결한 초기 연구도 있습니다([J Korean Soc Biol Ther Psychiatry 2020](../publication/lee-2020/)).

        ## 3. AI 임상 의사결정 지원

        임상 연구에서는 의료진이 읽을 수 있는 모델을 우선합니다. 전자의무기록의 자유 서술 진단명을 ClinicalBERT 미세조정으로 SNOMED-CT 개념에 매핑하고, 잠재 공간이 모호한 진단과 뚜렷이 다른 진단을 어떻게 구분하는지 분석했습니다([Med Biol Eng Comput 2026](../publication/oh-2026/)). 간이식 환자에서는 symbolic regression으로 이식 후 균혈증의 직관적인 위험 방정식을 도출했고, SHAP 분석에서 EBV/HBV 혈청 지표가 통상 검사값 외의 위험 인자 후보로 드러났습니다([Biomedicines 2026](../publication/oh-2026-2/)). 앞선 연구에서는 내시경 영상으로 거대세포바이러스 식도염과 단순헤르페스 식도염을 기계학습으로 구분하고([Scientific Reports 2021](../publication/lee-2021/)), 내시경 전문의가 GAN 생성 위내시경 영상을 실제와 구별할 수 있는지 시험했으며([J Digit Imaging 2023](../publication/shin-2023/)), TCGA 코호트로 대장암의 비만 역설을 살폈습니다([J Cancer 2023](../publication/lim-2023-2/)). 의학교육에서 ChatGPT의 가능성을 다룬 초기 논문은 이 주제에서 가장 많이 인용되는 논문 중 하나입니다([Anat Sci Educ 2024](../publication/lee-2024/)).

        ## 4. 해마 × 강화학습

        해마가 successor representation을 구현한다는 가설을 검증하고, 신경조절물질이 그 학습 규칙을 어떻게 바꾸는지 묻습니다([Biosystems 2022](../publication/lee-2022/); [Front Comput Neurosci 2025](../publication/lee-daou-2025/)). 시뮬레이션 연구로 가중치 초기화가 successor feature 학습에 미치는 영향([Electronics 2023](../publication/lee-2023/)), 잡음이 있는 T-미로 과제에서 predecessor/successor feature의 전이([Sensors 2024](../publication/seo-2024/)), 1차원·2차원 환경에서 두 알고리즘의 잡음 내성([Sensors 2025](../publication/lee-2025/))을 보였습니다. 가장 최근에는 아세틸콜린 조절을 반영한 predecessor feature 모델을 제안했습니다. 적격성 흔적(eligibility trace)으로 게이트되는 억압이 보상 이후에도 에이전트가 탐색을 이어가게 하며, n-arm 방사형 미로 시뮬레이션에서 기존 모델을 능가했고, 환경이 복잡해질수록 효과적인 조절 범위는 좁아졌습니다([Cognitive Neurodynamics 2026](../publication/seo-2026/)).

        > "From synapse to silicon, insight travels — and patient care transforms."

        {{% cta cta_link="../publication/" cta_text="전체 논문 목록 →" %}}
    design:
      columns: '1'
---
