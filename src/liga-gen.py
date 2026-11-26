A='file:///home/claude/bk/'
FONT=f"""@font-face{{font-family:'Archivo';src:url('{A}assets/archivo.woff2');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:'Instrument Serif';src:url('{A}assets/instrument-italic.woff2');font-style:italic}}"""
CSS='''*{margin:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;position:relative;font-family:Archivo;color:#fff;background:#0f3157}
.ph{position:absolute;left:0;top:0;width:100%;height:860px;object-fit:cover}
.gr{position:absolute;left:0;right:0;top:0;height:864px;background:linear-gradient(180deg,rgba(15,49,87,.75) 0%,rgba(15,49,87,.25) 28%,rgba(15,49,87,.55) 60%,#0f3157 100%)}
.bgw{position:absolute;inset:0;background:radial-gradient(110% 70% at 80% 0%,#1d5a96 0%,#15406e 45%,#0c2a4c 100%)}
.wm{position:absolute;left:50%;top:58%;width:1500px;transform:translate(-50%,-50%);opacity:.05}
.top{position:absolute;left:80px;right:80px;top:240px;display:flex;justify-content:space-between;align-items:center}
.top img{height:64px}
.kick{font-weight:800;font-size:24px;letter-spacing:.18em;text-transform:uppercase;color:#5fd0f5}
.sr{font-family:'Instrument Serif';font-style:italic;font-weight:400;color:#5fd0f5}
.sr+.tt{margin-top:22px!important}.tt{font-weight:900;font-stretch:112%;letter-spacing:-.03em;line-height:1.02;text-transform:uppercase}
.c{position:absolute;left:80px;right:80px}
.card{background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.13);border-radius:28px;padding:30px 34px}
.p{font-size:39px;line-height:1.4;font-weight:500}
.p b{font-weight:800}
.num{flex:0 0 66px;height:66px;border-radius:20px;background:#5fd0f5;color:#0f3157;font-weight:900;font-size:34px;display:flex;align-items:center;justify-content:center}
.row{display:flex;gap:26px;align-items:flex-start}
.chip{display:inline-block;background:#fff;color:#15406e;font-weight:800;border-radius:999px;padding:14px 34px;font-size:34px}
.lime{display:inline-block;width:36px;height:6px;background:#bfd84a;border-radius:3px;vertical-align:middle;margin-right:14px}
.foot{position:absolute;left:80px;right:80px;top:1640px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:24px;letter-spacing:.12em;text-transform:uppercase;opacity:.7}
'''
def page(inner,photo=None,pos='50% 50%',n=None):
    bg=(f'<div class="bgw"></div><img class="ph" src="{photo}" style="object-position:{pos}"><div class="gr"></div>' if photo else f'<div class="bgw"></div><img class="wm" src="{A}logos/branco_simbolo20.png">')
    foot=f'<div class="foot"><span>Clube TomarPadel</span><span>{n}/5</span></div>' if n else ''
    return f'<!doctype html><meta charset=utf-8><style>{FONT}{CSS}</style><body>{bg}<div class="top"><img src="{A}logos/branco_simbolo20.png"><div class="kick">Liga de Clubes 2027</div></div>{inner}{foot}</body>'
P={}
P['1-capa']=page(f'''<div class="c" style="top:690px"><div class="sr" style="font-size:110px;line-height:1">Liga de Clubes</div><div class="tt" style="font-size:300px;margin-top:6px">2027</div>
<div style="margin-top:26px;font-weight:800;font-size:44px;letter-spacing:.04em">CLUBE TOMARPADEL</div>
<div class="card" style="margin-top:56px;display:flex;justify-content:space-between;align-items:center"><div><div class="kick" style="font-size:22px">Pré-inscrições abertas</div><div style="font-weight:900;font-size:56px;margin-top:8px;line-height:1">até 31 de dezembro</div></div><div style="font-size:70px">🎾</div></div>
<div class="p" style="margin-top:40px;opacity:.85">Queres representar o TomarPadel? Desliza e fica a saber tudo.</div></div>''',photo=f'{A}assets/fotos-out2026/foto-08.jpg',pos='50% 55%',n=1)
P['2-pre-inscricao']=page(f'''<div class="c" style="top:400px"><div class="sr" style="font-size:96px;line-height:1">Como fazer a</div><div class="tt" style="font-size:92px;white-space:nowrap">pré-inscrição</div>
<div class="p" style="margin-top:60px">As pré-inscrições estão abertas até <b>31 de dezembro de 2026</b>. Entra no grupo de pré-inscrição da tua categoria:</div>
<div style="display:flex;gap:20px;margin-top:44px"><div class="chip" style="font-size:46px;padding:22px 52px">Masculino</div><div class="chip" style="font-size:46px;padding:22px 52px">Feminino</div></div>
<div class="card" style="margin-top:70px"><div class="p"><b>Não precisas de mais nada nesta fase!</b> Basta demonstrares o teu interesse e juntares-te ao grupo.</div></div>
<div class="row" style="margin-top:70px"><div class="num">✓</div><div class="p">Até <b>15 de janeiro de 2027</b> os treinadores do clube fazem a seleção e avaliação dos atletas para formar as equipas.</div></div></div>''',n=2)
P['3-quota']=page(f'''<div class="c" style="top:400px"><div class="sr" style="font-size:96px;line-height:1">Condições de</div><div class="tt" style="font-size:98px">participação</div>
<div class="card" style="margin-top:46px;display:flex;align-items:center;gap:40px;padding:34px 40px"><div><div class="kick" style="font-size:24px">Quota única</div><div class="tt" style="font-size:130px;margin-top:8px">60€</div></div><div class="p" style="border-left:2px solid rgba(255,255,255,.18);padding-left:40px">Pagamento único, com acesso a um conjunto de <b>vantagens exclusivas</b>.</div></div>
<div class="p" style="margin-top:34px;font-size:30px;opacity:.75;line-height:1.4">* O valor pode ser ajustado consoante o custo dos equipamentos e será usado na totalidade para a compra do equipamento da Liga de Clubes.</div><div class="kick" style="margin-top:70px;font-size:24px"><span class="lime"></span>Datas a reter</div><div style="margin-top:14px"><div style="display:flex;gap:28px;align-items:center;padding:12px 0;border-bottom:2px solid rgba(255,255,255,.1)"><div style="flex:0 0 220px;font-weight:900;font-size:38px;color:#5fd0f5">31 dez</div><div class="p" style="font-size:36px">Fim das pré-inscrições</div></div><div style="display:flex;gap:28px;align-items:center;padding:12px 0;border-bottom:2px solid rgba(255,255,255,.1)"><div style="flex:0 0 220px;font-weight:900;font-size:38px;color:#5fd0f5">15 jan</div><div class="p" style="font-size:36px">Seleção dos atletas</div></div><div style="display:flex;gap:28px;align-items:center;padding:12px 0;border-bottom:2px solid rgba(255,255,255,.1)"><div style="flex:0 0 220px;font-weight:900;font-size:38px;color:#5fd0f5">15 a 30 jan</div><div class="p" style="font-size:36px">Formação das equipas</div></div><div style="display:flex;gap:28px;align-items:center;padding:12px 0;border-bottom:2px solid rgba(255,255,255,.1)"><div style="flex:0 0 220px;font-weight:900;font-size:38px;color:#5fd0f5">10 fev</div><div class="p" style="font-size:36px">Prazo de pagamento da quota</div></div><div style="display:flex;gap:28px;align-items:center;padding:12px 0;border-bottom:2px solid rgba(255,255,255,.1)"><div style="flex:0 0 220px;font-weight:900;font-size:38px;color:#5fd0f5">1 mar</div><div class="p" style="font-size:36px">Início das vantagens</div></div></div></div>''',n=3)
V=[('Jogos a preço especial','Cada jogo de 1h30 custa apenas <b>5€ por jogador</b>, de 1 de março de 2027 até ao fim da participação da equipa.'),
('Equipamento oficial','Fornecido pelo clube.'),('Treino mensal de equipa','2 horas por mês.'),('Água nos jogos em casa','Oferta do clube.'),
('Apoio logístico','Bolas e campos para os eventos da Liga de Clubes.'),('8 t-shirts de treino extra','Para as equipas apuradas para as fases Regional e Nacional.')]
items=''.join(f'<div class="row" style="margin-top:44px"><div class="num">{i+1}</div><div><div style="font-weight:800;font-size:42px;line-height:1.15">{t}</div><div class="p" style="font-size:33px;opacity:.85;margin-top:6px;line-height:1.35">{d}</div></div></div>' for i,(t,d) in enumerate(V))
P['4-vantagens']=page(f'''<div class="c" style="top:390px"><div class="sr" style="font-size:96px;line-height:1">As tuas</div><div class="tt" style="font-size:130px">vantagens</div><div style="margin-top:20px">{items}</div></div>''',n=4)
K=[('Pagamento da quota até <b>10 de fevereiro de 2027</b>.','Fora do prazo, o jogador não é inscrito na equipa nem tem acesso às vantagens.'),
('Equipas formadas pelos treinadores entre <b>15 e 30 de janeiro de 2027</b>.',''),
('Treinos ao <b>fim de semana</b>, com dias e horários definidos pelo treinador de cada equipa.',''),
('As vantagens vigoram de <b>1 de março de 2027</b> até ao fim da participação na Liga.','')]
ki=''.join(f'<div class="row" style="margin-top:48px"><div class="num">{i+1}</div><div><div class="p" style="font-size:38px">{a}</div>'+(f'<div class="p" style="font-size:32px;opacity:.75;margin-top:8px">{b}</div>' if b else '')+'</div></div>' for i,(a,b) in enumerate(K))
P['5-importante']=page(f'''<div class="c" style="top:390px"><div class="sr" style="font-size:96px;line-height:1">Informação</div><div class="tt" style="font-size:112px">importante</div><div style="margin-top:14px">{ki}</div>
<div class="card" style="margin-top:70px"><div class="kick" style="font-size:24px"><span class="lime"></span>Treinadores responsáveis</div><div style="display:flex;justify-content:space-between;margin-top:22px;font-weight:800;font-size:38px"><span>Luís Coelho</span><span>Ricardo Santos</span><span>João Farinha</span></div></div></div>''',n=5)
from playwright.sync_api import sync_playwright
import os
os.makedirs('out',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,h in P.items():
        open('t.html','w').write(h);pg.goto('file:///home/claude/liga/t.html');pg.wait_for_timeout(500);pg.screenshot(path=f'out/liga-{n}.png')
    b.close()
from PIL import Image
fs=sorted(os.listdir('out'));S=Image.new('RGB',(5*432+40,768),'white')
for i,f in enumerate(fs): S.paste(Image.open('out/'+f).resize((432,768)),(i*442,0))
S.save('sheet.png')
