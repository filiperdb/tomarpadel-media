import random
R='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/kit/project/'
RED='#b8141f'; DRED='#7d0b13'; GREEN='#0e3b2c'; GOLD='#e9c46a'; WHITE='#ffffff'
LOGO='/_blob/0754512c9d115284b57fd1a8d5f1c5d8'; PL='/_blob/a1afe2902f9264b89ba005151baff896'; PS='/_blob/d6b9c2783a1af5a690f020bde7b45bbe'
PW,PH=1122,1402

def snow(w,h,n,seed):
    r=random.Random(seed); c=[]
    for _ in range(n):
        x=r.uniform(0,w); y=r.uniform(0,h); rad=r.choice([1.5,2,2.5,3,4,5]); op=r.uniform(0.25,0.8)
        c.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rad}" fill="#ffffff" fill-opacity="{op:.2f}"></circle>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true" style="position:absolute;left:0;top:0">{"".join(c)}</svg>'

def star(x,y,s,col=GOLD):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" aria-hidden="true" style="position:absolute;left:{x}px;top:{y}px"><path d="M12 0 L14.2 9.8 L24 12 L14.2 14.2 L12 24 L9.8 14.2 L0 12 L9.8 9.8 Z" fill="{col}"></path></svg>'

def lab(t,fs): return f'<div style="font-style:italic;font-weight:700;font-size:{fs}px;letter-spacing:0.14em;color:{GOLD}">{t}</div>'

def sponsors(top,h,w,pad,n,lbl=True,vertical=True):
    cells=f'<div style="display:flex;align-items:center;justify-content:center"><img src="{PS}" alt="P&amp;S Auto Color Expert" style="max-width:100%;max-height:{h-50}px;object-fit:contain"></div>'
    cells+=''.join(f'<div style="border:2px dashed #b9a7a7;border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;color:#7a6262">LOGO</div>' for _ in range(n-1))
    lb=(f'<div style="font-weight:800;font-size:16px;letter-spacing:0.14em;color:{DRED};writing-mode:vertical-rl;transform:rotate(180deg)">PATROCÍNIOS</div>' if vertical else f'<div style="font-weight:800;font-size:18px;letter-spacing:0.14em;color:{DRED}">PATROCÍNIOS</div>') if lbl else ''
    return f'''  <div style="position:absolute;left:0;right:0;top:{top}px;height:{h}px;box-sizing:border-box;background:#ffffff;padding:18px {pad}px;display:flex;align-items:center;gap:24px">
    {lb}
    <div style="display:grid;grid-template-columns:repeat({n},minmax(0,1fr));gap:16px;flex:1;height:{h-40}px">{cells}</div>
  </div>'''

def phases(top,left,right,fs1,fs2,line='rgba(255,255,255,0.3)'):
    items=[('01 a 14 Nov','Inscrições'),('15 a 22 Nov','Pagamentos'),('25 Nov','Grupo de WhatsApp'),('30 Nov','Divulgação do calendário')]
    cells=''.join(f'<div><div style="font-weight:800;font-size:{fs1}px">{a}</div><div style="font-size:{fs2}px;color:#f3d6d6">{b}</div></div>' for a,b in items)
    return f'  <div style="position:absolute;left:{left}px;right:{right}px;top:{top}px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;border-top:2px solid {line};padding-top:12px">{cells}</div>'

def infocol(left,top,width,fl,fv,big,gap):
    return f'''  <div style="position:absolute;left:{left}px;top:{top}px;width:{width}px;display:flex;flex-direction:column;gap:{gap}px">
    <div>{lab('CATEGORIAS',fl)}<div style="font-weight:800;font-size:{fv}px;line-height:1.3;margin-top:6px">Mistos Iniciante<br>Mistos Avançado<br>Masculinos Iniciante<br>Masculinos Avançado</div></div>
    <div>{lab('INSCRIÇÃO',fl)}<div style="display:flex;align-items:baseline;gap:12px;margin-top:4px"><div style="font-weight:900;font-stretch:62%;font-size:{big}px;line-height:0.9">25€</div><div style="font-weight:700;font-size:{fv-2}px">2ª categoria +10€</div></div></div>
    <div>{lab('WELCOME PACK',fl)}<div style="font-weight:800;font-size:{fv}px;line-height:1.3;margin-top:6px">T-shirt · Água · Voucher 1h30</div></div>
    <div>{lab('PRÉMIOS',fl)}<div style="font-weight:800;font-size:{fv}px;line-height:1.3;margin-top:6px">8 troféus<br>Prize money para 1º e 2º lugar</div></div>
  </div>'''

def chip(left,top,fs,align='flex-start'):
    return f'''  <div style="position:absolute;left:{left}px;top:{top}px;display:flex;flex-direction:column;align-items:{align};gap:8px">
    <div style="background:{GREEN};border:2px solid {GOLD};color:#ffffff;border-radius:999px;padding:10px 24px;font-weight:900;font-size:{fs}px;letter-spacing:0.06em">ESPECIAL EQUIPAS</div>
    <div style="font-weight:700;font-size:{fs-6}px">Equipas de 4 elementos</div>
  </div>'''

def portrait(W,H,T,title_top,natal_fs,pl_h,pl_bottom,info_top,ph_top,sp_top,sp_h,story=False):
    sc=pl_h/PH; pw=PW*sc
    body=f'''<div class="ar" style="position:relative;width:{W}px;height:{H}px;overflow:hidden;background:radial-gradient(ellipse 80% 60% at 60% 42%,#d42a33 0%,{RED} 45%,{DRED} 100%);color:#ffffff">
  {snow(W,H,120,H)}
  <!-- Topo -->
  <div style="position:absolute;left:56px;right:56px;top:{T}px;display:flex;align-items:center;justify-content:space-between">
    <img src="{LOGO}" alt="TomarPadel 2.0" style="width:270px;height:auto">
    <div style="border:2px solid #ffffff;border-radius:999px;padding:9px 20px;font-weight:800;font-size:20px;letter-spacing:0.14em">TORNEIO OFICIAL</div>
  </div>
  <!-- Linha de informação -->
  <div style="position:absolute;left:56px;right:56px;top:{T+92}px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;font-weight:800;font-size:22px;line-height:1.25">
    <div>{lab('DATA',16)}4 · 5 · 6 DEZEMBRO 2026</div>
    <div style="text-align:center">{lab('LOCAL',16)}TOMARPADEL 2.0 · TOMAR</div>
    <div style="text-align:right">{lab('INSCRIÇÕES',16)}01 A 14 NOVEMBRO</div>
  </div>
  <!-- Título -->
  <div style="position:absolute;left:0;right:0;top:{title_top}px;text-align:center;font-weight:900;font-stretch:62%;font-size:60px;line-height:1;letter-spacing:0.18em;color:{GOLD}">TORNEIO DE</div>
  {star(W//2-250,title_top+14,30)}{star(W//2+220,title_top+14,30)}{star(W-110,title_top+330,22)}{star(70,title_top+300,18)}{star(W-200,T+180,16)}
  <div style="position:absolute;left:0;right:0;top:{title_top+60}px;text-align:center;font-weight:900;font-stretch:62%;font-size:{natal_fs}px;line-height:0.8;letter-spacing:-0.01em;color:#ffffff;text-shadow:0 10px 40px rgba(60,0,0,0.35)">NATAL</div>
  <!-- Jogadores -->
  <img src="{PL}" alt="Dupla mista de padel em jogo" style="position:absolute;left:{W-pw:.0f}px;top:{pl_bottom-pl_h}px;width:{pw:.0f}px;height:{pl_h}px;filter:drop-shadow(0 18px 24px rgba(60,0,0,0.45))">
{infocol(56,info_top,330 if not story else 380,15 if not story else 17,21 if not story else 24,60 if not story else 70,20 if not story else 26)}
{chip(56,info_top-110 if not story else info_top-120,26 if not story else 28)}
{phases(ph_top,56,56,19 if not story else 21,15 if not story else 17)}
{sponsors(sp_top,sp_h,W,56,5)}
</div>'''
    return body

def landscape():
    W,H=1920,1080; pl_h=860; sc=pl_h/PH; pw=PW*sc
    return f'''<div class="ar" style="position:relative;width:3840px;height:2160px;overflow:hidden;background:{DRED};color:#ffffff">
<div style="position:absolute;left:0;top:0;width:1920px;height:1080px;transform:scale(2);transform-origin:0 0;background:radial-gradient(ellipse 70% 70% at 55% 45%,#d42a33 0%,{RED} 45%,{DRED} 100%)">
  {snow(W,H,180,7)}
  <div style="position:absolute;left:72px;right:72px;top:52px;display:flex;align-items:center;justify-content:space-between">
    <img src="{LOGO}" alt="TomarPadel 2.0" style="width:300px;height:auto">
    <div style="display:flex;gap:56px;font-weight:800;font-size:22px;line-height:1.25">
      <div>{lab('DATA',15)}4 · 5 · 6 DEZEMBRO 2026</div>
      <div>{lab('LOCAL',15)}TOMARPADEL 2.0 · TOMAR</div>
      <div>{lab('INSCRIÇÕES',15)}01 A 14 NOVEMBRO</div>
    </div>
  </div>
  <div style="position:absolute;left:0;width:1200px;top:150px;text-align:center;font-weight:900;font-stretch:62%;font-size:56px;line-height:1;letter-spacing:0.18em;color:{GOLD}">TORNEIO DE</div>
  {star(330,162,28)}{star(840,162,28)}
  <div style="position:absolute;left:0;width:1200px;top:205px;text-align:center;font-weight:900;font-stretch:62%;font-size:380px;line-height:0.8;color:#ffffff;text-shadow:0 10px 40px rgba(60,0,0,0.35)">NATAL</div>
  <img src="{PL}" alt="Dupla mista de padel em jogo" style="position:absolute;left:{1240-pw/2:.0f}px;top:{930-pl_h}px;width:{pw:.0f}px;height:{pl_h}px;filter:drop-shadow(0 18px 24px rgba(60,0,0,0.45))">
  <div style="position:absolute;left:72px;top:540px;display:flex;align-items:center;gap:16px">
    <div style="background:{GREEN};border:2px solid {GOLD};border-radius:999px;padding:8px 22px;font-weight:900;font-size:24px;letter-spacing:0.06em">ESPECIAL EQUIPAS</div>
    <div style="font-weight:700;font-size:20px">Equipas de 4 elementos</div>
  </div>
  <div style="position:absolute;left:72px;width:620px;top:620px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px 30px">
    <div>{lab('CATEGORIAS',15)}<div style="font-weight:800;font-size:19px;line-height:1.3;margin-top:4px">Mistos Iniciante<br>Mistos Avançado<br>Masculinos Iniciante<br>Masculinos Avançado</div></div>
    <div>{lab('INSCRIÇÃO',15)}<div style="display:flex;align-items:baseline;gap:10px;margin-top:4px"><div style="font-weight:900;font-stretch:62%;font-size:56px;line-height:0.9">25€</div><div style="font-weight:700;font-size:17px">2ª categoria +10€</div></div></div>
    <div>{lab('WELCOME PACK',15)}<div style="font-weight:800;font-size:19px;line-height:1.3;margin-top:4px">T-shirt · Água · Voucher 1h30</div></div>
    <div>{lab('PRÉMIOS',15)}<div style="font-weight:800;font-size:19px;line-height:1.3;margin-top:4px">8 troféus<br>Prize money 1º e 2º lugar</div></div>
  </div>
  <div style="position:absolute;right:72px;width:300px;top:300px;display:flex;flex-direction:column;gap:16px;border-left:2px solid rgba(255,255,255,0.3);padding-left:22px">
    {lab('FASES',15)}
    <div><div style="font-weight:800;font-size:19px">01 a 14 Nov</div><div style="font-size:15px;color:#f3d6d6">Inscrições</div></div>
    <div><div style="font-weight:800;font-size:19px">15 a 22 Nov</div><div style="font-size:15px;color:#f3d6d6">Pagamentos</div></div>
    <div><div style="font-weight:800;font-size:19px">25 Nov</div><div style="font-size:15px;color:#f3d6d6">Grupo de WhatsApp</div></div>
    <div><div style="font-weight:800;font-size:19px">30 Nov</div><div style="font-size:15px;color:#f3d6d6">Divulgação do calendário</div></div>
  </div>
{sponsors(930,150,1920,72,6,vertical=False)}
</div>
</div>'''


def story_layout():
    W,H=1080,1920; T=150; pl_h=860; sc=pl_h/PH; pw=PW*sc; pb=1330
    return f'''<div class="ar" style="position:relative;width:{W}px;height:{H}px;overflow:hidden;background:radial-gradient(ellipse 80% 60% at 60% 38%,#d42a33 0%,{RED} 45%,{DRED} 100%);color:#ffffff">
  {snow(W,H,150,H)}
  <div style="position:absolute;left:56px;right:56px;top:{T}px;display:flex;align-items:center;justify-content:space-between">
    <img src="{LOGO}" alt="TomarPadel 2.0" style="width:270px;height:auto">
    <div style="border:2px solid #ffffff;border-radius:999px;padding:9px 20px;font-weight:800;font-size:20px;letter-spacing:0.14em">TORNEIO OFICIAL</div>
  </div>
  <div style="position:absolute;left:56px;right:56px;top:{T+92}px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;font-weight:800;font-size:22px;line-height:1.25">
    <div>{lab('DATA',16)}4 · 5 · 6 DEZEMBRO 2026</div>
    <div style="text-align:center">{lab('LOCAL',16)}TOMARPADEL 2.0 · TOMAR</div>
    <div style="text-align:right">{lab('INSCRIÇÕES',16)}01 A 14 NOVEMBRO</div>
  </div>
  <div style="position:absolute;left:0;right:0;top:360px;text-align:center;font-weight:900;font-stretch:62%;font-size:64px;line-height:1;letter-spacing:0.18em;color:{GOLD}">TORNEIO DE</div>
  {star(W//2-262,374,32)}{star(W//2+230,374,32)}{star(W-110,760,22)}{star(70,720,18)}{star(W-200,T+190,16)}
  <div style="position:absolute;left:0;right:0;top:424px;text-align:center;font-weight:900;font-stretch:62%;font-size:390px;line-height:0.8;color:#ffffff;text-shadow:0 10px 40px rgba(60,0,0,0.35)">NATAL</div>
  <img src="{PL}" alt="Dupla mista de padel em jogo" style="position:absolute;left:{W-pw:.0f}px;top:{pb-pl_h}px;width:{pw:.0f}px;height:{pl_h}px;filter:drop-shadow(0 18px 24px rgba(60,0,0,0.45))">
  <div style="position:absolute;left:56px;top:900px;width:330px;display:flex;flex-direction:column;gap:22px">
    <div style="display:flex;flex-direction:column;align-items:flex-start;gap:8px"><div style="background:{GREEN};border:2px solid {GOLD};border-radius:999px;padding:10px 22px;font-weight:900;font-size:24px;letter-spacing:0.06em;white-space:nowrap">ESPECIAL EQUIPAS</div><div style="font-weight:700;font-size:22px">Equipas de 4 elementos</div></div>
    <div>{lab('CATEGORIAS',17)}<div style="font-weight:800;font-size:23px;line-height:1.3;margin-top:6px">Mistos Iniciante<br>Mistos Avançado<br>Masculinos Iniciante<br>Masculinos Avançado</div></div>
  </div>
  <div style="position:absolute;left:56px;right:56px;top:1360px;display:grid;grid-template-columns:minmax(0,0.9fr) minmax(0,1fr) minmax(0,1.1fr);gap:24px;border-top:2px solid rgba(255,255,255,0.3);padding-top:18px">
    <div>{lab('INSCRIÇÃO',17)}<div style="font-weight:900;font-stretch:62%;font-size:72px;line-height:0.9;margin-top:4px">25€</div><div style="font-weight:700;font-size:20px;margin-top:4px">2ª categoria +10€</div></div>
    <div>{lab('WELCOME PACK',17)}<div style="font-weight:800;font-size:23px;line-height:1.3;margin-top:6px">T-shirt<br>Água<br>Voucher 1h30</div></div>
    <div>{lab('PRÉMIOS',17)}<div style="font-weight:800;font-size:23px;line-height:1.3;margin-top:6px">8 troféus<br>Prize money para<br>1º e 2º lugar</div></div>
  </div>
{phases(1575,56,56,21,16)}
{sponsors(1680,150,W,56,5)}
</div>'''

def wrap(title,body,w,h):
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
HELMET
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
post=portrait(1080,1350,52,230,330,800,1130,680,1142,1212,138)
story=story_layout()
a4b=portrait(1080,1528,60,240,350,900,1290,760,1300,1380,148)
a4=f'<div class="ar" style="position:relative;width:794px;height:1123px;overflow:hidden;background:{DRED}"><div style="position:absolute;left:0;top:0;width:1080px;height:1528px;transform:scale(0.735185);transform-origin:0 0">'+a4b.replace('<div class="ar" ','<div ',1)+'</div></div>'
open(R+'NatalPost.dc.html','w').write(wrap('Torneio de Natal post',post,1080,1350))
open(R+'NatalStory.dc.html','w').write(wrap('Torneio de Natal story',story,1080,1920))
open(R+'NatalA4.dc.html','w').write(wrap('Torneio de Natal cartaz A4',a4,794,1123))
open(R+'NatalTV.dc.html','w').write(wrap('Torneio de Natal TV 4K',landscape(),3840,2160))
print('ok')
