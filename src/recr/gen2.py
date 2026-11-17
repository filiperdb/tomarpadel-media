A='file:///home/claude/bk/'
FONT=f'''@font-face{{font-family:'Archivo';src:url('{A}assets/archivo.woff2');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:'Instrument Serif';src:url('{A}assets/instrument-italic.woff2');font-style:italic}}'''
BASE='''*{box-sizing:border-box;margin:0}
body{width:1080px;height:HHpx;overflow:hidden;font-family:'Archivo';color:#fff;background:radial-gradient(120% 80% at 80% 0%,#1d5a96 0%,#15406e 45%,#0c2a4c 100%);position:relative}
.sr{font-family:'Instrument Serif';font-style:italic;font-weight:400}
.big{font-weight:900;font-stretch:118%;letter-spacing:-.04em;line-height:.84;text-transform:uppercase}
.out{color:transparent;-webkit-text-stroke:3px #fff}
.acc{color:#5fd0f5}
.chip{display:inline-block;background:#fff;color:#15406e;font-weight:800;border-radius:999px}
.sec{font-weight:800;font-size:26px;letter-spacing:.16em;text-transform:uppercase;color:#5fd0f5;display:flex;align-items:center;gap:14px}
.sec:before{content:'';width:34px;height:5px;background:#bfd84a;border-radius:3px}
.it{display:flex;gap:28px;align-items:center;font-size:41px;font-weight:700;line-height:1.2;padding:34px 0;border-bottom:2px solid rgba(255,255,255,.12)}
.it .n{flex:0 0 84px;height:84px;border-radius:18px;background:rgba(95,208,245,.16);color:#5fd0f5;display:flex;align-items:center;justify-content:center;font-size:44px}
.lg{position:absolute;height:64px}
.dots{position:absolute;right:56px;display:flex;gap:10px}.dots i{width:12px;height:12px;border-radius:50%;background:rgba(255,255,255,.3)}.dots i.on{background:#fff;width:34px;border-radius:6px}
'''
def doc(h,body): return f"<!doctype html><html><head><meta charset=utf-8><style>{FONT}{BASE.replace('HH',str(h))}</style></head><body>{body}<script>document.fonts.ready.then(()=>{{document.querySelectorAll('.fit').forEach(e=>{{let f=300;e.style.fontSize=f+'px';e.style.whiteSpace='nowrap';e.style.display='inline-block';while(e.getBoundingClientRect().width>936&&f>40){{f-=2;e.style.fontSize=f+'px'}}}});let a=document.getElementById('a'),v=document.getElementById('v');if(a){{let f=400;a.style.display=v.style.display='inline-block';a.style.fontSize=f+'px';while(a.getBoundingClientRect().width>936){{f-=2;a.style.fontSize=f+'px'}}v.style.fontSize=f+'px';v.style.display='block';a.style.display='block'}}}})</script></body></html>"
def dots(n,top): return f'<div class="dots" style="top:{top}px">'+''.join(f'<i class="{"on" if i==n else ""}"></i>' for i in range(3))+'</div>'
ball='''<svg viewBox="0 0 100 100" width="W" height="W" style="position:absolute;POS;filter:drop-shadow(0 14px 22px rgba(0,0,0,.35))"><defs><radialGradient id="bg" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#e4f27a"/><stop offset=".6" stop-color="#c6dc3c"/><stop offset="1" stop-color="#93ad16"/></radialGradient><clipPath id="cc"><circle cx="50" cy="50" r="47"/></clipPath></defs><circle cx="50" cy="50" r="47" fill="url(#bg)"/><g clip-path="url(#cc)" fill="none" stroke="#fbfdf0" stroke-width="4.2" stroke-linecap="round"><path d="M14 6 C 40 26, 40 74, 14 94"/><path d="M86 6 C 60 26, 60 74, 86 94"/></g></svg>'''
# SLIDE 1 cover
s1=doc(1350,f'''
<img class="lg" src="{A}logos/branco_simbolo20.png" style="left:72px;top:60px">
{dots(0,86)}
<div style="position:absolute;left:72px;top:200px" class="sr acc"><span style="font-size:80px;line-height:1.02">Gostas de padel<br>e de pessoas?</span></div>
<div style="position:absolute;left:72px;top:390px"><div class="big" id="v" style="line-height:.86">Estamos a</div><div class="big acc" id="a" style="line-height:.86">contratar.</div></div>
<div style="position:absolute;left:72px;right:72px;top:690px;height:400px;border-radius:28px;overflow:hidden"><img src="{A}assets/fotos-out2026/foto-05.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 38%"></div>
<div style="position:absolute;left:72px;right:72px;bottom:150px;display:flex;align-items:center;gap:22px">
<div class="chip" style="font-size:44px;padding:18px 40px">Receção &amp; Bar</div>
<div style="font-size:30px;font-weight:600;opacity:.85;line-height:1.25">Vem fazer parte<br>da nossa equipa</div></div>
<div style="position:absolute;left:72px;right:72px;bottom:70px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:26px;letter-spacing:.06em;opacity:.8"><span>DESLIZA PARA SABER MAIS</span><span style="font-size:44px">→</span></div>
''')
ball1=ball.replace('W','150').replace('POS','right:90px;top:170px')
s1=s1.replace('</body>',ball1+'</body>')
# SLIDE 2
items2=[('🛎️','Receber os jogadores e fazer o check&#8209;in'),('📅','Apoio na receção e nas reservas'),('🍺','Trabalho de bar'),('🏆','Ajudar nos jogos e torneios'),('✨','Manter o clube funcional, arrumado e limpo')]
s2=doc(1350,f'''
<img class="lg" src="{A}logos/branco_simbolo20.png" style="left:72px;top:60px">{dots(1,86)}
<div style="position:absolute;left:72px;right:72px;top:190px">
<div class="sr acc" style="font-size:96px;line-height:1">O que</div><div class="big" style="font-size:132px;white-space:nowrap">vais fazer.</div>
<div style="margin-top:46px">'''+''.join(f'<div class="it"><span class="n">{e}</span>{t}</div>' for e,t in items2)+'''</div></div>''')
# SLIDE 3
s3=doc(1350,f'''
<img class="lg" src="{A}logos/branco_simbolo20.png" style="left:72px;top:60px">{dots(2,86)}
<div style="position:absolute;left:72px;right:72px;top:180px">
<div class="sec">Procuramos</div>
<div style="font-size:52px;font-weight:800;line-height:1.15;margin-top:18px">Boa energia, simpatia e<br>vontade de aprender.</div>
<div style="font-size:30px;opacity:.8;margin-top:12px;line-height:1.35">Experiência em bar ou atendimento é uma vantagem.</div>
<div class="sec" style="margin-top:58px">Oferecemos</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px">
<div style="background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.14);border-radius:24px;padding:34px 30px;font-size:36px;font-weight:700;line-height:1.2;min-height:240px"><div style="font-size:56px;margin-bottom:14px">🎓</div>Formação desde o primeiro dia</div>
<div style="background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.14);border-radius:24px;padding:34px 30px;font-size:36px;font-weight:700;line-height:1.2;min-height:240px"><div style="font-size:56px;margin-bottom:14px">🤝</div>Ambiente descontraído e espírito de equipa</div>
<div style="background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.14);border-radius:24px;padding:34px 30px;font-size:36px;font-weight:700;line-height:1.2;min-height:240px"><div style="font-size:56px;margin-bottom:14px">🚀</div>Oportunidade de crescimento</div>
<div style="background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.14);border-radius:24px;padding:34px 30px;font-size:36px;font-weight:700;line-height:1.2;min-height:240px"><div style="font-size:56px;margin-bottom:14px">🎾</div>Trabalhar no meio do padel</div>
</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:250px;background:#fff;color:#15406e;padding:40px 72px;display:flex;justify-content:space-between;align-items:center">
<div><div style="font-weight:800;font-size:24px;letter-spacing:.16em;text-transform:uppercase;color:#12ace3">Candidata-te já</div>
<div style="font-weight:800;font-size:40px;margin-top:10px">tomarpadel@gmail.com</div>
<div style="font-weight:800;font-size:40px;margin-top:4px">WhatsApp 916 563 352</div></div>
<img src="{A}logos/azul_vertical.png" style="height:180px"></div>''')
# STORY
st=doc(1920,f'''
<img class="lg" src="{A}logos/branco_simbolo20.png" style="left:72px;top:250px">
<div style="position:absolute;left:72px;top:380px" class="sr acc"><span style="font-size:80px;line-height:1.02">Gostas de padel<br>e de pessoas?</span></div>
<div style="position:absolute;left:72px;top:560px"><div class="big" id="v" style="line-height:.86">Estamos a</div><div class="big acc" id="a" style="line-height:.86">contratar.</div></div>
<div style="position:absolute;left:72px;right:72px;top:930px">
<div class="chip" style="font-size:46px;padding:18px 40px">Receção &amp; Bar</div>
<div style="margin-top:34px;font-size:40px;font-weight:700;line-height:1.6">
<div>🛎️ Check-in dos jogadores e reservas</div><div>🍺 Trabalho de bar</div><div>🏆 Apoio nos jogos e torneios</div><div>✨ Clube funcional, arrumado e limpo</div></div></div>
<div style="position:absolute;left:72px;right:72px;top:1400px;background:#fff;color:#15406e;border-radius:28px;padding:30px 36px">
<div style="font-weight:800;font-size:24px;letter-spacing:.16em;text-transform:uppercase;color:#12ace3">Responde a esta story ou envia</div>
<div style="font-weight:800;font-size:38px;margin-top:8px">tomarpadel@gmail.com</div>
<div style="font-weight:800;font-size:38px">WhatsApp 916 563 352</div></div>
''').replace('</body>',ball.replace('W','150').replace('POS','right:90px;top:360px')+'</body>')
def light(d):
    R=[('background:radial-gradient(120% 80% at 80% 0%,#1d5a96 0%,#15406e 45%,#0c2a4c 100%)','background:radial-gradient(120% 80% at 80% 0%,#ffffff 0%,#eef3f7 55%,#dfe8f1 100%)'),
    ('color:#fff;background:radial','color:#15406e;background:radial'),('.acc{color:#5fd0f5}','.acc{color:#12ace3}'),
    ('logos/branco_simbolo20.png','logos/azul_simbolo20.png'),('.chip{display:inline-block;background:#fff;color:#15406e','.chip{display:inline-block;background:#15406e;color:#fff'),
    ('color:#5fd0f5;display:flex','color:#12ace3;display:flex'),('border-bottom:2px solid rgba(255,255,255,.12)','border-bottom:2px solid rgba(21,64,110,.12)'),
    ('background:rgba(95,208,245,.16);color:#5fd0f5','background:rgba(18,172,227,.12);color:#12ace3'),
    ('background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.14)','background:#fff;border:2px solid rgba(21,64,110,.1)'),
    ('.dots i{width:12px;height:12px;border-radius:50%;background:rgba(255,255,255,.3)}.dots i.on{background:#fff','.dots i{width:12px;height:12px;border-radius:50%;background:rgba(21,64,110,.25)}.dots i.on{background:#15406e'),
    ('height:250px;background:#fff;color:#15406e','height:250px;background:#15406e;color:#fff'),('color:#12ace3">Candidata-te já','color:#5fd0f5">Candidata-te já'),
    ('<img src="'+A+'logos/azul_vertical.png" style="height:180px">','<img src="'+A+'logos/branco_vertical.png" style="height:180px">'),
    ('top:1400px;background:#fff;color:#15406e','top:1400px;background:#15406e;color:#fff'),('color:#12ace3">Responde','color:#5fd0f5">Responde'),
    ('box-shadow:0 20px 50px rgba(0,0,0,.3)','box-shadow:0 20px 50px rgba(0,0,0,.12)')]
    for a,b in R: d=d.replace(a,b)
    return d
for n,h,d in [('vaga-1',1350,s1),('vaga-2',1350,s2),('vaga-3',1350,s3),('vaga-story',1920,st)]:
    open(n+'.html','w').write(d); open(n+'-claro.html','w').write(light(d))
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,h in [(a+x,h) for a,h in [('vaga-1',1350),('vaga-2',1350),('vaga-3',1350),('vaga-story',1920)] for x in ('','-claro')]:
        pg=b.new_page(viewport={'width':1080,'height':h});pg.goto(f'file:///home/claude/recr/{n}.html');pg.wait_for_timeout(1500);pg.screenshot(path=f'{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'{n}-claro.png').resize((432,540)) for n in ['vaga-1','vaga-2','vaga-3']]+[Image.open('vaga-story-claro.png').resize((432,768))]
S=Image.new('RGB',(432*4+30,768),'white')
for i,im in enumerate(ims):S.paste(im,(i*442,0))
S.save('sheet2.png')
