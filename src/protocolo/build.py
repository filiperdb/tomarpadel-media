R=[("Roll up","na entrada","Roll up da marca em zona de passagem do clube, junto à entrada e à loja de equipamento.","400€","+ IVA",0),
("Patrocínio","parede L","Lona de grande formato aplicada na parede do clube, visível de dentro dos campos e da zona de convívio.","500€","+ IVA",0),
("Publicidade","de campo","Nome da marca no campo e branding nos vidros. O campo passa a ser identificado pela marca nas reservas, na comunicação e nos torneios.","1500€","+ IVA",1),
("Entradas","dos campos","Branding nas entradas dos campos: o ponto por onde passa todo o jogador, em todos os jogos.","500€","+ IVA",0),
("Patrocínio","de equipas","Naming da equipa e marca no equipamento de jogo, ao longo da Liga de Clubes, dentro e fora de Tomar.","900€","+ IVA",0),
("Patrocínio","de torneio","Branding no torneio: roll ups, bandeiras e presença na comunicação do evento. Em alternativa, prémios ligados ao negócio da empresa.","750€","+ IVA ou prémios",0)]
rows=''
for a,b,d,v,iva,hl in R:
    bg='background:#15406e;color:#fff' if hl else 'background:#fff'
    tag='<div class="lab" style="color:#bfd84a;font-size:8.5px;margin-bottom:4px">Mais exposição</div>' if hl else ''
    vc='#fff' if hl else '#12ace3'
    rows+=f'''<div style="{bg};border-radius:12px;padding:22px 22px;display:grid;grid-template-columns:160px 1fr 110px;gap:18px;align-items:center">
<div>{tag}<div style="font-weight:800;font-size:14.5px;line-height:1.2">{a}<br><span class="sr" style="font-weight:400;font-size:17px">{b}</span></div></div>
<div class="body" style="font-size:12px;opacity:.85">{d}</div>
<div style="text-align:right"><div class="k" style="font-size:32px;color:{vc}">{v}</div><div style="font-size:8.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;opacity:.7;margin-top:3px">{iva}</div></div></div>\n'''
s=open('protocolo.html').read().replace('%%ROWS%%',rows)
open('out.html','w').write(s)
from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page()
    pg.goto('file://'+os.getcwd()+'/out.html');pg.wait_for_timeout(1200)
    pg.pdf(path='Protocolo_Parceiro_TomarPadel_v2.pdf',format='A4',print_background=True,prefer_css_page_size=True)
    b.close()
