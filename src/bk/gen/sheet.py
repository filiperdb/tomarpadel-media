import sys
from PIL import Image
outs=sys.argv[2:]; out=sys.argv[1]
ims=[Image.open(o) for o in outs]
w=ims[0].width; h=ims[0].height
s=Image.new('RGB',(len(ims)*(w+16)+16,h+32),'#222')
for i,im in enumerate(ims): s.paste(im,(16+i*(w+16),16))
s.save(out)
