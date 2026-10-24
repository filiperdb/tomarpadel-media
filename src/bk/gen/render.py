import sys,re
exec(open('/home/claude/bk/prev.py').read().split('from playwright')[0].replace('import sys',''))
from playwright.sync_api import sync_playwright
R='/tmp/claude-0/-home-claude/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/scratchpad/kit/project/'
jobs=[l.split() for l in open(sys.argv[1]).read().strip().splitlines()]
with sync_playwright() as p:
    b=p.chromium.launch()
    for src,out,w,h in jobs:
        s=open(R+src).read()
        for k,v in M.items(): s=s.replace("/_blob/"+k,"file:///home/claude/bk/assets/"+v)
        s=s.replace('<script src="./support.js"></script>','')
        open('/home/claude/bk/gen/_r.html','w').write(s)
        pg=b.new_page(viewport={"width":int(w),"height":int(h)})
        pg.goto("file:///home/claude/bk/gen/_r.html"); pg.wait_for_timeout(1800)
        pg.screenshot(path='/home/claude/bk/dl/'+out); pg.close(); print(out)
    b.close()
