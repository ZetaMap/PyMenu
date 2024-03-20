"""Documentation: https://github.com/ZetaMap/PyMenu"""
from kandinsky import fill_rect as fr,draw_string as ds
from ion import keydown as kd

def wait_key(*k):
 while k:
  for i in k:
   if kd(i):
    while kd(i):pass
    return i
def accent_colors():
 c=["#ffb531","1.0"]
 try:
  from ion import get_keys
  c[0]="#c53431"
 except:
  try:
   from kandinsky import get_palette as gp
   c=[gp()["Toolbar"],gp()["HomeBackground"]]
  except:pass
 return c
class Menu:
 colors=["0.95","0.2","0.38",accent_colors()[0],"#2a78e0"]
 r,u=colors,1
 options=lambda s:[s.p[i][s.c[i]]for i in range(s.s)]
 def __init__(s,title,action,*options):
  s.t,s.a,s.p=title[0:25],action[0:28],options
  s.s=len(s.p)
  s.c,s.b=[],len(s.a)
  for i in s.p :
   assert len(i)>2,"need [label,default,values...]"
   s.c.append(int(i[1])+2)
 def mo(s,i,o,u):
  t,l=str(s.p[i][s.c[i]])[0:15],i%6
  ds('<'*u+' '*(17-2*u)+'>'*u,140,65+l*25,s.r[2],s.r[1])
  ds(t,150+(150-10*len(t))//2,65+l*25,o,s.r[1])
 def do(s):
  u=s.u-1*(s.u>0)
  u=(u-(u and u==u//6*6))//6*6
  for i in range(6):
   if u+i<s.s:
    t=str(s.p[u+i][0])[0:12]
    ds(t+' '*(12-len(t)),10,65+i*25,s.r[0],s.r[1])
    s.mo(u+i,s.r[2],0)
   else:fr(10,65+i*25,300,18,s.r[1])
  if s.s>6:s.sb(u)
 def sb(s,u):
  fr(314,65,3,140,s.r[2])
  o=140//((s.s+5)//6)
  p=o*(u//6)
  fr(314,65+p,3,o+(u==s.s//6*6)*(140-o-p),s.r[3])
 def da(s,i):
  c=s.r[3*(i==0)]
  ds("<",10,8,c,s.r[1])
  fr(13,16,13,1,c)
  fr(26,10,1,6,c)
  ds(s.a,160-5*s.b,36,s.r[3*(i==1)],s.r[1])
 def ds(s):
  fr(0,0,320,222,s.r[1])
  ds(s.t,160-5*len(s.t),8,s.r[4],s.r[1])
  s.da(s.u)
  s.do()
 def close(s,b=0):
  fr(0,0,320,222,s.r[1])
  if b:s.u=1
  return[]if b else s.options()
 def open(s):
  s.ds()
  r=-1
  while 1:
   if r in(5,17):return s.close(1)
   elif r in(4,52):
    if s.u<2:return s.close(s.u==0)
    r=-2
   elif r in(-1,1,2):
    if s.u<2:s.da(s.u+1)
    s.u=(s.u-1*(r==1)+1*(r==2))%(s.s+2)
    s.do()
    if s.u>1:s.mo(s.u-2,s.r[3],1)
    else:s.da(s.u)
   if r in(-2,0,3)and s.u>1:
    v=s.u-2
    s.c[v],l=s.c[v]+1*(r==3)-1*(r==0)if r>=0 else s.p[v][1]+2,s.c[v]
    o=s.c[v]
    if o==1:s.c[v]=len(s.p[v])-1
    if o==len(s.p[v]):s.c[v]=2
    if l!=o and s.p[v][0].lower()=="darkmode":#special
     s.r[0],s.r[1]=s.r[1],s.r[0]
     s.ds()
    s.mo(v,s.r[3],1)
   r=wait_key(0,1,2,3,4,5,17,52)

if __name__ == '__main__':
 print(Menu("Game Settings","Start Game",
  ["Speed",9]+list(range(1,26)),
  ["Power",1]+list(range(1,21)),
  ["Size",9]+list(range(1,51)),
  ["Added Score",0]+list(range(1,21)),
  ["Expert Mode",1,"Yes","No"],
  ["Gost Snake",1,"Yes","No"],
  ["Darkmode",0,"Enabled","Disabled"],
  ["Rainbow",1,"On","Off"],
  ["Walls",0,"Yes","No"]
 ).open())
