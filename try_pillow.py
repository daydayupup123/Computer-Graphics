#-*- coding: UTF-8 -*-  
 
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
#生成深蓝色绘图画布
array = np.ndarray((480, 640, 3), np.uint8)
array[:, :, 0] = 255
array[:, :, 1] = 255
array[:, :, 2] = 255

#DDA画直线
def DDA(x0,y0,x1,y1):
  x0=200 
  y0=200
  x1=480
  y1=480
  dx=x1-x0
  dy=y1-y0
  k=(dy)/dx
  y=y0
  for x in range(x0,x1,1):
    array[x,int(y+0.5)]=(255,255,255)
    y=y+k
  return
# DDA(200,200,480,450)

def MidPiont(x2,y2,x3,y3):
#中点画线法
  a=y2-y3
  b=x3-x2
  d=2*a+b
  d1=2*a
  d2=2*(a+b)
  x=x2
  y=y2
  array[x,y]=(0,0,0)
  while(x<x3):
    if(d<0):
      x+=1
      y+=1
      d+=d2
    else:
      x+=1
      d+=d1
    array[x,y]=(0,0,0)
  return
# MidPiont(20,30,200,300)


#Bresenham画直线
def Bresenham(x0,y0,x1,y1):
  dx=x1-x0
  dy=y1-y0
  e=-dx
  x=x0
  y=y0
  for i in range(dx):
    array[x,y]=(123,233,255)
    x+=1
    e+=2*dy
    if(e>=0):
      y+=1
      e-=2*dx
    i+=1
  return
# Bresenham(234,123,450,450)

# 画坐标轴
for i in range(0,480,5):
  array[i,320]=(0,0,0)
for j in range(0,640,5):
  array[240,j]=(0,0,0)


def draw(x,y):
  array[x+240,y+320]=(255,0,0)
  array[x+240,320-y]=(255,0,0)
  array[240-x,320-y]=(255,0,0)
  array[240-x,y+320]=(255,0,0)

def MidpointEllipse(a,b):
  x=0
  y=b
  d1=b*b+a*a*(-b+0.25)
  draw(x,y)
  while(b*b*(x+1)<a*a*(y-0.5)):
    if(d1<0):
      d1+=b*b*(2*x+3)
      x+=1
    else:
      d1+=(b*b*(2*x+3)+a*a*(-2*y+2))
      x+=1
      y-=1
    draw(x,y)
  d2=b*b*(x+0.5)*(x+0.5)+a*a*(y-1)*(y-1)-a*a*b*b
  while(y>0):
    if(d2<0):
      d2+=b*b*(2*x+2)+a*a*(-2*y+3)
      x+=1
      y-=1
    else:
      d2+=a*a*(-2*y+3)
      y-=1
    draw(x,y)
a=input("请输入x：")
a=int(a)
b=input("请输入y：")
b=int(b)
MidpointEllipse(a,b)

def circlepoints(x,y):
  array[y+240,x+320]=(255,255,255)
  array[x+240,y+320]=(255,255,255)
  array[240-y,x+320]=(255,255,255)
  array[x+240,320-y]=(255,255,255)
  array[y+240,320-x]=(255,255,255)
  array[240-x,y+320]=(255,255,255)
  array[240-x,320-y]=(255,255,255)
  array[240-y,320-x]=(255,255,255)
#中点画圆法
def MidPointCircle(r):
  x=0
  y=r
  d=1.25-r
  circlepoints(x,y)
  while(x<=y):
    if(d<0):
      d+=2*x+3
    else:
      d+=2*(x-y)+5
      y-=1
    x+=1
    circlepoints(x,y)
# MidPointCircle(50)

#改进后的中点画圆法1
def MidPointCircle1(r):
  x=0
  y=r
  d=1.25-r
  circlepoints(x,y)
  while(x<=y):
    if(d<0):
      d+=2*x+3
    else:
      d+=2*(x-y)+5
      y-=1
    x+=1
    circlepoints(x,y)

image = Image.fromarray(array)


#创建绘制对象
draw = ImageDraw.Draw(image)

#绘制直线
# draw.line((20, 20, 150, 150), 'cyan')
 
#绘制矩形
# draw.rectangle((100, 200, 300, 400), 'black', 'red')
 
#绘制弧
# draw.arc((100, 200, 300, 400), 0, 180, 'yellow')
# draw.arc((100, 200, 300, 400), -90, 0, 'green')
 
#绘制弦
# draw.chord((350, 50, 500, 200), 0, 120, 'khaki', 'orange')
 
#绘制圆饼图
# draw.pieslice((350, 50, 500, 200), -150, -30, 'pink', 'crimson')

#绘制椭圆
# draw.ellipse((350, 300, 500, 400), 'yellowgreen', 'wheat')
#外切矩形为正方形时椭圆即为圆
# draw.ellipse((550, 50, 600, 100), 'seagreen', 'skyblue') 
 
#绘制多边形
# draw.polygon((150, 180, 200, 180, 250, 120, 230, 90, 130, 100), 'olive', 'hotpink')
 
#绘制文本
font = ImageFont.truetype("consola.ttf", 40, encoding="unic")#设置字体
draw.text((100, 125), u'ellipse', 'fuchsia', font)


image.show()
image.save('D:\\4.jpg')
 


