import re
src=open('/home/claude/work/prev.py').read()
M=eval(re.search(r'M=(\{.*?\})\n',src,re.S).group(1))
from playwright.sync_api import sync_playwright
R='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/menus/project/'
jobs=[('PostHamburgueres','hamburgueres'),('PostPizzas','pizzas'),('PostTostas','tostas'),('PostSnacks','snacks'),('PostKids','kids'),('PostTorneio','especial-torneio')]
with sync_playwright() as p:
    b=p.chromium.launch()
    for s_,o in jobs:
        s=open(R+s_+'.dc.html').read()
        for k,v in M.items(): s=s.replace("/_blob/"+k,"file:///home/claude/work/"+v)
        s=s.replace('<script src="./support.js"></script>','')
        open('/home/claude/work/_r.html','w').write(s)
        pg=b.new_page(viewport={"width":1080,"height":1350})
        pg.goto("file:///home/claude/work/_r.html"); pg.wait_for_timeout(2000)
        pg.screenshot(path=f'/home/claude/bk/dl/bar/{o}.png'); pg.close(); print(o)
    b.close()
