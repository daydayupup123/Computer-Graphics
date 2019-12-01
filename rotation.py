# rotation.py
from polyfill import main as drawpoly #直接调用上个实验画多边形的函数
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import math
import array

# sample data
'''
200 200
300 200
350 280
300 360
200 360
150 280
'''
# 绘制画布
array = np.ndarray((480, 640, 3), np.uint8)
arrayc = np.ndarray((480, 640, 3), np.uint8)
arrayc[:,:,:]=array[:,:,:]
xr=200
yr=200
array=drawpoly()
# 计算变换矩阵
calc_cos=math.cos(math.pi*(-5/4))   #逆时针旋转225°
calc_sin=math.sin(math.pi*(-5/4))
rotation_arr=[[calc_cos,calc_sin,0],
[-calc_sin,calc_cos,0],
[(1-calc_cos)*xr+yr*calc_sin,(1-calc_cos)*yr-xr*calc_sin,1]]

# 利用齐次坐标实现相对于点的旋转
for i in range(480):
    for j in range(640):
        t=np.array([i,j,1])
        t=np.dot(t,rotation_arr)
        arrayc[i,j,:]=(array[min(max(int(t[0]),0),479),min(max(int(t[1]),0),639),:]) 
        # print(t[0])
# 显示原图像便于对比
for i in range(480):
    for j in range(640):
        if (arrayc[i,j,:]==np.array([255,255,255])).all():
            arrayc[i,j,:]=array[i,j,:]

# 创建绘制对象
image = Image.fromarray(arrayc)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("consola.ttf", 30, encoding="unic")#设置字体
draw.text((75, 20), u'Rotation(left:dst,right:src)', 'fuchsia', font)
image.show()