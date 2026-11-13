src=open('/home/claude/bk/gen/lote2.py').read()
exec(src[:src.index('out={}')])
import re
out={}
def endslide(n,label,big1,big2,sub,dark=True):
    root=D if dark else L
    logo=LOGO_BR if dark else LOGO_AZ
    c='#c9d7e6' if dark else '#15406e'
    return f'''{root}{head(label,n,n,dark)}
<div style="position:absolute;left:64px;top:300px"><div class="sr" style="font-size:150px;line-height:0.86;color:#12ace3">{big1}</div>
<div style="font-weight:900;font-stretch:108%;font-size:124px;line-height:0.92;letter-spacing:-0.03em">{big2}</div></div>
<div style="position:absolute;left:64px;top:840px;width:780px;font-size:38px;line-height:1.35;color:{c}">{sub}</div>
<img src="{logo}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>'''
# 1 Comunidade fotos (escuro)
n=6
fot=[('foto-16.jpg','50% 55%','Isto é o','TomarPadel.'),('foto-07.jpg','50% 45%','Jogos','a qualquer hora.'),('foto-10.jpg','50% 35%','Smashes','que ficam na memória.'),('foto-13.jpg','50% 45%','Duplas','que se tornam amizades.'),('foto-15.jpg','30% 50%','E entre jogos,','ping-pong.')]
s=[]
for i,(f,pos,a,b) in enumerate(fot):
    s.append(f'''<div class="ar" style="position:relative;width:1080px;height:1350px;overflow:hidden;background:#0f3157;color:#ffffff">
<img src="{F}{f}" alt="" style="position:absolute;left:0;top:0;width:1080px;height:1350px;object-fit:cover;object-position:{pos}">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,49,87,0.55) 0%,rgba(15,49,87,0) 25%,rgba(15,49,87,0) 55%,rgba(15,49,87,0.92) 82%,#0f3157 100%)"></div>
{head('Comunidade',i+1,n,True)}
<div style="position:absolute;left:64px;top:{960 if i else 900}px"><div class="sr" style="font-size:{110 if i else 130}px;line-height:0.9;color:#12ace3">{a}</div><div style="font-weight:900;font-stretch:108%;font-size:{96 if i else 124}px;line-height:0.95;letter-spacing:-0.03em">{b}</div></div>
{'' if i else '<div style="position:absolute;right:64px;top:1180px;display:flex;align-items:center;gap:14px;border:3px solid #ffffff;border-radius:999px;padding:14px 30px;font-weight:700;font-size:28px">Desliza<svg width="28" height="28" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>'}
</div>''')
s.append(endslide(n,'Comunidade','Vem','fazer parte.','Reserva o teu campo na app TiePlayer.',True))
for i,b in enumerate(s): out[f'L3Com{i+1}']=(b,f'posts/comunidade-fotos/comunidade-fotos-{i+1}.png')
# 2 Aquecimento (claro)
n=6
s=[f'''{L}{head('Dicas',1,n)}
<div style="position:absolute;left:64px;top:230px"><div style="font-weight:900;font-stretch:62%;font-size:300px;line-height:0.8;color:#12ace3">5'</div>
<div style="font-weight:900;font-stretch:108%;font-size:112px;line-height:0.92;letter-spacing:-0.03em;margin-top:10px">de aquecimento</div>
<div class="sr" style="font-size:132px;line-height:0.95">que fazem</div>
<div style="font-weight:900;font-stretch:108%;font-size:112px;line-height:0.92;letter-spacing:-0.03em">a diferença.</div></div>
{swipe}</div>''']
tips=[("Mobiliza as articulações","Círculos com os ombros, pulsos, ancas e tornozelos. Um minuto chega para acordar o corpo."),
("Ativa as pernas","Pequenos saltos e deslocamentos laterais de um lado ao outro do campo, como se estivesses a jogar."),
("Começa devagar","Troca bolas suaves do fundo do campo. Nada de smashes nos primeiros minutos."),
("Aquece o ombro","Faz uns voleios curtos junto à rede antes das bandejas e dos remates.")]
for i,(t,txt) in enumerate(tips):
    s.append(f'''{L}{head('Dicas',i+2,n)}
<div style="position:absolute;left:64px;top:220px;font-weight:900;font-stretch:62%;font-size:340px;line-height:0.8;color:#12ace3">{i+1}</div>
<div style="position:absolute;left:64px;right:64px;top:600px;font-weight:900;font-stretch:108%;font-size:96px;line-height:0.95;letter-spacing:-0.03em">{t}</div>
<div style="position:absolute;left:64px;width:820px;top:900px;font-size:38px;line-height:1.35">{txt}</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
s.append(endslide(n,'Dicas','Menos lesões,','melhor jogo.','Guarda e faz antes do próximo jogo.',True))
for i,b in enumerate(s): out[f'L3Aq{i+1}']=(b,f'posts/aquecimento/aquecimento-{i+1}.png')
# 3 Natal faltam 10 dias (vermelho)
nat=open(P+'NatalUltimos.dc.html').read()
body=nat[nat.index('</helmet>')+9:nat.index('</x-dc>')] if '</helmet>' in nat else None
if body is None:
    body=nat[nat.index('<div class="ar"'):nat.rindex('</x-dc>')]
body=body.replace('>Últimos<','>Faltam<').replace('>Dias<','>10 dias<').replace('font-size:250px;line-height:0.82','font-size:200px;line-height:0.82')
body=body.replace('>Inscrições até<','>Grupo de WhatsApp<').replace('>14 Nov<','>25 Nov<')
body=body.replace('Equipas de 4 elementos. Mistos e Masculinos, Iniciante e Avançado.','Calendário de jogos publicado a 30 de novembro.')
out['L3Natal10']=(body,'torneios/natal-faltam-10.png')
# 4 Bingo (claro)
cells=['Pedi desculpa<br>5 vezes','A bola bateu<br>na grade','Ouvi «tua!»<br>e ninguém foi','Smash<br>para fora','«Última bola»<br>3 vezes','Imperial<br>no fim','Discussão:<br>foi rede?','Raquete nova,<br>mesmo nível','Gritei<br>«VAMOS!»']
g=''.join(f'<div style="background:{"#15406e" if i==4 else "#ffffff"};color:{"#ffffff" if i==4 else "#15406e"};border-radius:22px;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:30px;line-height:1.15;padding:10px;box-shadow:0 10px 24px rgba(21,64,110,0.08)">{c}</div>' for i,c in enumerate(cells))
out['L3Bingo']=(f'''{L}{head('Humor')}
<div style="position:absolute;left:64px;top:190px"><div style="font-weight:900;font-stretch:108%;font-size:110px;line-height:0.92;letter-spacing:-0.03em">Bingo</div><div class="sr" style="font-size:110px;line-height:0.95;color:#12ace3">do padel.</div></div>
<div style="position:absolute;left:64px;right:64px;top:440px;height:700px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:16px">{g}</div>
<div style="position:absolute;left:64px;top:1180px;font-size:32px;line-height:1.3;font-weight:700">Quantas fizeste no último jogo?</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;right:64px;top:1250px;width:200px;height:auto"></div>''','posts/bingo-padel.png')
# 5 Campo Jovem (claro)
out['L3CampoJovem']=(f'''{L}{head('Parceiros')}
<div style="position:absolute;left:64px;top:220px"><div class="sr" style="font-size:150px;line-height:0.86;color:#12ace3">Obrigado,</div><div style="font-weight:900;font-stretch:108%;font-size:118px;line-height:0.92;letter-spacing:-0.03em">Campo Jovem.</div></div>
<div style="position:absolute;left:64px;top:520px;width:460px;height:560px;border-radius:32px;overflow:hidden"><img src="{F}foto-08.jpg" alt="Campo com o logo Campo Jovem no vidro" style="width:100%;height:100%;object-fit:cover;object-position:65% 75%"></div>
<div style="position:absolute;left:556px;right:64px;top:520px;height:560px;background:#ffffff;border-radius:32px;box-shadow:0 20px 50px rgba(21,64,110,0.12);display:flex;align-items:center;justify-content:center"><img src="{PAR}campo-jovem-preto.jpg" alt="Campo Jovem" style="width:340px;height:auto;mix-blend-mode:multiply"></div>
<div style="position:absolute;left:64px;top:1110px;width:900px;font-size:32px;line-height:1.35">Presentes nos nossos campos e no padel de Tomar.</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''','posts/parceiro-campo-jovem.png')
# 6 Erros na rede (escuro)
n=5
s=[f'''{D}{head('Dicas',1,n,True)}
<div style="position:absolute;left:64px;top:230px"><div style="font-weight:900;font-stretch:62%;font-size:300px;line-height:0.8;color:#12ace3">3</div>
<div style="font-weight:900;font-stretch:108%;font-size:112px;line-height:0.92;letter-spacing:-0.03em;margin-top:10px">erros na rede</div>
<div class="sr" style="font-size:132px;line-height:0.95">que todos</div>
<div style="font-weight:900;font-stretch:108%;font-size:112px;line-height:0.92;letter-spacing:-0.03em">cometemos.</div></div>
<div style="position:absolute;left:64px;top:1150px;display:flex;align-items:center;gap:14px;border:3px solid #ffffff;border-radius:999px;padding:14px 30px;font-weight:700;font-size:28px">Desliza<svg width="28" height="28" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></div></div>''']
er=[("Ficar colado à rede","Fica a cerca de 2 metros. Chegas aos voleios e ainda tens tempo para recuar se vier um lob."),
("Bater forte em vez de colocar","Na rede ganha quem coloca. Um voleio aos pés do adversário vale mais do que um remate contra o vidro."),
("Ficar parado depois do voleio","Volta logo à posição, com a raquete à frente. A próxima bola já vem a caminho.")]
for i,(t,txt) in enumerate(er):
    s.append(f'''{D}{head('Dicas',i+2,n,True)}
<div style="position:absolute;left:64px;top:220px;font-weight:900;font-stretch:62%;font-size:340px;line-height:0.8;color:#12ace3">{i+1}</div>
<div style="position:absolute;left:64px;right:64px;top:600px;font-weight:900;font-stretch:108%;font-size:96px;line-height:0.95;letter-spacing:-0.03em">{t}</div>
<div style="position:absolute;left:64px;width:820px;top:900px;font-size:38px;line-height:1.35;color:#c9d7e6">{txt}</div>
<img src="{LOGO_BR}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''')
s.append(endslide(n,'Dicas','Guarda','e envia ao teu<br>parceiro de rede.','Para o próximo jogo correr melhor aos dois.',False))
for i,b in enumerate(s): out[f'L3Rede{i+1}']=(b,f'posts/rede/rede-{i+1}.png')
# 7 Meme Natal (escuro)
out['L3MemeNatal']=(f'''{D}{head('Verdades do padel',None,None,True)}
<div style="position:absolute;left:64px;top:240px"><div style="font-weight:900;font-stretch:108%;font-size:112px;line-height:0.92;letter-spacing:-0.03em">No Natal,<br>o teu parceiro<br>dá-te uma prenda.</div>
<div class="sr" style="font-size:124px;line-height:0.95;color:#12ace3;margin-top:28px">Em vez de<br>culpas.</div></div>
<div style="position:absolute;left:64px;top:1010px;width:700px;font-size:34px;line-height:1.35;color:#c9d7e6">Pelo menos durante o torneio.</div>
<img src="{LOGO_BR}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''','posts/meme-natal.png')
# 8 Quinta da Cacabrava (claro)
out['L3Cacabrava']=(f'''{L}{head('Parceiros')}
<div style="position:absolute;left:64px;top:220px"><div class="sr" style="font-size:150px;line-height:0.86;color:#12ace3">Obrigado,</div><div style="font-weight:900;font-stretch:108%;font-size:104px;line-height:0.92;letter-spacing:-0.03em">Quinta da<br>Caçabrava.</div></div>
<div style="position:absolute;left:64px;right:64px;top:600px;height:480px;background:#ffffff;border-radius:32px;box-shadow:0 20px 50px rgba(21,64,110,0.12);display:flex;align-items:center;justify-content:center"><img src="{PAR}quinta-cacabrava.webp" alt="Quinta da Caçabrava" style="width:640px;height:auto"></div>
<div style="position:absolute;left:64px;top:1110px;width:900px;font-size:32px;line-height:1.35">Obrigado pelo apoio ao TomarPadel e ao padel em Tomar.</div>
<img src="{LOGO_AZ}" alt="TomarPadel" style="position:absolute;left:64px;top:1230px;width:230px;height:auto"></div>''','posts/parceiro-cacabrava.png')
jobs=[]
for k,(b,o) in out.items():
    open(P+k+'.dc.html','w').write(wrap(k,b)); jobs.append(f'{k}.dc.html {o} 1080 1350')
open('/home/claude/bk/gen/j_lote3.txt','w').write('\n'.join(jobs)+'\n')
print(len(jobs))
