import re
P='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/kit/project/'
F='file:///home/claude/bk/assets/fotos-out2026/'
PAR='file:///home/claude/bk/assets/parceiros/'
AZ='/_blob/08b8550035ca2d696fd1c495792ca175'; BR='/_blob/dc6f42a16820c4982ce97f828280ea49'
LOGO_AZ='/_blob/2428388fcfd39d59989393ee6918b890'; LOGO_BR='/_blob/0754512c9d115284b57fd1a8d5f1c5d8'
H=open('/home/claude/bk/gen/helmet.txt').read().strip()
def wrap(t,b):
    return f'''<!doctype html>
<html lang="pt-PT"><head><meta charset="utf-8"><title>{t}</title><script src="./support.js"></script></head><body><x-dc>
{H}
{b}
</x-dc><script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{ renderVals() {{ return {{}}; }} }}
</script></body></html>'''
def head(label,i=None,n=None,dark=False):
    c='#ffffff' if dark else '#15406e'; src=BR if dark else AZ
    pg=f'<div style="font-weight:800;font-size:22px">{i}/{n}</div>' if i else ''
    return f'''<div style="position:absolute;left:64px;top:56px;right:64px;display:flex;align-items:center;justify-content:space-between;color:{c}"><img src="{src}" alt="TomarPadel 2.0" style="height:72px;width:auto"><div style="display:flex;align-items:center;gap:24px"><div style="font-style:italic;font-weight:600;font-size:22px;letter-spacing:0.12em;text-transform:uppercase">{label}</div>{pg}</div></div>'''
L='<div class="ar" style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#eef3f7;color:#15406e">'
D='<div class="ar" style="position:relative;width:1080px;height:1350px;overflow:hidden;background:linear-gradient(160deg,#1b4f86 0%,#15406e 55%,#0f3157 100%);color:#ffffff">'
swipe='<div style="position:absolute;left:64px;top:1150px;display:flex;align-items:center;gap:14px;border:3px solid currentColor;border-radius:999px;padding:14px 30px;font-weight:700;font-size:28px">Desliza<svg width="28" height="28" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>'
out={}
# 1 Dicas para quem esta a comecar (claro)
n=6
s=[f'''{L}{head('Dicas',1,n)}
<div style="position:absolute;left:64px;top:230px"><div style="font-weight:900;font-stretch:62%;font-size:300px;line-height:0.8;color:#12ace3">4</div>
<div style="font-weight:900;font-stretch:108%;font-size:112px;line-height:0.92;letter-spacing:-0.03em;margin-top:10px">dicas para</div>
<div style="font-weight:900;font-stretch:108%;font-size:112px;line-height:0.92;letter-spacing:-0.03em">quem está</div>
<div class="sr" style="font-size:132px;line-height:0.95">a começar.</div></div>
<img src="/_blob/8de4c30c6f0228042767989f6724d05b" alt="" style="position:absolute;left:760px;top:760px;width:240px;height:240px">
{swipe}</div>''']
tips=[("Mexe-te com o teu parceiro","Avancem e recuem juntos, lado a lado, como se estivessem presos por uma corda. Assim não abrem buracos no meio."),
("Raquete sempre à frente","Entre pancadas, mantém a raquete à frente do peito. Ganhas tempo para reagir, sobretudo junto à rede."),
("Deixa a bola vir","Não tenhas pressa: espera que a bola saia do vidro e bate-a quando desce. O vidro dá-te tempo."),
("Na dúvida, joga ao meio","Uma bola pelo meio cria confusão entre os adversários e dá-te menos margem para errar.")]
for i,(t,txt) in enumerate(tips):
    s.append(f'''{L}{head('Dicas',i+2,n)}
<div style="position:absolute;left:64px;top:220px;font-weight:900;font-stretch:62%;font-size:340px;line-height:0.8;color:#12ace3">{i+1}</div>
<div style="position:absolute;left:64px;right:64px;top:600px;font-weight:900;font-stretch:108%;font-size:96px;line-height:0.95;letter-spacing:-0.03em">{t}</div>
<div style="position:absolute;left:64px;width:820px;top:900px;font-size:38px;line-height:1.35">{txt}</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
s.append(f'''{D}{head('Dicas',n,n,True)}
<div style="position:absolute;left:64px;top:300px"><div class="sr" style="font-size:150px;line-height:0.86;color:#12ace3">Guarda</div>
<div style="font-weight:900;font-stretch:108%;font-size:124px;line-height:0.92;letter-spacing:-0.03em">e experimenta<br>no próximo jogo.</div></div>
<div style="position:absolute;left:64px;top:840px;width:760px;font-size:38px;line-height:1.35;color:#c9d7e6">E envia a quem começou a jogar contigo.</div>
<img src="{LOGO_BR}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
for i,b in enumerate(s): out[f'L2Dicas{i+1}']=(b,f'posts/dicas/dicas-{i+1}.png')
# 2 Coisas que so quem joga padel percebe (claro)
n=6
s=[f'''{L}{head('Só quem joga',1,n)}
<div style="position:absolute;left:64px;top:230px"><div style="font-weight:900;font-stretch:108%;font-size:118px;line-height:0.92;letter-spacing:-0.03em">Coisas que</div>
<div class="sr" style="font-size:140px;line-height:0.95;color:#12ace3">só quem joga</div>
<div style="font-weight:900;font-stretch:108%;font-size:118px;line-height:0.92;letter-spacing:-0.03em">padel percebe.</div></div>
{swipe}</div>''']
coisas=[("Marcar campo às 23h","e chamar-lhe «jogo rápido»."),("Perder dois jogos","e achar que o problema é a raquete."),("Dizer «última bola»","três vezes seguidas."),("Acabar o jogo","e analisar cada ponto no bar.")]
for i,(a,b) in enumerate(coisas):
    s.append(f'''{L}{head('Só quem joga',i+2,n)}
<div style="position:absolute;left:64px;top:220px;font-weight:900;font-stretch:62%;font-size:220px;line-height:0.8;color:#12ace3">0{i+1}</div>
<div style="position:absolute;left:64px;right:64px;top:560px"><div style="font-weight:900;font-stretch:108%;font-size:104px;line-height:0.95;letter-spacing:-0.03em">{a}</div><div class="sr" style="font-size:96px;line-height:1.05;margin-top:12px">{b}</div></div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
s.append(f'''{D}{head('Só quem joga',n,n,True)}
<div style="position:absolute;left:64px;top:300px"><div class="sr" style="font-size:150px;line-height:0.86;color:#12ace3">E tu,</div>
<div style="font-weight:900;font-stretch:108%;font-size:124px;line-height:0.92;letter-spacing:-0.03em">qual é a<br>tua?</div></div>
<div style="position:absolute;left:64px;top:820px;width:760px;font-size:38px;line-height:1.35;color:#c9d7e6">Conta nos comentários. Nós não julgamos 😅</div>
<img src="{LOGO_BR}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
for i,b in enumerate(s): out[f'L2Coisas{i+1}']=(b,f'posts/coisas/coisas-{i+1}.png')
# 3 Que raquete e para ti (escuro)
n=5
s=[f'''<div class="ar" style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#0f3157;color:#ffffff">
<img src="{F}foto-11.jpg" alt="Parede de raquetes na loja do TomarPadel" style="position:absolute;left:0;top:0;width:1080px;height:1350px;object-fit:cover;object-position:50% 30%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,49,87,0.55) 0%,rgba(15,49,87,0.2) 35%,rgba(15,49,87,0.92) 70%,#0f3157 100%)"></div>
{head('Dicas',1,n,True)}
<div style="position:absolute;left:64px;top:820px"><div class="sr" style="font-size:130px;line-height:0.9;color:#12ace3">Que raquete</div><div style="font-weight:900;font-stretch:108%;font-size:124px;line-height:0.92;letter-spacing:-0.03em">é para ti?</div></div>
<div style="position:absolute;left:64px;top:1150px;display:flex;align-items:center;gap:14px;border:3px solid #ffffff;border-radius:999px;padding:14px 30px;font-weight:700;font-size:28px">Desliza<svg width="28" height="28" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></div></div>''']
shapes={'Redonda':'<path d="M150 20 C230 20 270 90 270 160 C270 240 210 300 150 300 C90 300 30 240 30 160 C30 90 70 20 150 20Z"/>',
'Lágrima':'<path d="M150 14 C225 14 268 70 268 140 C268 220 205 300 150 300 C95 300 32 220 32 140 C32 70 75 14 150 14Z"/>',
'Diamante':'<path d="M150 10 C200 10 260 60 268 110 C272 150 230 240 150 300 C70 240 28 150 32 110 C40 60 100 10 150 10Z"/>'}
info=[('Redonda','Mais controlo','O ponto doce é maior e perdoa mais os erros. Ideal para quem está a começar.'),
('Lágrima','Equilíbrio','Meio-termo entre controlo e potência. Para quem já joga com regularidade.'),
('Diamante','Mais potência','Bate mais forte, mas com menos margem de erro. Para jogadores avançados e atacantes.')]
for i,(nm,sub,txt) in enumerate(info):
    s.append(f'''{D}{head('Dicas',i+2,n,True)}
<svg width="300" height="420" viewBox="0 0 300 420" aria-hidden="true" style="position:absolute;right:90px;top:200px"><g fill="none" stroke="#ffffff" stroke-width="10">{shapes[nm]}</g><rect x="138" y="300" width="24" height="110" rx="10" fill="#12ace3"/><g fill="#12ace3" opacity="0.8"><circle cx="120" cy="150" r="9"/><circle cx="150" cy="150" r="9"/><circle cx="180" cy="150" r="9"/><circle cx="135" cy="185" r="9"/><circle cx="165" cy="185" r="9"/><circle cx="150" cy="115" r="9"/></g></svg>
<div style="position:absolute;left:64px;top:240px;font-style:italic;font-weight:600;font-size:26px;letter-spacing:0.14em;text-transform:uppercase;color:#bfd84a">{sub}</div>
<div style="position:absolute;left:64px;right:64px;top:700px;font-weight:900;font-stretch:108%;font-size:130px;line-height:0.92;letter-spacing:-0.03em">{nm}</div>
<div style="position:absolute;left:64px;width:820px;top:880px;font-size:38px;line-height:1.35;color:#c9d7e6">{txt}</div>
<img src="{LOGO_BR}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
s.append(f'''{L}{head('Dicas',n,n)}
<div style="position:absolute;left:64px;top:300px"><div class="sr" style="font-size:150px;line-height:0.86;color:#12ace3">Ainda</div><div style="font-weight:900;font-stretch:108%;font-size:124px;line-height:0.92;letter-spacing:-0.03em">na dúvida?</div></div>
<div style="position:absolute;left:64px;top:700px;width:820px;font-size:40px;line-height:1.35">Experimenta antes de comprar: alugamos raquetes no balcão por 1€. E passa pela nossa loja.</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
for i,b in enumerate(s): out[f'L2Raquete{i+1}']=(b,f'posts/raquete/raquete-{i+1}.png')
# 4 Conhece a nossa casa (claro, fotos)
n=5
fotos=[('foto-16.jpg','50% 50%','Os campos','Cobertos, para jogar faça chuva ou faça sol.'),('foto-05.jpg','50% 55%','O bar','Para o terceiro set e para ver os jogos.'),('foto-11.jpg','50% 40%','A loja','Raquetes, roupa e tudo o que precisas para jogar.'),('foto-14.jpg','50% 60%','Ping-pong','Para quem está à espera da sua vez.')]
s=[f'''{L}{head('O clube',1,n)}
<div style="position:absolute;left:64px;top:200px"><div class="sr" style="font-size:130px;line-height:0.9;color:#12ace3">Conhece</div><div style="font-weight:900;font-stretch:108%;font-size:118px;line-height:0.92;letter-spacing:-0.03em">a nossa casa.</div></div>
<div style="position:absolute;left:64px;right:64px;top:520px;height:580px;border-radius:32px;overflow:hidden"><img src="{F}foto-02.jpg" alt="Fachada do TomarPadel" style="width:100%;height:100%;object-fit:cover;object-position:50% 70%"></div>
{swipe}</div>''']
for i,(f,pos,t,txt) in enumerate(fotos):
    s.append(f'''{L}{head('O clube',i+2,n)}
<div style="position:absolute;left:64px;right:64px;top:170px;height:820px;border-radius:32px;overflow:hidden"><img src="{F}{f}" alt="{t}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>
<div style="position:absolute;left:64px;right:64px;top:1030px;display:flex;align-items:baseline;gap:22px"><div style="font-weight:900;font-stretch:108%;font-size:78px;line-height:1;letter-spacing:-0.03em;white-space:nowrap">{t}</div></div>
<div style="position:absolute;left:64px;width:900px;top:1125px;font-size:32px;line-height:1.35">{txt}</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;right:64px;top:1240px;width:200px;height:auto"></div>''')
for i,b in enumerate(s): out[f'L2Clube{i+1}']=(b,f'posts/clube/clube-{i+1}.png')
# 5 Meme 2 (escuro)
out['L2Meme2']=(f'''{D}{head('Verdades do padel',None,None,True)}
<div style="position:absolute;left:64px;top:240px"><div style="font-weight:900;font-stretch:108%;font-size:118px;line-height:0.92;letter-spacing:-0.03em">Não existe<br>bola perdida.</div>
<div class="sr" style="font-size:118px;line-height:0.95;color:#12ace3;margin-top:24px">Existe parceiro<br>mal colocado.</div></div>
<div style="position:absolute;left:64px;top:930px;width:700px;font-size:34px;line-height:1.35;color:#c9d7e6">Envia ao teu parceiro. Ele sabe o que fez.</div>
<img src="{LOGO_BR}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''','posts/meme-parceiro.png')
# 6 Carlsberg (claro)
out['L2Carlsberg']=(f'''{L}{head('Parceiros')}
<div style="position:absolute;left:64px;top:220px"><div class="sr" style="font-size:150px;line-height:0.86;color:#12ace3">Obrigado,</div><div style="font-weight:900;font-stretch:108%;font-size:118px;line-height:0.92;letter-spacing:-0.03em">Carlsberg.</div></div>
<div style="position:absolute;left:64px;top:520px;width:460px;height:560px;border-radius:32px;overflow:hidden"><img src="{F}foto-19.jpg" alt="Torneira de Carlsberg no bar do TomarPadel" style="width:100%;height:100%;object-fit:cover;object-position:35% 40%"></div>
<div style="position:absolute;left:556px;right:64px;top:520px;height:560px;background:#ffffff;border-radius:32px;box-shadow:0 20px 50px rgba(21,64,110,0.12);display:flex;align-items:center;justify-content:center"><img src="{PAR}carlsberg.png" alt="Carlsberg" style="width:360px;height:auto"></div>
<div style="position:absolute;left:64px;top:1110px;width:900px;font-size:32px;line-height:1.35">Connosco em cada jogo e em cada terceiro set.</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''','posts/parceiro-carlsberg.png')
# 7 Mini 14 escuro
m=open(P+'MiniPost14.dc.html').read()
body=m[m.index('</helmet>')+9:m.index('</x-dc>')]
body=body.replace('background:#eef3f7;color:#15406e','background:#15406e;color:#ffffff',1)
body=body.replace('linear-gradient(180deg,#eef3f700 0%,#eef3f7 100%)','linear-gradient(180deg,#15406e00 0%,#15406e 100%)')
body=body.replace('border:3px solid #15406e','border:3px solid #ffffff').replace('background:#15406e;color:#ffffff;border-radius:999px;padding:9px 20px','background:#ffffff;color:#15406e;border-radius:999px;padding:9px 20px')
body=body.replace('border:2px solid #15406e','border:2px solid #ffffff').replace('rgba(21,64,110,0.2)','rgba(255,255,255,0.25)')
body=body.replace('/_blob/2428388fcfd39d59989393ee6918b890','/_blob/0754512c9d115284b57fd1a8d5f1c5d8')
out['L2Mini14Dark']=(body,'mini-torneios/mini-torneio-14nov-post-escuro.png')
jobs=[]
for k,(b,o) in out.items():
    open(P+k+'.dc.html','w').write(wrap(k,b)); jobs.append(f'{k}.dc.html {o} 1080 1350')
open('/home/claude/bk/gen/j_lote2.txt','w').write('\n'.join(jobs)+'\n')
print(len(jobs))
