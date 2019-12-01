# DrawEllipse.py
 
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
#生成深蓝色绘图画布
array = np.ndarray((480, 640, 3), np.uint8)
array[:, :, 0] = 0
array[:, :, 1] = 0
array[:, :, 2] = 0

# 画坐标轴
for i in range(0,480,5):
  array[i,320]=(255,255,255)
for j in range(0,640,5):
  array[240,j]=(255,255,255)

# 利用对称性根据一点画出其他三个点
def draw(x,y):
  array[x+240,y+320]=(255,0,0)
  array[x+240,320-y]=(255,0,0)
  array[240-x,320-y]=(255,0,0)
  array[240-x,y+320]=(255,0,0)

# 中点画椭圆法
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

def main():
  # 输入长短半径a,b
  a,b=map(int,input("请输入a,b:").split())
  MidpointEllipse(a,b)
  image = Image.fromarray(array)
  image=image.rotate(90)
  #创建绘制对象
  draw = ImageDraw.Draw(image)
  #绘制文本
  font = ImageFont.truetype("consola.ttf", 40, encoding="unic")#设置字体
  draw.text((100, 125), u'ellipse', 'fuchsia', font)
  image.show()

if __name__ == '__main__':
  main()




 


