import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.TTF"
font=font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)
plt.rcParams['axes.unicode_minus'] = False

category = ['카테고리1', '카테고리2', '카테고리3',
            '카테고리4', '카테고리5']

x_pos = np.arange(len(category))

y_val_1 = [90, 60, 70, 40, 90]
y_val_2 = [70, 90, 80, 70, 80]
# 계속 여러 개 그래프 가능

# 두 개의 그래프를 동시에 그릴 수 있음 (비교하는 경우)
bar_width = 0.35
plt.bar(x_pos, y_val_1, color='yellow', width=bar_width, label='그래프 1')

plt.bar(x_pos+bar_width, y_val_2, color='blue', width=bar_width, label='그래프 2')

plt.title("두 개의 그래프 비교")
plt.legend()
plt.xlabel('도시명')
plt.ylabel('상점수')
plt.xticks(x_pos, category)

plt.show() 