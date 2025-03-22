import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df=pd.read_excel('WorkData.xlsx')
x=df['H'].values
y=df['B'].values
print(x)
#隐藏多余的线段
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
#设置坐标轴
plt.gca().spines['bottom'].set_position(('data',0))
plt.gca().spines['left'].set_position(('data',0))
#设置标题
plt.title('Hysteresis Curve of Magnetization')

#x,y轴数据，线段的颜色
plt.plot(x,y,marker='o',linestyle='-',color='blue')

#图片保存
plt.savefig('Yours.png')

plt.show()





