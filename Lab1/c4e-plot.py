import matplotlib
matplotlib.use("tkAgg")
from matplotlib import pyplot

#1. Prepare data
labels = ["Web", "Android", "iOS", "React Native"]
values = [57, 50, 22, 30]
colors = ["red", "blue", "yellow", "green"]
explode = [0, 0, 0, 0.2]

#2. Plot
pyplot.pie(values,
    labels = labels,
    colors = colors,
    explode = explode)
pyplot.axis('equal')

#3. Show
pyplot.show()