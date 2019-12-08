import numpy as np
from PIL import Image,ImageFont,ImageDraw

array=np.ndarray((480,640,3),np.uint8)
array[:,:,:]=0
image=Image.fromarray(array)
draw=ImageDraw.Draw(image)

def swap1(x1,y1,x2,y2):
    if(x1>x2):
        sx=x2
        sy=y2
        dx=x1
        dy=y1
    else:
        sx=x1
        sy=y1
        dx=x2
        dy=y2
    return sx,sy,dx,dy

def swap2(x1,y1,x2,y2):
    if(y1>y2):
        sx=x2
        sy=y2
        dx=x1
        dy=y1
    else:
        sx=x1
        sy=y1
        dx=x2
        dy=y2
    return sx,sy,dx,dy

def drawline1(x1,y1,x2,y2):
    sx,sy,dx,dy=swap1(x1,y1,x2,y2)
    a=sy-dy
    b=dx-sx
    d=2*a+b
    x=sx
    y=sy
    while(x<=dx):
        draw.point((x,y),fill='red')   
        # print(x,y) 
        if d<0:
            x+=1
            y+=1
            d+=2*(a+b)
        else:
            x+=1
            d+=2*a
def drawline2(x1,y1,x2,y2):
    sx,sy,dx,dy=swap1(x1,y1,x2,y2)
    # sx,sy,dx,dy=x1,y1,x2,y2
    a=sy-dy
    b=dx-sx
    d=2*a-b
    x=sx
    y=sy
    while(x<=dx):
        draw.point((x,y),fill='red') 
        # print(x,y)    
        if d>=0:
            x+=1
            y-=1
            d+=2*(a-b)
        else:
            x+=1
            d+=2*a

def drawline3(x1,y1,x2,y2):
    sx,sy,dx,dy=swap2(x1,y1,x2,y2)
    a=sy-dy
    b=dx-sx
    d=a+2*b
    x=sx
    y=sy
    while(y<=dy):
        draw.point((x,y),fill='red')   
        # print(x,y) 
        if d>=0:
            x+=1
            y+=1
            d+=2*(a+b)
        else:
            y+=1
            d+=2*b

def drawline4(x1,y1,x2,y2):
    sx,sy,dx,dy=swap2(x1,y1,x2,y2)
    a=sy-dy
    b=dx-sx
    d=a+2*b
    x=sx
    y=sy
    while(y<=dy):
        draw.point((x,y),fill='red')   
        # print(x,y) 
        if d<0:
            x-=1
            y+=1
            d+=2*(-a+b)
        else:
            y+=1
            d+=2*b

def drawline(x1,y1,x2,y2):
    if x1==x2:
        drawline3(x1,y1,x2,y2)
        return 
    if y1==y2:
        drawline1(x1,y1,x2,y2)
        return
    k=(y2-y1)/(x2-x1)
    if k>=0:
        if k<=1:
            drawline1(x1,y1,x2,y2)
        else:
            drawline3(x1,y1,x2,y2)
    else:
        if k>=-1:
            drawline2(x1,y1,x2,y2)
        else:
            drawline4(x1,y1,x2,y2)

# draw.point((20,20),fill='red')
# drawline(80,20,20,20)
# drawline(80,20,80,100)
# drawline(20,20,2,2)   #0<=k<=1
# drawline(150,0,0,80)   #-1<=k<=0
# drawline(50,200,2,2)   #k>1
# drawline(2,200,50,2)   #k<-1
class node(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
points=[]
n=6
x=0
y=0

# 输入六边形的六个顶点的位置
def init():            
    drawline(200,150,206,150)
    drawline(206,150,211,150)
    drawline(212,150,217,151)
    drawline(217,151,223,152)
    drawline(223,152,228,153)
    drawline(223,152,228,153)

    return
init()
draw.text((100,50),u'CG Demo','red')
image.show()