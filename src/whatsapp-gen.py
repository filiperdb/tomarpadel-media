import os
A='file:///home/claude/bk/'
FONT=f"""@font-face{{font-family:'Archivo';src:url('{A}assets/archivo.woff2');font-weight:100 900;font-stretch:62% 125%}}"""
NAVY='radial-gradient(circle at 50% 40%,#1f5a96 0%,#15406e 55%,#0f3157 100%)'
DARK='radial-gradient(circle at 50% 40%,#173f6a 0%,#0f2c4f 60%,#0a213c 100%)'
BLUE='radial-gradient(circle at 50% 40%,#3cc3f0 0%,#12ace3 55%,#0b8fc0 100%)'
WHITE='radial-gradient(circle at 50% 40%,#ffffff 0%,#eef3f7 60%,#dce7f1 100%)'
RED='radial-gradient(circle at 50% 40%,#e0213f 0%,#c8102e 55%,#9e0b23 100%)'
I={
'briefcase':'<rect x="2.5" y="7" width="19" height="13.5" rx="2.2"/><path d="M8.5 7V5.2A2.2 2.2 0 0 1 10.7 3h2.6a2.2 2.2 0 0 1 2.2 2.2V7M2.5 13h19M10.5 13v1.5h3V13"/>',
'badge':'<rect x="4" y="3" width="16" height="18.5" rx="2.5"/><path d="M9.5 3v2.5h5V3"/><circle cx="12" cy="11" r="2.6"/><path d="M7.8 18c.6-2 2.2-3.2 4.2-3.2s3.6 1.2 4.2 3.2"/>',
'bulb':'<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6M10 22h4"/>',
'sunrise':'<path d="M12 2v6M4.93 10.93l1.41 1.41M2 18h2M20 18h2M19.07 10.93l-1.41 1.41M22 22H2M8 6l4-4 4 4M16 18a4 4 0 0 0-8 0"/>',
'racket':'<g transform="rotate(-35 12 12)"><rect x="6.2" y="1.6" width="11.6" height="13.4" rx="5.8"/><path d="M10.4 15v2.2M13.6 15v2.2"/><rect x="10.3" y="17" width="3.4" height="5.6" rx="1.2"/></g><g stroke="none" fill="currentColor"><circle cx="7.6" cy="8.6" r=".85"/><circle cx="9.9" cy="7.0" r=".85"/><circle cx="9.3" cy="10.3" r=".85"/><circle cx="11.6" cy="8.7" r=".85"/><circle cx="11.0" cy="12.0" r=".85"/><circle cx="13.3" cy="10.4" r=".85"/><circle cx="12.2" cy="5.5" r=".85"/></g>',
'trophy':'<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22M18 2H6v7a6 6 0 0 0 12 0V2Z"/>',
}
def svg(k,s,c='#fff'): return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="{c}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="color:{c}">{I[k]}</svg>'
def logo(white=True,h=64): return f'<img src="{A}logos/{"branco" if white else "azul"}_simbolo20.png" style="height:{h}px">'
import os as _o
WM=_o.environ.get('WM','0')=='1'
def page(bg,inner,fg='#fff'):
    dark = fg=='#fff'
    wm=(f'<img src="{A}logos/{"branco" if dark else "azul"}_simbolo20.png" style="position:absolute;left:50%;top:50%;width:960px;transform:translate(-50%,-50%);opacity:{(.26 if bg==BLUE else .17) if dark else .13};pointer-events:none">' if WM else '')
    inner=wm+'<div style="position:relative;display:flex;flex-direction:column;align-items:center">'+inner+'</div>'
    return f"""<!doctype html><meta charset=utf-8><style>{FONT}*{{margin:0;box-sizing:border-box}}body{{position:relative;overflow:hidden;width:1080px;height:1080px;background:{bg};color:{fg};font-family:Archivo;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.lab{{font-weight:900;font-stretch:112%;letter-spacing:-.01em;text-transform:uppercase;line-height:.95}}.sub{{font-weight:700;font-size:44px;letter-spacing:.18em;text-transform:uppercase;opacity:.85}}</style><body>{inner}</body>"""
def icon_page(k,label,size=96,bg=NAVY,sub=None):
    s=f'<div style="margin:0 0 40px">{svg(k,280)}</div><div class="lab" style="font-size:{size}px">{label}</div>'
    if sub: s+=f'<div class="sub" style="font-size:36px;margin-top:18px">{sub}</div>'
    return page(bg,s)
P={}
P['01-comunidade']=page(NAVY,f'<img src="{A}logos/branco_vertical.png" style="width:560px"><div class="lab" style="margin-top:50px;font-size:104px">Comunidade</div>')
P['02-gerencia']=icon_page('briefcase','Gerência',bg=DARK)
P['03-staff']=icon_page('badge','Staff',size=120,bg=DARK)
P['04-ricardo-santos']=page(NAVY,f'<div class="lab" style="font-size:120px">Ricardo<br>Santos</div><div class="sub" style="font-size:40px;margin-top:20px;letter-spacing:.08em">Treinador &amp; Relações Públicas</div>')
P['05-professores']=icon_page('racket','Professores',size=92)
P['06-tips-tricks']=icon_page('bulb','Tips &amp; Tricks',size=96,bg=BLUE)
P['07-alvoradas']=icon_page('sunrise','Alvoradas',size=100,bg=NAVY)
lv=[('F4','F'),('F5','F'),('F6','F'),('M3','M'),('M3+','M'),('M4','M'),('M4+','M'),('M5','M'),('M5+','M'),('M6','M'),('Mx4','X'),('Mx5','X'),('Mx6','X')]
T={'F':(BLUE,'#fff','Feminino',True),'M':(NAVY,'#fff','Masculino',True),'X':(WHITE,'#15406e','Misto',False)}
for i,(n,t) in enumerate(lv):
    bg,fg,sub,w=T[t]
    acc='#5fd0f5' if t=='M' else ('#ffffff' if t=='F' else '#12ace3')
    P[f'{8+i:02d}-{n.lower().replace("+","-mais")}']=page(bg,f'<div class="lab" style="font-size:{400 if len(n)<3 else 330}px;letter-spacing:-.05em;text-transform:none">{n.replace("+","<span style=&quot;color:"+acc+"&quot;>+</span>")}</div>',fg)
ball='<svg viewBox="0 0 100 100" width="110" height="110" style="position:absolute;right:200px;top:20px;filter:drop-shadow(0 10px 16px rgba(0,0,0,.3))"><defs><radialGradient id="bg" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#e4f27a"/><stop offset=".6" stop-color="#c6dc3c"/><stop offset="1" stop-color="#93ad16"/></radialGradient><clipPath id="cc"><circle cx="50" cy="50" r="47"/></clipPath></defs><circle cx="50" cy="50" r="47" fill="url(#bg)"/><g clip-path="url(#cc)" fill="none" stroke="#fbfdf0" stroke-width="4.2" stroke-linecap="round"><path d="M14 6 C 40 26, 40 74, 14 94"/><path d="M86 6 C 60 26, 60 74, 86 94"/></g></svg>'
P['21-torneio-natal-equipas']=page(RED,f'<div style="position:relative;width:100%;display:flex;flex-direction:column;align-items:center">{ball}<div style="margin-top:-20px">{logo(h=130)}</div><div class="lab" style="font-size:44px;letter-spacing:.3em;margin-top:40px;font-stretch:125%">Torneio de</div><div class="lab" style="font-size:196px;font-stretch:118%;letter-spacing:-.03em;margin-top:6px">Natal</div><div style="background:#fff;color:#c8102e;font-weight:900;font-size:50px;letter-spacing:.08em;padding:12px 36px;margin-top:30px;text-transform:uppercase;font-stretch:115%">Equipas</div><div class="sub" style="font-size:34px;margin-top:26px">4 · 5 · 6 Dezembro</div></div>')
from playwright.sync_api import sync_playwright
OUT='out_wm' if WM else 'out';os.makedirs(OUT,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1080})
    for n,h in P.items():
        open('t.html','w').write(h);pg.goto('file:///home/claude/wa/t.html');pg.wait_for_timeout(250);pg.screenshot(path=f'{OUT}/{n}.png')
    b.close()
# preview sheet with circle crop
from PIL import Image,ImageDraw
fs=sorted(os.listdir(OUT));fs=[f for f in fs if f[0].isdigit()]
C=7;S=200;G=24;rows=(len(fs)+C-1)//C
sheet=Image.new('RGB',(C*(S+G)+G,rows*(S+G)+G),(11,20,26))
m=Image.new('L',(S,S),0);ImageDraw.Draw(m).ellipse((0,0,S,S),fill=255)
for i,f in enumerate(fs):
    im=Image.open(OUT+'/'+f).convert('RGB').resize((S,S),Image.LANCZOS)
    sheet.paste(im,(G+(i%C)*(S+G),G+(i//C)*(S+G)),m)
sheet.save('sheet_wm.png' if WM else 'sheet.png')
