import os
import json,html
exec(open('gen/items.py').read())
C={}
for s in SECTIONS: C.update(s[4])
T2="#TomarPadel #Padel #Tomar #BarTomarPadel"
C['bar/hamburgueres.png']=f"""Depois do jogo, há hambúrguer 🍔

Menu completo com hambúrguer, batata frita e bebida, a 7,5€:
• Menu 30/0: porco e vaca 130g
• Menu 15/40: peru 130g
• Menu 40/0: especial com farinheira 130g

Extra: hambúrguer 130g por 2€

Pede no bar do TomarPadel 💙

{T2}"""
C['bar/pizzas.png']=f"""Jogo feito, pizza merecida 🍕

Pizza + bebida a 7,5€:
• Bandeja de Atum e Bacon
• Smash à Carbonara
• Víbora Romana
• Chiquita Havaina

Qual é a tua jogada preferida? 👇

{T2}"""
C['bar/tostas.png']=f"""Fome entre jogos? Temos tostas 🥪

Tosta + batata frita + bebida a 5,5€:
• Dupla Perfeita: pão rústico, queijo e fiambre
• Top Spin Ibérico: pão rústico, queijo e presunto

Pede no bar do TomarPadel 💙

{T2}"""
C['bar/snacks.png']=f"""Novidade no bar: Snacks 🆕

🥖 Pão com chouriço: 3€
🥚 Ovo cozido: 1€

Perfeito para um reforço rápido antes ou depois do jogo.

{T2}"""
C['posts/patrocinador.png']=f"""Obrigado a quem nos apoia 💙

A P&S Auto Color Expert é o patrocinador oficial do Torneio de Natal do TomarPadel. Pintura auto e bate-chapas com o rigor que o teu carro merece.

Obrigado pela confiança e por apostarem no padel em Tomar! 🎾

{T}"""
C['posts/regras/regras-1.png']=f"""5 regras do padel que muita gente não sabe 🎾👉

Desliza e confirma quantas já conhecias. Sê honesto 😅

Guarda este post e envia ao teu parceiro de jogo que ainda serve por cima.

#TomarPadel #Padel #RegrasDoPadel #Tomar #PadelPortugal"""
C['posts/gamecard.png']=f"""Joga mais, paga menos 🎾

Com o Gamecard tens 10 jogos por 65€.

Pede o teu no balcão do clube e garante os próximos jogos.

{T}"""
C['torneios/natal-ultimos-dias.png']="""Últimos dias para inscreveres a tua equipa no Torneio de Natal! 🏆

📅 4, 5 e 6 de dezembro
👥 Equipas de 4 elementos
🎯 Mistos e Masculinos, Iniciante e Avançado
💶 25€ por jogador (+10€ pela 2ª categoria)
🎁 Welcome pack: t-shirt, água e voucher de 1h30
🏆 Troféu de equipa e prize money para 1º e 2º lugar

Inscrições até 14 de novembro. Não fiques de fora!

Patrocinador oficial: P&S Auto Color Expert

#TomarPadel #Padel #TorneioDeNatal #Tomar #PadelPortugal"""
C['posts/parceiros/parceiros-1.png']=f"""Os 5 tipos de parceiro de padel 😂👉

Desliza e diz-nos: qual destes és tu? E qual é o teu parceiro?

Identifica-o nos comentários, ele vai perceber 😉

{T}"""
C['posts/meme-terceiro-set.png']=f"""O terceiro set joga-se no bar 🍺

Ganhar ou perder, a rodada é sagrada. Marca quem te deve a próxima 👇

{T}"""
C['posts/dicas/dicas-1.png']=f"""4 dicas para quem está a começar no padel 🎾👉

Desliza, guarda e experimenta no próximo jogo. E envia a quem começou a jogar contigo!

#TomarPadel #Padel #DicasDePadel #Tomar #PadelPortugal"""
C['posts/coisas/coisas-1.png']=f"""Coisas que só quem joga padel percebe 😂👉

Qual destas é a tua? Conta nos comentários, nós não julgamos.

{T}"""
C['posts/raquete/raquete-1.png']=f"""Redonda, lágrima ou diamante? Que raquete é para ti? 🎾👉

Desliza e descobre qual combina com o teu jogo. Ainda na dúvida? Experimenta no clube: alugamos raquetes por 1€.

#TomarPadel #Padel #DicasDePadel #Tomar #PadelPortugal"""
C['posts/clube/clube-1.png']=f"""Conhece a nossa casa 💙👉

Campos cobertos, bar, loja e até ping-pong para a espera. Anda conhecer o TomarPadel!

📍 Rua D. João I, Vale Carrito, Tomar

{T}"""
C['posts/meme-parceiro.png']=f"""Não existe bola perdida. Existe parceiro mal colocado 😅

Envia ao teu parceiro. Ele sabe o que fez 👇

{T}"""
C['posts/meme-analise.png']=f"""90 minutos de jogo. 2 horas no bar a analisá-lo 🍺🎾

Marca quem faz sempre a melhor análise pós-jogo 👇

{T}"""
C['posts/parceiro-carlsberg.png']=f"""Obrigado, Carlsberg 💚

Connosco em cada jogo e em cada terceiro set. Obrigado por apoiarem o padel em Tomar!

{T}"""
C['mini-torneios/mini-torneio-14nov-post-escuro.png']=MINI.format(d='14',c='M3+, M3 e M4+')
P=[
("2026-10-25T11:00:00+00:00","Dom 25 Out","11:00","Aprender","posts/regras/regras-1.png","Carrossel: 5 regras que muita gente não sabe","Claro, a seguir à agenda de eventos (escura)."),
("2026-10-26T18:30:00+00:00","Seg 26 Out","18:30","Clube","posts/precos-campos.png","Preços dos campos","Escuro. Serve de teste ao Facebook."),
("2026-10-27T18:30:00+00:00","Ter 27 Out","18:30","Humor","posts/parceiros/parceiros-1.png","Carrossel: 5 tipos de parceiro de padel","Claro. Sem mini-torneio nesta semana."),
("2026-10-28T18:30:00+00:00","Qua 28 Out","18:30","Clube","posts/aluguer-material.png","Aluguer de material","Escuro. Trocado com o Snacks, que fica para mais tarde."),
("2026-11-01T11:00:00+00:00","Dom 1 Nov","11:00","Promoção","calendarios/tematicas-novembro-post.png","Promoções e temáticas de novembro","Claro. Quinta 29 fica sem post para manter claro e escuro alternados."),
("2026-11-02T18:30:00+00:00","Seg 2 Nov","18:30","Humor","posts/meme-parceiro.png","Não existe bola perdida","Escuro."),
("2026-11-03T18:30:00+00:00","Ter 3 Nov","18:30","Competição","mini-torneios/mini-torneio-07nov-post.png","Mini-torneio 07 Nov","Claro. Sempre à terça antes do mini-torneio."),
("2026-11-04T18:30:00+00:00","Qua 4 Nov","18:30","Humor","posts/meme-terceiro-set.png","O terceiro set joga-se no bar","Escuro."),
("2026-11-05T18:30:00+00:00","Qui 5 Nov","18:30","Parceiros","posts/patrocinador.png","Obrigado P&S Auto Color Expert","Claro."),
("2026-11-08T11:00:00+00:00","Dom 8 Nov","11:00","Comunidade","posts/comunidade.png","Comunidade","Escuro."),
("2026-11-09T18:30:00+00:00","Seg 9 Nov","18:30","Aprender","posts/dicas/dicas-1.png","Carrossel: 4 dicas para quem está a começar","Claro."),
("2026-11-10T18:30:00+00:00","Ter 10 Nov","18:30","Competição","mini-torneios/mini-torneio-14nov-post-escuro.png","Mini-torneio 14 Nov","Escuro. Versão escura para manter a alternância."),
("2026-11-11T18:30:00+00:00","Qua 11 Nov","18:30","Humor","posts/coisas/coisas-1.png","Carrossel: coisas que só quem joga padel percebe","Claro."),
("2026-11-12T18:30:00+00:00","Qui 12 Nov","18:30","Competição","torneios/natal-ultimos-dias.png","Torneio de Natal: últimos dias","Escuro (vermelho). Inscrições até 14 Nov."),
("2026-11-15T11:00:00+00:00","Dom 15 Nov","11:00","Comunidade","posts/clube/clube-1.png","Carrossel: conhece a nossa casa","Claro. Com as tuas fotos novas."),
("2026-11-16T18:30:00+00:00","Seg 16 Nov","18:30","Aprender","posts/raquete/raquete-1.png","Carrossel: que raquete é para ti?","Escuro."),
("2026-11-17T18:30:00+00:00","Ter 17 Nov","18:30","Competição","mini-torneios/mini-torneio-21nov-post.png","Mini-torneio 21 Nov","Claro."),
("2026-11-18T18:30:00+00:00","Qua 18 Nov","18:30","Humor","posts/meme-analise.png","90 minutos de jogo, 2 horas no bar","Escuro. Novo."),
("2026-11-19T18:30:00+00:00","Qui 19 Nov","18:30","Parceiros","posts/parceiro-carlsberg.png","Obrigado, Carlsberg","Claro."),
]
S=[]
def st(d,dia,h,img,t): S.append((d,dia,h,img,t))
for d,dia in [('2026-10-26','Seg 26 Out'),('2026-11-02','Seg 2 Nov'),('2026-11-09','Seg 9 Nov'),('2026-11-16','Seg 16 Nov'),('2026-11-23','Seg 23 Nov'),('2026-11-30','Seg 30 Nov')]: st(d+'T10:00:00+00:00',dia,'10:00','stories/promo-segundas-story-v2.png','Segundas à noite')
for d,dia in [('2026-10-28','Qua 28 Out'),('2026-11-04','Qua 4 Nov'),('2026-11-11','Qua 11 Nov'),('2026-11-18','Qua 18 Nov'),('2026-11-25','Qua 25 Nov')]: st(d+'T10:00:00+00:00',dia,'10:00','stories/promo-roleta-story.png','Roleta da Sorte')
st('2026-11-01T10:00:00+00:00','Dom 1 Nov','10:00','calendarios/eventos-novembro-story.png','Agenda de eventos de novembro')
st('2026-11-01T12:00:00+00:00','Dom 1 Nov','12:00','torneios/natal-story.png','Torneio de Natal: inscrições abertas')
st('2026-11-13T19:00:00+00:00','Sex 13 Nov','19:00','torneios/natal-story.png','Torneio de Natal: inscrições fecham amanhã')
for d,dia in [('07','Sáb 7 Nov'),('14','Sáb 14 Nov'),('21','Sáb 21 Nov')]: st(f'2026-11-{d}T11:00:00+00:00',dia,'11:00',f'mini-torneios/mini-torneio-{d}nov-story.png',f'Mini-torneio {d} Nov: é hoje')
S.sort()
json.dump([dict(dueAt=a,img=d,title=e) for a,b,c,d,e in S],open('gen/stories.json','w'),ensure_ascii=False,indent=1)
json.dump([dict(dueAt=a,img=e,caption=C[e],title=f) for a,b,c,d,e,f,g in P],open('gen/plano.json','w'),ensure_ascii=False,indent=1)
from PIL import Image
OUT='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/plano/'
cards=[]
for i,(a,dia,h,pil,img,t,nota) in enumerate(P):
    fn=f"img/{i+1:02d}.jpg"; Image.open('dl/'+img).convert('RGB').resize((720,900),Image.LANCZOS).save(OUT+fn,quality=86)
    car=None
    CAR={'regras':7,'parceiros':7,'dicas':6,'coisas':6,'raquete':5,'clube':5}
    key=next((k for k in CAR if f'/{k}/' in img),None)
    if key:
        base=img.rsplit('-',1)[0]; os.makedirs(OUT+'img/c',exist_ok=True); car=[]
        for k in range(1,CAR[key]+1):
            cf=f"img/c/{base.split('/')[-1]}-{k}.jpg"; Image.open(f'dl/{base}-{k}.png').convert('RGB').resize((720,900),Image.LANCZOS).save(OUT+cf,quality=84); car.append(cf)
    if car:
        slides=''.join(f'<img src="{c}" alt="{html.escape(t)} {k+1}/{len(car)}" loading="lazy" width="720" height="900">' for k,c in enumerate(car))
        ph=f'<div class="ph car"><div class="track">{slides}</div><button class="nav prev" aria-label="Anterior">‹</button><button class="nav next" aria-label="Seguinte">›</button><div class="cnt">1/{len(car)}</div></div>'
    else:
        ph=f'<div class="ph"><img src="{fn}" alt="{html.escape(t)}" loading="lazy" width="720" height="900"></div>'
    st_='Publicado' if a<'2026-10-28T06' else ('Agendado' if a<'2026-11-05' else ('Agendo a 30 Out' if a<'2026-11-06' else 'Lote 2 · por aprovar'))
    cards.append(f'''<article class="card">{ph}<div class="badge {'pub' if a<'2026-10-28T06' else ('ok' if a<'2026-11-05' else 'wait')}">{st_}</div>
<div class="meta"><div class="when"><span class="d">{dia}</span><span class="h">{h}</span></div><span class="pill p-{pil.lower().replace('ç','c').replace('ã','a')}">{pil}</span></div>
<h3>{html.escape(t)}</h3>{f'<p class="nota">{html.escape(nota)}</p>' if nota else ''}
<details><summary>Legenda</summary><pre>{html.escape(C[img])}</pre></details></article>''')
import os
os.makedirs(OUT+'img/st',exist_ok=True)
sc=[]
for a,dia,h,img,t in S:
    fn='img/st/'+img.split('/')[-1].replace('.png','.jpg')
    if not os.path.exists(OUT+fn): Image.open('dl/'+img).convert('RGB').resize((360,640),Image.LANCZOS).save(OUT+fn,quality=84)
    sk=sum(1 for _ in sc)
    sb='Publicado' if a<'2026-10-28T06' else ('Agendado' if a<'2026-11-05' else ('Agendo a 30 Out' if a<'2026-11-08' else 'Lote 2 · por aprovar'))
    sc.append(f'<div class="sc"><div class="badge {"pub" if a<"2026-10-28T06" else ("ok" if a<"2026-11-05" else "wait")}">{sb}</div><img src="{fn}" alt="{html.escape(t)}" loading="lazy"><div class="sm"><b>{dia}</b> {h}<br>{html.escape(t)}</div></div>')
page=open('gen/plano_tpl.html').read().replace('%%CARDS%%','\n'.join(cards)).replace('%%STORIES%%','\n'.join(sc))
open(OUT+'plano.html','w').write(page)
print('ok')
