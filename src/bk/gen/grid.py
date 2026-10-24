O='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/plano/'
tiles=['img/ex_natal.jpg']+[f'img/{i:02d}.jpg' for i in range(10,0,-1)]+['img/ex_eventos.jpg','img/ex_templarios.jpg']
labels=['Fixado']+[None]*10+['Publicado','Publicado']
h='<h2 style="margin-top:36px">Como fica a grelha a 5 de novembro</h2><p class="sub">O Torneio de Natal continua fixado no topo. A seguir, claro e escuro alternados.</p><div class="igrid">'
for t,l in zip(tiles,labels): h+=f'<div class="tile"><img src="{t}" alt="" loading="lazy">{f"<span>{l}</span>" if l else ""}</div>'
h+='</div>'
s=open(O+'plano.html').read()
css='.igrid{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;max-width:520px;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}.tile{position:relative}.tile img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover}.tile span{position:absolute;left:6px;top:6px;background:rgba(0,0,0,.6);color:#fff;font-size:11px;font-weight:700;border-radius:999px;padding:2px 8px}\n.next{margin-top:36px}'
s=s.replace('.next{margin-top:36px}',css,1).replace('<h2 style="margin-top:36px">Stories',h+'\n<h2 style="margin-top:36px">Stories',1)
open(O+'plano.html','w').write(s)
