# polyfill.py
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import array

# 绘制画布
array = np.ndarray((480, 640, 3), np.uint8)
array[:, :, 0] = 255
array[:, :, 1] = 255
array[:, :, 2] = 255

# 定义顶点坐标
class node(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

# 定义边
class edge(object):
    def __init__(self,x=0,dx=0.0,ymax=0):
        self.x=x
        self.dx=dx
        self.ymax=ymax
        self.next=None
# points=[node(100+100,30+120),node(200+100,30+120),node(250+100,110+120),node(200+100,190+120),node(100+100,190+120),node(50+100,110+120)]
# points=[node(2,7),node(5,5),node(11,8),node(11,3),node(5,1),node(2,2)]

# sample data
'''
200 150
300 150
350 230
300 310
200 310
150 230
'''
# points用来存储六边形的各个顶点
points=[]
n=6
x=0
y=0

# 输入六边形的六个顶点的位置
def init():            
    for i in range(n):
        x,y=map(int,input('请输入x{0},y{1}:'.format(i,i)).split())
        points.append(node(x,y))
    return


NET=[]  #新边表
def polygonScan():
    maxY=0
    minY=1000
    for po in points:
        if(maxY<po.y):
            maxY=po.y
        if(minY>po.y):
            minY=po.y
    # 初始化新边表和活性边表
    for i in range(0,maxY+1):
        NET.append(edge())
        NET[i].next=None
    AET=edge()
    AET.next=None

    point_num=len(points)
    for i in range(point_num):
        x1=points[i].x
        x2=points[(i+1)%point_num].x
        y0=points[(i-1+point_num)%point_num].y
        y1=points[i].y
        y3=points[(i+2)%point_num].y
        y2=points[(i+1)%point_num].y
        if(y1==y2):
            continue
        if(y1>y2):
            ymin=y2
            ymax=y1
            x=x2
        else:
            ymin=y1
            ymax=y2
            x=x1
        dx=(x1-x2)*1.0/(y1-y2)
        if(((y1<y2) and (y1>y0)) or ((y1>y2) and (y2>y3))):
            ymin+=1
            x+=dx
        # 插入新边
        p=edge(x,dx,ymax)
        p.next=NET[ymin].next
        NET[ymin].next=p

    
    # 从下到上扫描填充，同时更新活性边表
    for i in range(minY,maxY):
        q=AET
        while(q.next):
            q=q.next
        while NET[i].next:
            q=NET[i].next
            p=AET
            while(p.next):
                if(q.x>p.next.x):
                    p=p.next
                    continue
                if (p.next.x==q.x) and (q.dx>p.next.dx):
                    p=p.next
                    continue
                break
           
            NET[i].next=q.next
            q.next=p.next
            p.next=q
            
        p=AET
        while (p.next) and (p.next.next):
            for x in range(int(p.next.x),int(p.next.next.x)):
                array[x,i,0]=255
                array[x,i,1]=0
                array[x,i,2]=0
            p=p.next.next
        p=AET
        while(p.next):
            if(p.next.ymax==i):
                deletep=p.next
                p.next=deletep.next
                deletep.next=None
            else:
                p=p.next
        p=AET
        while(p.next):
            p.next.x+=p.next.dx
            p=p.next
    return

def main():
    init()  #输入凸六边形的六个顶点
    polygonScan()  #扫描线填充算法绘制凸六边形
    
    
    return array

if __name__ == '__main__':
  main()
  #创建绘制对象
  image = Image.fromarray(array)
  draw = ImageDraw.Draw(image)
  font = ImageFont.truetype("consola.ttf", 40, encoding="unic")#设置字体
  draw.text((75, 20), u'Convex hexagon', 'fuchsia', font)
  image.show()