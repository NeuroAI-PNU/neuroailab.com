import re,base64,os,sys
IC='/home/hyunsu/.claude/jobs/f9ccb483/tmp/iconcand/'; GA='/home/hyunsu/.claude/jobs/f9ccb483/tmp/ga/'
def body(name):
    s=open(IC+f'lucide_{name}.svg').read(); return re.search(r'>\s*(<(?:path|circle|rect|line)[\s\S]*?)</svg>',s).group(1)
def ic(name,x,y,size,color,sw=2):
    sc=size/24; return f'<g transform="translate({x-size/2:.1f},{y-size/2:.1f}) scale({sc:.3f})" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body(name)}</g>'
_c={}
def img(path,x,y,w,h):
    if path not in _c: _c[path]=base64.b64encode(open(path,'rb').read()).decode()
    return f'<image href="data:image/jpeg;base64,{_c[path]}" x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" preserveAspectRatio="xMidYMid meet"/>'
ORA,GRN,SKY,PUR,TEAL,INK='#F0A94A','#3FA36B','#5BD0F0','#7B3FA0','#2A9DBD','#222'
F='font-family="DejaVu Sans, Helvetica, Arial, Apple SD Gothic Neo, Malgun Gothic, Noto Sans KR, sans-serif"'
TXT={'en':dict(model='Computational model',data='Experimental &amp; clinical data',mol='Molecule',beh='Behavior',
    q1=('AI drug discovery','virtual screening · AI prediction · MD · kinase inhibitors',[[('f_drug_yoon.jpg','FAK activator discovery · Comput Biol Chem 2025')],[('f_drug1.jpg','KMU-11342 · kinase targets · Pharmaceuticals 2026')]]),
    q2=('Hippocampus × RL','successor / predecessor features · ACh-modulated exploration',[[('f_rl_ach.jpg','ACh gain × arm length · Cogn Neurodyn 2026')],[('f_rl_sensors24.jpg','T-maze task and cumulative reward · Sensors 2024')]]),
    q3=('Brain data &amp; neuropsychiatry','electrophysiology · MEA · scRNA-seq · in-silico epilepsy',[[('f_brain1.jpg','CASCADE: cross-platform MEA pipeline · Bioinformatics 2026')]]),
    q4=('AI clinical decision support','risk equations · clinical NLP · interpretable models',[[('f_clin1.jpg','SNOMED-CT mapping · MBEC 2026')],[('f_clin_sr.jpg','symbolic regression vs ML · Biomedicines 2026')]])),
  'ko':dict(model='계산 모델',data='실험 · 임상 데이터',mol='분자',beh='행동',
    q1=('AI 신약 개발','가상 스크리닝 · AI 예측 · 분자동역학 · 키나아제 억제제',[[('f_drug_yoon.jpg','FAK 활성화제 발굴 · Comput Biol Chem 2025')],[('f_drug1.jpg','KMU-11342 · 키나아제 표적 · Pharmaceuticals 2026')]]),
    q2=('해마 × 강화학습','successor / predecessor feature · 아세틸콜린 조절 탐색',[[('f_rl_ach.jpg','ACh 이득 × 팔 길이 · Cogn Neurodyn 2026')],[('f_rl_sensors24.jpg','T-미로 과제와 누적 보상 · Sensors 2024')]]),
    q3=('뇌 데이터 · 신경정신의학','전기생리 · MEA · scRNA-seq · in-silico 뇌전증',[[('f_brain1.jpg','CASCADE: 다제조사 MEA 파이프라인 · Bioinformatics 2026')]]),
    q4=('AI 임상 의사결정 지원','위험 방정식 · 임상 자연어처리 · 해석 가능한 모델',[[('f_clin1.jpg','SNOMED-CT 매핑 · MBEC 2026')],[('f_clin_sr.jpg','symbolic regression vs ML · Biomedicines 2026')]]))}
ICONS={'q1':lambda x,y,s: ic('hexagon',x,y,s,PUR,2)+f'<circle cx="{x}" cy="{y}" r="{s/11:.0f}" fill="{PUR}"/>','q2':lambda x,y,s: ic('brain',x,y,s,GRN,2),'q3':lambda x,y,s: ic('activity',x,y,s,ORA,2),'q4':lambda x,y,s: ic('stethoscope',x,y,s,TEAL,2)}
COL={'q1':(PUR,'#F8EEFB'),'q2':(GRN,'#F2FAF5'),'q3':(ORA,'#FFF6E9'),'q4':(TEAL,'#EAF7FB')}
def panel(color,x,y,w,h,path,cap,fs):
    return f'''
  <rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="12" fill="#fff" stroke="{color}" stroke-width="1.5"/>
  {img(GA+path,x+6,y+6,w-12,h-(fs+22))}
  <text x="{x+w/2:.0f}" y="{y+h-11:.0f}" text-anchor="middle" font-size="{fs}" fill="#666">{cap}</text>'''
def quad(key,T,x,y,W,H,ft,fsub,fcap,axis=None):
    color,fill=COL[key]; title,sub,cols=T[key]; r=ft*1.3
    out=f'''<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="24" fill="{fill}" stroke="{color}" stroke-width="4"/>
  <circle cx="{x+r+16}" cy="{y+r+14}" r="{r:.0f}" fill="#fff" stroke="{color}" stroke-width="2.5"/>{ICONS[key](x+r+16,y+r+14,r*1.15)}
  <text x="{x+2*r+34}" y="{y+r+8}" font-size="{ft}" font-weight="bold" fill="{INK}">{title}</text>
  <text x="{x+2*r+34}" y="{y+r+8+fsub+8}" font-size="{fsub}" fill="#555">{sub}</text>'''
    top=y+2*r+40
    if axis:
        out+=f'<text x="{x+2*r+34}" y="{y+r+8+2*(fsub+8)}" font-size="{fsub-1}" font-weight="bold" fill="{color}">{axis}</text>'; top+=fsub+10
    ax,ay,aw,ah=x+18,top,W-36,H-(top-y)-18; gap=12; n=len(cols); cw=(aw-gap*(n-1))/n
    for i,col in enumerate(cols):
        fx=ax+i*(cw+gap); m=len(col); rh=(ah-gap*(m-1))/m
        for j,(p,c) in enumerate(col): out+=panel(color,fx,ay+j*(rh+gap),cw,rh,p,c,fcap)
    return out
def wide(lang,tag):
    T=TXT[lang]; cx,cy=800,590; W,H=640,450; g=60; x1,x2=cx-g-W,cx+g; y1,y2=cy-g-H,cy+g
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1180" viewBox="0 0 1600 1180" {F}>
  <rect width="1600" height="1180" fill="#fff"/>
  {quad('q1',T,x1,y1,W,H,28,17,12.5)}{quad('q2',T,x2,y1,W,H,28,17,12.5)}{quad('q3',T,x1,y2,W,H,28,17,12.5)}{quad('q4',T,x2,y2,W,H,28,17,12.5)}
  <g fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
    <line x1="150" y1="{cy}" x2="1450" y2="{cy}"/><path d="M 1425 {cy-16} L 1450 {cy} L 1425 {cy+16}"/><path d="M 175 {cy-16} L 150 {cy} L 175 {cy+16}"/>
    <line x1="{cx}" y1="62" x2="{cx}" y2="1118"/><path d="M {cx-16} 87 L {cx} 62 L {cx+16} 87"/><path d="M {cx-16} 1093 L {cx} 1118 L {cx+16} 1093"/>
  </g>
  <g font-size="26" font-weight="bold" fill="{INK}">
    <text x="78" y="{cy+9}" text-anchor="middle">{T['mol']}</text><text x="1522" y="{cy+9}" text-anchor="middle">{T['beh']}</text>
    <text x="{cx}" y="42" text-anchor="middle">{T['model']}</text><text x="{cx}" y="1160" text-anchor="middle">{T['data']}</text></g>
</svg>'''
    open(f'research-map-{tag}-{lang}.svg','w').write(s)
def mobile(lang,tag):
    T=TXT[lang]; W=780; H=590; gap=28; x=20
    ax={'q1':f"{T['mol']} × {T['model']}",'q2':f"{T['beh']} × {T['model']}",'q3':f"{T['mol']} × {T['data']}",'q4':f"{T['beh']} × {T['data']}"}
    total=20+4*(H+gap)-gap+20
    body_=''.join(quad(k,T,x,20+i*(H+gap),W,H,30,19,13,axis=ax[k]) for i,k in enumerate(('q1','q2','q3','q4')))
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W+40}" height="{total}" viewBox="0 0 {W+40} {total}" {F}>
  <rect width="{W+40}" height="{total}" fill="#fff"/>{body_}
</svg>'''
    open(f'research-map-{tag}-mobile-{lang}.svg','w').write(s)
tag=sys.argv[1] if len(sys.argv)>1 else 'v7'
for l in ('en','ko'): wide(l,tag); mobile(l,tag)
print('generated',tag)
