import matplotlib.pyplot as plt
import ConfigSettings

# 初始化配置类对象
config = ConfigSettings.ConfigSettings(
    "hello python", "time", "value", "red")

# 定义图片样式
plt.style.use('Solarize_Light2')
# 定义折线点位
squares = [1, 4, 9, 16, 2.5, 3, 12]
# 定义x轴坐标
input_values = [1, 2, 3, 4, 5, 6, 7]

# 绘制打点坐标
x_values = [1, 2, 3, 4, 7]
y_values = [1, 4, 9, 16, 12]

# 在一张图片中绘制一个或多个图表。变量fig 表示整张图片。变量ax 表示图片中的各个图表，
# 大多数情况下要使用它，返回一个tuple2元组
fig, ax = plt.subplots()
# 根据给定的数据以有意义的方式绘制图表
ax.plot(input_values, squares, color=config.color, linewidth=2)
ax.set_title(config.title, fontsize=24)
ax.set_xlabel(config.x_lable, fontsize=14)
ax.set_ylabel(config.y_lable, fontsize=14)
ax.scatter(x_values, y_values, s=200)
# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)
# 打开Matplotlib查看器并显示绘制的图表
plt.show()
