import sys,glob
h=open('/home/claude/bk/gen/helmet.txt').read().strip()
for p in sys.argv[1:]:
    s=open(p).read()
    if 'HELMET' in s: open(p,'w').write(s.replace('HELMET',h,1)); print('filled',p.split('/')[-1])
