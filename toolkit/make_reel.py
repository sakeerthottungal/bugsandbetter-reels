import re,subprocess,os,shutil
from PIL import Image,ImageDraw,ImageFont
W,H=1080,1920;BG=(0,0,0);WHITE=(245,245,245);GREY=(120,120,120)
SZ=50;LG=20;BG_GAP=62;M=96;HANDLE="@bugsandbetter"
FD="/usr/share/fonts/truetype/dejavu/"
fr=ImageFont.truetype(FD+"DejaVuSansMono.ttf",SZ);fb=ImageFont.truetype(FD+"DejaVuSansMono-Bold.ttf",SZ)
LOGO=Image.open("assets/logo_icon_white.png")
LH=56;LOGO=LOGO.resize((int(LOGO.width*LH/LOGO.height),LH))
def tok(s):
    out=[]
    for part in re.split(r'(\*\*[^*]+\*\*)',s):
        b=part.startswith('**');t=part.strip('*') if b else part
        for w in t.split():
            if re.fullmatch(r'[^\w]+',w) and out: out[-1]=(out[-1][0]+w,out[-1][1])
            else: out.append((w,b))
    return out
def wrap(words,maxw):
    lines=[];cur=[]
    for w in words:
        trial=cur+[w];n=sum(len(x[0]) for x in trial)+len(trial)-1
        if n*fr.getlength("M")>maxw and cur: lines.append(cur);cur=[w]
        else: cur=trial
    if cur: lines.append(cur)
    return lines
def blocks(q):
    bl=[]
    for c in q:
        parts=[c] if isinstance(c,str) else c
        lines=[]
        for p in parts: lines+=wrap(tok(p),W-2*M)
        bl.append(lines)
    return bl
lh=fr.getbbox("Ay")[3]-fr.getbbox("Ay")[1]+LG
cw=fr.getlength("M")
def layout(q):
    bl=blocks(q);total=sum(len(b)*lh for b in bl)+BG_GAP*(len(bl)-1)
    y=(H-total)//2-60;pos=[]
    for b in bl:
        for ln in b:
            x=M
            for w,bold in ln:
                pos.append((w,bold,x,y));x+=int(cw*(len(w)+1))
            y+=lh
        y+=BG_GAP
    return pos,len(blocks(q)[0])
def render(q,name,fps=30,wps=4.0,hold=2.0):
    pos,_=layout(q);first=sum(len(l) for l in blocks(q)[0])
    d="frames";shutil.rmtree(d,ignore_errors=True);os.makedirs(d)
    fpw=int(fps/wps);n=len(pos)-first;total=n*fpw+int(fps*hold);
    idx=0
    for f in range(total+1):
        shown=first+min(n,f//fpw)
        im=Image.new("RGB",(W,H),BG);dr=ImageDraw.Draw(im)
        for w,b,x,y in pos[:shown]:
            dr.text((x,y),w,font=fb if b else fr,fill=WHITE if b else GREY)
        lw,lb,lx,ly=pos[shown-1];cx=lx+int(cw*len(lw))+6
        typing=f//fpw<n
        if typing and (f*2.5*2//fps)%2==0 or not typing and False:
            dr.rectangle([cx,ly,cx+22,ly+SZ+6],fill=WHITE)
        if not typing:
            t=min(1,(f-n*fpw)/(fps*0.8))
            a=int(255*t)
            l=LOGO.copy();al=l.split()[3].point(lambda v:v*t);l.putalpha(al)
            im.paste(l,((W-l.width)//2,H-330),l)
            for txt,fs,fill,yy in((HANDLE,28,90,H-260),("// New leadership truth daily",28,70,H-210)):
                ft=ImageFont.truetype(FD+"DejaVuSansMono.ttf",fs);tw=dr.textlength(txt,font=ft)
                c=int(fill*t*1.0);dr.text(((W-tw)//2,yy),txt,font=ft,fill=(c,c,c))
        im.save(f"{d}/f{f:05d}.png")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",f"{d}/f%05d.png","-c:v","libx264","-pix_fmt","yuv420p","-r",str(fps),name],check=True)
    im.save("last.png")
