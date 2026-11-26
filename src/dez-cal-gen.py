import os,datetime as dt
A='file:///home/claude/bk/'
FONT=f"""@font-face{{font-family:'Archivo';src:url('{A}assets/archivo.woff2');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:'Instrument Serif';src:url('{A}assets/instrument-italic.woff2');font-style:italic}}
*{{margin:0;box-sizing:border-box}}body{{font-family:Archivo}}.sr{{font-family:'Instrument Serif';font-style:italic;font-weight:400}}"""
NAVY='#15406e';LB='#12ace3';LIME='#bfd84a';RED='#e0213f'
EV=[('01','TER','Feriado','Estamos abertos.','Feriado',LIME),
('4 a 6','SEX a DOM','Torneio de Natal','Especial equipas · Mistos e Masculinos<br>Iniciante e Avançado','Torneio',RED),
('08','TER','Feriado','Estamos abertos.','Feriado',LIME),
('24','QUI','Véspera de Natal','Aberto até às 18:00.','Horário especial',LB),
('25','SEX','Dia de Natal','Clube fechado.','Fechado','#ffffff'),
('31','QUI','Passagem de ano','Aberto até às 18:00.','Horário especial',LB)]
def ev_rows(fs=1.0):
    out=''
    for i,(d,w,t,sub,pill,c) in enumerate(EV):
        bb=';border-bottom:2px solid rgba(255,255,255,.22)' if i==len(EV)-1 else ''
        dsz=80 if len(d)<=2 else 58
        out+=f'''<div style="display:grid;grid-template-columns:{150*fs}px minmax(0,1fr) auto;gap:{26*fs}px;align-items:center;padding:{11*fs}px 0;border-top:2px solid rgba(255,255,255,.22){bb}">
<div><div style="font-weight:900;font-stretch:62%;font-size:{dsz*fs}px;line-height:.85;white-space:nowrap">{d}</div><div style="font-style:italic;font-weight:600;font-size:{19*fs}px;letter-spacing:.12em;margin-top:{6*fs}px">{w}</div></div>
<div><div style="font-weight:800;font-stretch:104%;font-size:{36*fs}px;line-height:1.05">{t}</div><div style="font-size:{21*fs}px;line-height:1.35;color:#c9d7e6;margin-top:{6*fs}px">{sub}</div></div>
<div style="border:2px solid {c};color:{c};border-radius:999px;padding:{7*fs}px {18*fs}px;font-weight:700;font-size:{19*fs}px;white-space:nowrap">{pill}</div></div>'''
    return out
def header(label,logo='branco',col=LIME,fs=1.0):
    return f'<div style="display:flex;align-items:center;justify-content:space-between"><img src="{A}logos/{logo}_simbolo20.png" style="height:{72*fs}px"><div style="font-style:italic;font-weight:600;font-size:{22*fs}px;letter-spacing:.12em;text-transform:uppercase;color:{col}">{label}</div></div>'
LINES='<svg width="1080" height="1350" viewBox="0 0 1080 1350" style="position:absolute;left:0;top:0"><g fill="none" stroke="#fff" stroke-opacity=".07" stroke-width="4"><rect x="620" y="-60" width="560" height="560"/><line x1="900" y1="-60" x2="900" y2="500"/><line x1="620" y1="200" x2="1180" y2="200"/></g></svg>'
def eventos_post():
    return f'''<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:{NAVY};color:#fff">{LINES}
<div style="position:absolute;left:64px;right:64px;top:56px">{header('Agenda do mês')}</div>
<div style="position:absolute;left:64px;top:176px"><div class="sr" style="font-size:84px;line-height:.9;color:{LB}">agenda de</div><div style="font-weight:900;font-stretch:62%;font-size:200px;line-height:.84;text-transform:uppercase">Dezembro</div></div>
<div style="position:absolute;left:64px;right:64px;top:440px">{ev_rows()}</div>
<div style="position:absolute;left:64px;right:64px;top:1230px;display:flex;justify-content:space-between;align-items:center"><div style="font-size:26px">Boas festas, de toda a equipa TomarPadel!</div><img src="{A}logos/branco_horizontal.png" style="width:300px"></div></div>'''
# promo grid
def cell(d,h=92,fs=1.0):
    base=f'height:{h}px;border-radius:{14*fs}px;padding:{10*fs}px {12*fs}px;display:flex;flex-direction:column;justify-content:space-between;font-weight:800;font-size:{26*fs}px;line-height:1;'
    if d is None: return f'<div style="{base}"></div>'
    wd=dt.date(2026,12,d).weekday()
    st='background:transparent;color:#5b7591;border:2px solid #d3dde8;'
    if wd==0: st=f'background:{LB};color:#0b2a4c;'
    elif wd==2: st=f'background:{NAVY};color:#fff;'
    elif wd==4 and d not in (4,25): st=f'background:#fff;color:{NAVY};border:3px solid {NAVY};'
    tag=''
    def t(c,txt,ring='#0b2a4c'): return f'<div style="display:flex;align-items:center;gap:{6*fs}px"><div style="flex:none;width:{16*fs}px;height:{16*fs}px;border-radius:50%;background:{c};box-shadow:inset 0 0 0 2px {ring}"></div><div style="font-size:{12*fs}px;font-weight:800;line-height:1">{txt}</div></div>'
    if d in (4,5,6): st=f'background:{RED};color:#fff;';tag=t('#fff','NATAL',RED)
    if d in (1,8): tag=t(LIME,'FERIADO')
    if d in (24,31): tag=t(LIME,'ATÉ 18H')
    if d==25: st='background:repeating-linear-gradient(135deg,#dfe7ef 0 8px,#eef3f7 8px 16px);color:#8aa0b6;border:2px solid #d3dde8;';tag=f'<div style="font-size:{12*fs}px;font-weight:800">FECHADO</div>'
    return f'<div style="{base}{st}"><div>{d}</div>{tag}</div>'
def grid(h=92,fs=1.0,gap=10):
    days=[None]+list(range(1,32)); days+= [None]*((7-len(days)%7)%7)
    return f'<div style="display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:{gap}px;font-style:italic;font-weight:700;font-size:{20*fs}px;letter-spacing:.1em;margin-bottom:{14*fs}px"><div>SEG</div><div>TER</div><div>QUA</div><div>QUI</div><div>SEX</div><div>SÁB</div><div>DOM</div></div><div style="display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:{gap}px">'+''.join(cell(d,h,fs) for d in days)+'</div>'
LEG=[(f'background:{LB}','Segundas · Promoção','22:30 às 00:00: joga e habilita-te ao sorteio de um voucher de 1h30 para um dos 4 jogadores.'),
(f'background:{NAVY}','Quartas · Desafio do mês','Roleta da sorte.'),
(f'background:#fff;border:3px solid {NAVY}','Sextas · Happy Hour','Imperial a 1€, das 15:00 às 02:00. Exceto dia 4 (torneio) e dia 25 (fechado).'),
(f'background:{RED}','Torneio de Natal','4, 5 e 6 de dezembro.'),
(f'background:{LIME};border-radius:50%','Horários especiais','Feriados 1 e 8: abertos. Dias 24 e 31: até às 18:00. Dia 25: fechado.')]
def legend(fs=1.0,cols=2):
    return f'<div style="display:grid;grid-template-columns:repeat({cols},minmax(0,1fr));gap:{16*fs}px {30*fs}px">'+''.join(f'<div style="display:grid;grid-template-columns:{26*fs}px minmax(0,1fr);gap:{14*fs}px;align-items:start"><div style="width:{26*fs}px;height:{26*fs}px;border-radius:{8*fs}px;{sw};margin-top:2px"></div><div><div style="font-weight:800;font-size:{22*fs}px">{a}</div><div style="font-size:{17*fs}px;line-height:1.35;margin-top:{4*fs}px">{b}</div></div></div>' for sw,a,b in LEG)+'</div>'
def promos_post():
    return f'''<div style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#eef3f7;color:{NAVY}">
<div style="position:absolute;left:64px;right:64px;top:56px">{header('Calendário do mês','azul',NAVY)}</div>
<div style="position:absolute;left:64px;top:166px"><div class="sr" style="font-size:64px;line-height:.95">promoções e horários de</div><div style="font-weight:900;font-stretch:62%;font-size:168px;line-height:.84;text-transform:uppercase">Dezembro</div></div>
<div style="position:absolute;left:64px;right:64px;top:412px">{grid()}</div>
<div style="position:absolute;left:64px;right:64px;top:984px">{legend()}</div></div>'''
def story(inner,bg):
    return f'<div style="position:relative;width:1080px;height:1920px;overflow:hidden;background:{bg}"><div style="position:absolute;left:0;top:275px">{inner}</div></div>'
def tv_eventos():
    return f'''<div style="position:relative;width:1920px;height:1080px;overflow:hidden;background:{NAVY};color:#fff">
<div style="position:absolute;left:90px;top:70px;width:640px">{header('Agenda do mês')}</div>
<div style="position:absolute;left:90px;top:300px"><div class="sr" style="font-size:110px;line-height:.9;color:{LB}">agenda de</div><div style="font-weight:900;font-stretch:62%;font-size:178px;line-height:.84;text-transform:uppercase">Dezembro</div>
<div style="font-size:30px;margin-top:60px;max-width:620px;line-height:1.35">Boas festas, de toda a equipa TomarPadel!</div><img src="{A}logos/branco_horizontal.png" style="width:340px;margin-top:40px"></div>
<div style="position:absolute;left:860px;right:90px;top:110px">{ev_rows(1.12)}</div></div>'''
def tv_promos():
    return f'''<div style="position:relative;width:1920px;height:1080px;overflow:hidden;background:#eef3f7;color:{NAVY}">
<div style="position:absolute;left:80px;top:64px;width:560px">{header('Calendário do mês','azul',NAVY)}</div>
<div style="position:absolute;left:80px;top:210px;width:600px"><div class="sr" style="font-size:66px;line-height:.95">promoções e horários de</div><div style="font-weight:900;font-stretch:62%;font-size:140px;line-height:.84;text-transform:uppercase">Dezembro</div>
<div style="margin-top:44px">{legend(1.05,1)}</div></div>
<div style="position:absolute;left:760px;right:80px;top:120px">{grid(146,1.3,14)}</div></div>'''
P={'eventos-dezembro-post':(1080,1350,1,eventos_post()),'eventos-dezembro-story':(1080,1920,1,story(eventos_post(),NAVY)),
'promocoes-dezembro-post':(1080,1350,1,promos_post()),'promocoes-dezembro-story':(1080,1920,1,story(promos_post(),'#eef3f7')),
'eventos-dezembro-tv-4k':(1920,1080,2,tv_eventos()),'promocoes-dezembro-tv-4k':(1920,1080,2,tv_promos())}
from playwright.sync_api import sync_playwright
os.makedirs('out',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch()
    for n,(w,h,sc,html) in P.items():
        open('t.html','w').write(f'<!doctype html><meta charset=utf-8><style>{FONT}</style><body>{html}</body>')
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=sc);pg.goto('file:///home/claude/dez/t.html');pg.wait_for_timeout(500);pg.screenshot(path=f'out/{n}.png');pg.close()
    b.close()
from PIL import Image
a=Image.open('out/eventos-dezembro-post.png').resize((540,675));b2=Image.open('out/promocoes-dezembro-post.png').resize((540,675))
c=Image.open('out/eventos-dezembro-tv-4k.png').resize((640,360));d=Image.open('out/promocoes-dezembro-tv-4k.png').resize((640,360))
e=Image.open('out/eventos-dezembro-story.png').resize((380,675));f=Image.open('out/promocoes-dezembro-story.png').resize((380,675))
S=Image.new('RGB',(540*2+380*2+30,675+380),'white');S.paste(a,(0,0));S.paste(b2,(550,0));S.paste(e,(1100,0));S.paste(f,(1490,0));S.paste(c,(0,685));S.paste(d,(650,685));S.save('sheet.png')
