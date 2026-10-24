import onnxruntime as ort, numpy as np
from PIL import Image
src='/root/.claude/uploads/4597a63e-1f82-5e3b-9ef6-d26353c1c0bf/94f92131-image.png'
im=Image.open(src).convert('RGB')
def run(model,size,mean,std):
    s=ort.InferenceSession(f'/home/claude/models/{model}.onnx',providers=['CPUExecutionProvider'])
    x=np.asarray(im.resize((size,size),Image.LANCZOS)).astype(np.float32)/255.
    x=(x-mean)/std; x=x.transpose(2,0,1)[None].astype(np.float32)
    o=s.run(None,{s.get_inputs()[0].name:x})[0][0,0]
    o=(o-o.min())/(o.max()-o.min()+1e-8)
    return np.asarray(Image.fromarray((o*255).astype(np.uint8)).resize(im.size,Image.LANCZOS))
a=run('isnet-general-use',1024,np.array([0.5,0.5,0.5]),np.array([1,1,1]))
b=run('u2net_human_seg',320,np.array([0.485,0.456,0.406]),np.array([0.229,0.224,0.225]))
Image.fromarray(a).save('/home/claude/bk/gen/m_isnet.png'); Image.fromarray(b).save('/home/claude/bk/gen/m_human.png')
for n,m in [('isnet',a),('human',b)]:
    o=im.copy(); o.putalpha(Image.fromarray(m))
    c=Image.alpha_composite(Image.new('RGBA',im.size,(255,255,255,255)),o).convert('RGB').resize((374,467))
    c.save(f'/home/claude/bk/gen/c_{n}.png')
s=Image.new('RGB',(758,467),'#888'); s.paste(Image.open('/home/claude/bk/gen/c_isnet.png'),(0,0)); s.paste(Image.open('/home/claude/bk/gen/c_human.png'),(384,0)); s.save('/home/claude/bk/gen/c_cmp.png')
