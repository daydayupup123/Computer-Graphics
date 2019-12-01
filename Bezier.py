# 绘制Bezier曲线
import matplotlib.pyplot as plt 
C=[1,6,15,20,15,6,1]  # n=6 组合数的大小

# sample data
'''
0 5
2 8
4 8
6 5
6 3
4 2
2 3
'''
x=[]
y=[]
n=6
def input_dot(): # 输入特征多边形的七个点
    for i in range(n+1):
        x_,y_=map(int,input('请输入x{0},y{1}:'.format(i,i)).split())
        x.append(x_)
        y.append(y_)

def main():    # 根据递推公式计算Bezier曲线上的点的位置并用plt显示
    x1=[]
    y1=[]
    t=0
    for i in range(200):
        x_val=0.0
        y_val=0.0
        for c in range(n+1):
            x_val+=C[c]*pow((1-t),n-c)*pow(t,c)*x[c]
            y_val+=C[c]*pow((1-t),n-c)*pow(t,c)*y[c]
        x1.append(x_val)
        y1.append(y_val)
        t+=1.0/200
    plt.plot(x1,y1) #绘制Bezier曲线上的点
    plt.plot(x,y)  #绘制原来的特征多边形
    plt.show()

if __name__ == '__main__':
    input_dot()   # 输入特征多边形的七个点
    main()        # 根据递推公式计算Bezier曲线上的点的位置并用plt显示