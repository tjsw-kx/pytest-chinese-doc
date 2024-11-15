# from faker import Faker
#
# fake = Faker('zh_CN')
# 
# print(f"name:{fake.name()}")
# print(fake.address())
# print("email:"+fake.email())

from matplotlib import pyplot as plt
import pandas as pd
import pynimate as nim

df = pd.DataFrame(
    {
         "time": ["1960-01-01", "1961-01-01", "1962-01-01"],
        "Afghanistan": [1, 2, 3],
        "Angola": [2, 3, 4],
        "Albania": [1, 2, 5],
        "USA": [5, 3, 4],
        "Argentina": [1, 4, 5],
    }
).set_index("time")
# 初始化画布
cnv = nim.Canvas()
# 创建条形图并指定时间格式
bar = nim.Barplot(df, "%Y-%m-%d", "2d")
# 设置时间回调函数，处理时间索引（这里假设我们取年份）
bar.set_time(callback=lambda i, datafier: datafier.data.index[i].year)
# 将条形图添加到画布
cnv.add_plot(bar)
# 动画并显示图形
cnv.animate()
plt.show()
