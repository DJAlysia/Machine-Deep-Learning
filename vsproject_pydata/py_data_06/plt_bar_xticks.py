import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.TTF"
font=font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)
plt.rcParams['axes.unicode_minus'] = False

stores = [500, 550, 590, 610]
area_no = [0, 1, 2, 3]
area = ['스타벅스','이디야','메가커피','빽다방']

plt.bar(area_no, stores)
plt.xticks(area_no, area)
plt.show()
