import json,datetime as dt,html
OUT='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/plano/'
NOW='2026-11-15T12:05'
P=json.load(open('gen/plano.json'));S=json.load(open('gen/stories.json'))
ev={}
def add(d,x): ev.setdefault(d,[]).append(x)
def st(a,kind):
    if a<NOW: return 'pub'
    if a<'2026-11-21T12': return 'ok'
    if kind=='post' or a>='2026-12': return 'new'
    return 'wait'
for i,p in enumerate(P):
    add(p['dueAt'][:10],dict(k='post',t=p['title'],h=p['dueAt'][11:16],img=f'img/{i+1:02d}.jpg',s=st(p['dueAt'],'post')))
add('2026-11-10',dict(k='post',t='Aviso: clube fechado (tempestade)',h='',img='img/ex_tempestade.jpg',s='pub'))
for s in S:
    a=s['dueAt'];add(a[:10],dict(k='story',t=s['title'],h=a[11:16],img='img/st/'+s['img'].split('/')[-1].replace('.png','.jpg'),s=st(a,'story')))
MES=['','Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
DS=['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']
d=dt.date(2026,10,19);end=dt.date(2026,12,6);today=dt.date(2026,11,15)
rows=''
while d<=end:
    wk=''
    for j in range(7):
        x=d+dt.timedelta(j);k=x.isoformat();E=sorted(ev.get(k,[]),key=lambda e:(e['k']!='post',e['h']))
        cls='day'+(' today' if x==today else '')+('' if E else ' empty')+(' past' if x<today else '')
        lab=f'<div class="dl"><span class="dw">{DS[j]}</span> {x.day} {MES[x.month] if (x.day==1 or j==0) else ""}</div>'
        body=''
        for e in E:
            t=html.escape(e['t'])
            if e['k']=='post': body+=f'<div class="cp {e["s"]}" title="{t}"><img src="{e["img"]}" alt="{t}" loading="lazy"><span class="ch">{e["h"]}</span></div>'
        sts=''.join(f'<div class="cs {e["s"]}" title="{html.escape(e["t"])} · {e["h"]}"><img src="{e["img"]}" alt="{html.escape(e["t"])}" loading="lazy"></div>' for e in E if e['k']=='story')
        if sts: body+=f'<div class="csr">{sts}</div>'
        names=''.join(f'<div class="cn">{"Story · " if e["k"]=="story" else ""}{html.escape(e["t"])}</div>' for e in E)
        wk+=f'<div class="{cls}">{lab}{body}<div class="cnames">{names}</div></div>'
    rows+=wk;d+=dt.timedelta(7)
css='''<style>
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px;margin-bottom:12px}
.ch7{font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);padding:0 4px}
.day{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:6px;min-height:92px;min-width:0}
.day.empty{background:transparent}.day.past{opacity:.78}
.day.today{outline:2.5px solid var(--acc);outline-offset:-1px;opacity:1}
.dl{font-size:11.5px;font-weight:800;margin-bottom:5px}.dw{display:none}
.cp{position:relative;border-radius:8px;overflow:hidden;border:3px solid transparent}
.cp img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover}
.ch{position:absolute;left:4px;bottom:4px;background:rgba(0,0,0,.65);color:#fff;font-size:10px;font-weight:700;border-radius:999px;padding:1px 6px}
.csr{display:flex;gap:4px;margin-top:5px;flex-wrap:wrap}
.cs{width:26px;border-radius:5px;overflow:hidden;border:2px solid transparent}.cs img{display:block;width:100%;aspect-ratio:9/16;object-fit:cover}
.pub{border-color:#15406e}.ok{border-color:#9fbf1f}.wait{border-color:#9db3cc;border-style:dashed}.new{border-color:#c8102e}
.cnames{display:none}
.leg{display:flex;flex-wrap:wrap;gap:14px;font-size:13px;color:var(--mute);margin:0 0 14px}.leg i{display:inline-block;width:14px;height:14px;border-radius:4px;border:3px solid;vertical-align:-2px;margin-right:6px}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .pub{border-color:#eaf2fb}}
@media (max-width:720px){.cal{grid-template-columns:1fr}.ch7,.day.empty{display:none}.day{display:grid;grid-template-columns:64px 72px 1fr;gap:10px;align-items:start;min-height:0}
.dw{display:block;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}.dl{font-size:15px}
.cp{grid-column:2}.csr{grid-column:2;margin-top:0}.cnames{display:block;grid-column:3;grid-row:1/span 3;font-size:13px}.cn{margin-bottom:4px}}
</style>'''
sec=css+'''<h2>Calendário</h2><p class="sub">Posts e stories dia a dia, de 19 Out a 6 Dez. Hoje está assinalado a azul. Passa o rato (ou toca) numa imagem para ver o título.</p>
<div class="leg"><span><i style="border-color:#15406e"></i>Publicado</span><span><i style="border-color:#9fbf1f"></i>Agendado no Buffer</span><span><i style="border-color:#9db3cc;border-style:dashed"></i>Aprovado, a agendar</span><span><i style="border-color:#c8102e"></i>Lote 3, por aprovar</span><span>Miniaturas pequenas: stories</span></div>
<div class="cal">'''+''.join(f'<div class="ch7">{x}</div>' for x in DS)+rows+'</div><div style="height:28px"></div>'
h=open(OUT+'plano.html').read()
anchor='<h2>O que aprendemos com outros clubes</h2>'
assert anchor in h
h=h.replace(anchor,sec+anchor,1)
open(OUT+'plano.html','w').write(h)
