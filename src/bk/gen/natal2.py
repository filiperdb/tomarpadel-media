R='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/kit/project/'
RED='#c8102e'; DK='#8e0b20'; W='#ffffff'
LOGO='/_blob/0754512c9d115284b57fd1a8d5f1c5d8'; PL='/_blob/5ab5cc2204ee4bbf3dbb22d98e40b904'; PS='/_blob/eaa293a753da728270603506b0c9c801'
PW,PH=1122,1402
I={
'users':'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
'ticket':'<path d="M3 8a2 2 0 0 0 2-2h14a2 2 0 0 0 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 0-2 2H5a2 2 0 0 0-2-2v-2a2 2 0 0 0 0-4z"/><path d="M13 6v2M13 11v2M13 16v2"/>',
'shirt':'<path d="M20.4 6.6 16 4a4 4 0 0 1-8 0L3.6 6.6a1 1 0 0 0-.5 1.2l1.4 3.6a1 1 0 0 0 1.3.5L7 11.4V20a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-8.6l1.2.5a1 1 0 0 0 1.3-.5l1.4-3.6a1 1 0 0 0-.5-1.2z"/>',
'bottle':'<path d="M10 2h4M10.5 2v3.5L8.5 8a3 3 0 0 0-.5 1.7V20a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2V9.7a3 3 0 0 0-.5-1.7l-2-2.5V2"/><path d="M8 12h8"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
'trophy':'<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
'coins':'<circle cx="9" cy="9" r="6"/><path d="M14.5 6.2A6 6 0 1 1 9 18"/><path d="M9 6.5v5M7.5 8h3"/>',
'cal':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/>',
'pin':'<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
}
def ic(n,s,sw=1.8): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#ffffff" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="flex:none">{I[n]}</svg>'
EXT='font-weight:900;font-stretch:125%;text-transform:uppercase'
def small(t,fs,extra=''): return f'<div style="{EXT};font-size:{fs}px;line-height:1.15;letter-spacing:0.02em;{extra}">{t}</div>'
def grain(w,h): return f'<svg width="{w}" height="{h}" aria-hidden="true" style="position:absolute;left:0;top:0;opacity:0.18;mix-blend-mode:overlay"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>'
def bg(): return f'background:radial-gradient(ellipse 75% 60% at 55% 40%,#e0213f 0%,{RED} 50%,{DK} 100%)'

def item(icon,label,body,isz,lf,bf):
    return f'''<div style="display:flex;gap:16px;align-items:flex-start">{ic(icon,isz)}<div><div style="{EXT};font-size:{lf}px;letter-spacing:0.08em;opacity:0.85">{label}</div><div style="font-weight:700;font-size:{bf}px;line-height:1.3;margin-top:4px">{body}</div></div></div>'''

def pack(isz,fs):
    one=lambda n,t: f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;width:{isz+40}px">{ic(n,isz)}<div style="font-weight:700;font-size:{fs}px;text-align:center">{t}</div></div>'
    return f'<div style="display:flex;gap:14px">{one("shirt","T-shirt")}{one("bottle","Água")}{one("ticket","Voucher 1h30")}</div>'

def sponsor(top,h,logo_h,pad,label_fs):
    return f'''  <div style="position:absolute;left:0;right:0;top:{top}px;height:{h}px;box-sizing:border-box;padding:0 {pad}px;display:flex;align-items:center;justify-content:center;gap:36px;border-top:2px solid rgba(255,255,255,0.35)">
    <div style="{EXT};font-size:{label_fs}px;letter-spacing:0.12em;line-height:1.3;text-align:right">Patrocinador<br>oficial</div>
    <img src="{PS}" alt="P&amp;S Auto Color Expert" style="height:{logo_h}px;width:auto">
  </div>'''

def phases(top,left,right,f1,f2):
    it=[('01 a 14 Nov','Inscrições'),('15 a 22 Nov','Pagamentos'),('25 Nov','Grupo de WhatsApp'),('30 Nov','Calendário')]
    c=''.join(f'<div><div style="{EXT};font-size:{f1}px">{a}</div><div style="font-weight:600;font-size:{f2}px;opacity:0.85;margin-top:2px">{b}</div></div>' for a,b in it)
    return f'  <div style="position:absolute;left:{left}px;right:{right}px;top:{top}px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px">{c}</div>'

def portrait(Wd,H,T,ttop,nfs,pl_h,pl_bottom,col_top,ph_top,sp_top,sp_h,logo_h):
    sc=pl_h/PH; pw=PW*sc
    return f'''<div class="ar" style="position:relative;width:{Wd}px;height:{H}px;overflow:hidden;{bg()};color:#ffffff">
  {grain(Wd,H)}
  <!-- Topo -->
  <div style="position:absolute;left:56px;right:56px;top:{T}px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:20px">
    {small('4 · 5 · 6 Dezembro<br>2026',19)}
    <img src="{LOGO}" alt="TomarPadel 2.0" style="width:230px;height:auto">
    {small('TomarPadel 2.0<br>Tomar',19,'text-align:right')}
  </div>
  <!-- Título -->
  <div style="position:absolute;left:0;right:0;top:{ttop}px;text-align:center;{EXT};font-size:{int(nfs*0.17)}px;letter-spacing:0.3em">Torneio de</div>
  <div style="position:absolute;left:0;right:0;top:{ttop+int(nfs*0.25)}px;text-align:center;{EXT};font-size:{nfs}px;line-height:0.82;letter-spacing:-0.03em">Natal</div>
  <!-- Jogadores -->
  <img src="{PL}" alt="Dupla mista de padel em jogo" style="position:absolute;left:{Wd-pw:.0f}px;top:{pl_bottom-pl_h}px;width:{pw:.0f}px;height:{pl_h}px;filter:drop-shadow(0 22px 30px rgba(70,0,10,0.45)) saturate(0.92) contrast(1.05);-webkit-mask-image:linear-gradient(180deg,#000 82%,rgba(0,0,0,0.35) 100%);mask-image:linear-gradient(180deg,#000 82%,rgba(0,0,0,0.35) 100%)">
  {grain(Wd,H)}
  <!-- Especial equipas -->
  <div style="position:absolute;left:56px;top:{col_top}px;display:flex;flex-direction:column;gap:28px;width:340px">
    <div style="display:flex;flex-direction:column;align-items:flex-start;gap:10px">
      <div style="background:#ffffff;color:{RED};padding:10px 18px;{EXT};font-size:24px;line-height:1;white-space:nowrap">Especial de equipas</div>
      <div style="border:2px solid #ffffff;padding:8px 16px;{EXT};font-size:20px;line-height:1;white-space:nowrap">Torneio do Barril</div>
      <div style="display:flex;align-items:center;gap:10px;font-weight:700;font-size:21px">{ic('users',26)}Equipas de 4 elementos</div>
    </div>
    {item('trophy','Categorias','Mistos Iniciante<br>Mistos Avançado<br>Masculinos Iniciante<br>Masculinos Avançado',34,15,20)}
    {item('ticket','Inscrição','<span style="'+EXT+';font-size:40px;line-height:1">25€</span><br>+10€ pela 2ª categoria',34,15,20)}
    <div style="display:flex;flex-direction:column;gap:12px"><div style="{EXT};font-size:15px;letter-spacing:0.08em;opacity:0.85">Welcome pack</div>{pack(40,17)}</div>
    {item('coins','Prémios','Troféu de equipa e<br>prize money para<br>1º e 2º lugar',34,15,20)}
  </div>
{phases(ph_top,56,56,19,15)}
{sponsor(sp_top,sp_h,logo_h,56,17)}
</div>'''

def landscape():
    Wd,H=1920,1080; pl_h=900; pw=PW*pl_h/PH
    return f'''<div class="ar" style="position:relative;width:3840px;height:2160px;overflow:hidden;background:{DK};color:#ffffff">
<div style="position:absolute;left:0;top:0;width:1920px;height:1080px;transform:scale(2);transform-origin:0 0;{bg()}">
  {grain(Wd,H)}
  <div style="position:absolute;left:72px;right:72px;top:48px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center">
    {small('4 · 5 · 6 Dezembro 2026',20)}
    <img src="{LOGO}" alt="TomarPadel 2.0" style="width:260px;height:auto">
    {small('TomarPadel 2.0 · Tomar',20,'text-align:right')}
  </div>
  <div style="position:absolute;left:72px;top:150px;{EXT};font-size:48px;letter-spacing:0.3em">Torneio de</div>
  <div style="position:absolute;left:60px;top:205px;{EXT};font-size:270px;line-height:0.82;letter-spacing:-0.03em">Natal</div>
  <img src="{PL}" alt="Dupla mista de padel em jogo" style="position:absolute;left:{1920-pw:.0f}px;top:{940-pl_h}px;width:{pw:.0f}px;height:{pl_h}px;filter:drop-shadow(0 22px 30px rgba(70,0,10,0.45)) saturate(0.92) contrast(1.05);-webkit-mask-image:linear-gradient(180deg,#000 82%,rgba(0,0,0,0.35) 100%);mask-image:linear-gradient(180deg,#000 82%,rgba(0,0,0,0.35) 100%)">
  {grain(Wd,H)}
  <div style="position:absolute;left:72px;top:520px;width:470px;display:flex;flex-direction:column;gap:24px">
    <div style="display:flex;flex-direction:column;align-items:flex-start;gap:10px">
      <div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start"><div style="background:#ffffff;color:{RED};padding:9px 16px;{EXT};font-size:26px;line-height:1;white-space:nowrap">Especial de equipas</div><div style="border:2px solid #ffffff;padding:7px 14px;{EXT};font-size:20px;line-height:1;white-space:nowrap">Torneio do Barril</div></div>
      <div style="display:flex;align-items:center;gap:10px;font-weight:700;font-size:19px">{ic('users',24)}Equipas de 4 elementos</div>
    </div>
    {item('trophy','Categorias','Mistos Iniciante · Avançado<br>Masculinos Iniciante · Avançado',30,14,18)}
    {item('ticket','Inscrição','<span style="'+EXT+';font-size:36px;line-height:1">25€</span><br>+10€ pela 2ª categoria',30,14,18)}
  </div>
  <div style="position:absolute;left:600px;top:520px;width:460px;display:flex;flex-direction:column;gap:24px">
    <div style="display:flex;flex-direction:column;gap:10px"><div style="{EXT};font-size:14px;letter-spacing:0.08em;opacity:0.85">Welcome pack</div>{pack(36,16)}</div>
    {item('coins','Prémios','Troféu de equipa e<br>prize money para<br>1º e 2º lugar',30,14,18)}
    {item('cal','Fases','Inscrições 01 a 14 Nov · Pagamentos 15 a 22 Nov<br>Grupo de WhatsApp 25 Nov · Calendário 30 Nov',30,14,16)}
  </div>
{sponsor(950,130,96,72,16)}
</div>
</div>'''

def wrap(title,body,w,h):
    return f'''<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
HELMET
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
post=portrait(1080,1350,48,140,236,860,1110,410,1124,1200,150,104)
story=portrait(1080,1920,150,300,236,900,1530,620,1560,1690,170,116)
a4b=portrait(1080,1528,60,160,236,960,1270,450,1290,1370,158,110)
a4=f'<div class="ar" style="position:relative;width:794px;height:1123px;overflow:hidden;background:{DK}"><div style="position:absolute;left:0;top:0;width:1080px;height:1528px;transform:scale(0.735185);transform-origin:0 0">'+a4b.replace('<div class="ar" ','<div ',1)+'</div></div>'
open(R+'NatalPost.dc.html','w').write(wrap('Torneio de Natal post',post,1080,1350))
open(R+'NatalStory.dc.html','w').write(wrap('Torneio de Natal story',story,1080,1920))
open(R+'NatalA4.dc.html','w').write(wrap('Torneio de Natal cartaz A4',a4,794,1123))
open(R+'NatalTV.dc.html','w').write(wrap('Torneio de Natal TV 4K',landscape(),3840,2160))
