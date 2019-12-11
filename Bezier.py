 # 绘制Bezier曲线
import numpy as np
from PIL import Image,ImageFont,ImageDraw
array=np.ndarray((480,640,3),np.uint8)
array[:,:,:]=0
image=Image.fromarray(array)
draw=ImageDraw.Draw(image)
def swap1(x1,y1,x2,y2):  #选择x较小的作为画直线的起点
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
def swap2(x1,y1,x2,y2):  #选择y较小的作为画直线的起点
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
def drawline1(x1,y1,x2,y2):  #0<=k<=1的直线
    sx,sy,dx,dy=swap1(x1,y1,x2,y2)
    a=sy-dy
    b=dx-sx
    d=2*a+b
    x=sx
    y=sy
    while(x<=dx):
        draw.point((x,y),fill='red')   
        if d<0:
            x+=1
            y+=1
            d+=2*(a+b)
        else:
            x+=1
            d+=2*a
def drawline2(x1,y1,x2,y2):#-1<=k<=0的直线
    sx,sy,dx,dy=swap1(x1,y1,x2,y2)
    a=sy-dy
    b=dx-sx
    d=2*a-b
    x=sx
    y=sy
    while(x<=dx):
        draw.point((x,y),fill='red') 
        if d>=0:
            x+=1
            y-=1
            d+=2*(a-b)
        else:
            x+=1
            d+=2*a
def drawline3(x1,y1,x2,y2):  #k>1的直线
    sx,sy,dx,dy=swap2(x1,y1,x2,y2)
    a=sy-dy
    b=dx-sx
    d=a+2*b
    x=sx
    y=sy
    while(y<=dy):
        draw.point((x,y),fill='red')   
        if d>=0:
            x+=1
            y+=1
            d+=2*(a+b)
        else:
            y+=1
            d+=2*b
def drawline4(x1,y1,x2,y2):  #k<-1的直线
    sx,sy,dx,dy=swap2(x1,y1,x2,y2)
    a=sy-dy
    b=dx-sx
    d=a+2*b
    x=sx
    y=sy
    while(y<=dy):
        draw.point((x,y),fill='red')   
        if d<0:
            x-=1
            y+=1
            d+=2*(-a+b)
        else:
            y+=1
            d+=2*b
def drawline(x1,y1,x2,y2):   #根据不同情况画出直线
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

x,y=[],[]
midx,midy=np.zeros((7,7)),np.zeros((7,7))  #创建两个矩阵用于存储中间结果
n=6              #输入的点数
def input_dot(): # 输入特征多边形的六个点
    for i in range(n):
        x_,y_=map(int,input('请输入x{0},y{1}:'.format(i,i)).split())
        x.append(x_)
        y.append(y_)
    x.append(x[0])
    y.append(y[0])

def main():    # 根据递推公式计算Bezier曲线上的点的位置并绘制
    t=0
    midx[0],midy[0]=x,y
    for i in range(1000):
        for r in range(n):
            for c in range(n-r):
                midx[r+1][c]=midx[r][c]*(1-t)+midx[r][c+1]*t
                midy[r+1][c]=midy[r][c]*(1-t)+midy[r][c+1]*t
        draw.point((midx[6][0],midy[6][0]),fill='red')
        t+=1.0/1000
 
    for i in range(n):      #绘制原来的特征多边形
        drawline(x[i],y[i],x[(i+1)%n],y[(i+1)%n])
    draw.text((100,50),u'Bezier','red')
    image.show()

if __name__ == '__main__':
    input_dot()   # 输入特征多边形的六个点
    main()        # 根据递推公式计算Bezier曲线上的点的位置并显示
