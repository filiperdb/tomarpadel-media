import sys
M={"cbcc0d5c62dc16ab8b8b1d33cfca4255":"up/hb_mix.png","3abb1c8838281a3f2acc193f4c736d5c":"up/hb_peru.png","b5766fbe4549f1be851c577d3ff37a51":"up/hb_premium.png","7c8fe9d4ae90b0108d3761c2e7bbf5b3":"up/badge_mix.png","e571ab9883aadd19bb7a8b3845235ef8":"up/badge_peru.png","9763e8ddd2fcce187315681c7f2061df":"up/badge_premium.png","06a0ea9c9e3c3501defa51b53d61fc9d":"up/pz_bandeja.png","ffd55ac49681451d49da23412490eb30":"up/pz_smash.png","1a281b851ab970c4008c71421bfa4a75":"up/pz_vibora.png","78a70429dfcc53f2a5359f039a8ba3b2":"up/pz_chiquita.png","dc3d83e345011d3f1ffac2f7705daff1":"up/tosta_dupla.png","44eee24a5cd1e9787a46727ba3b7a9da":"up/tosta_topspin.png","909dd2ac312cece0fa78f09964e7df4a":"up/paochourico.png","68a1fbb65ee099cfb540e2585a9e7c2f":"up/canard_p0.ttf","e487ab41d8a8e7f90496c49f472b452f":"up/canard_p1.ttf","8ec4effb66e53780be0b35491d186fbf":"up/canard_p2.ttf","677926230f4337ea2d995a7c2cfb4e0f":"up/canard_p3.ttf","3df5852486fc0a085ad4eec930fd3571":"up/canard_p4.ttf","1a9bac115eade3c590df06615fca81c2":"up/canard_p5.ttf","be1e0876a168593566d7a44957536d2b":"up/logo_tomarpadel.png","2a03ee7e21dadc652faf9ec2b69d204a":"up/cooperhewitt-book.woff2","bbd0500170b692b1ad2a50c18ad3e948":"up/bg_2col.png","cb2790c698afad96708458723c64ec3d":"up/minipizza.png","b1327e3bdc30d681c4d35bc5f7582875":"up/v2_bifana.png","ba35b9d8e1515294f238d606bed8ebd5":"up/v2_caldo.png","21558e620c1f45ddd734945880706e1b":"up/v2_ovo.png"}
from playwright.sync_api import sync_playwright
src_path,out,w,h=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
s=open(src_path).read()
for k,v in M.items(): s=s.replace("/_blob/"+k,"file:///home/claude/work/"+v)
s=s.replace('<script src="./support.js"></script>','')
open("/home/claude/work/_p.html","w").write(s)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":w,"height":h})
    pg.goto("file:///home/claude/work/_p.html"); pg.wait_for_timeout(2000); pg.screenshot(path=out); b.close()
