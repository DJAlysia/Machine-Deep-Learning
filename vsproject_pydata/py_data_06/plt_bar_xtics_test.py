# x축 점수 = 60, 70, 40, 50, 100
# y축 1, 2, 3, 4, 5 => A B C D F
# yticks로 학점으로 눈금을 출력
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.TTF"
font=font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)
plt.rcParams['axes.unicode_minus'] = False

x_val = range(0,5)
y_val = [4, 3, 5, 2, 1]
y_label = ['D', 'C', 'F', 'B', 'A']

plt.bar(x_val, y_val, color='violet')
plt.yticks(y_val, y_label)
plt.xticks(x_val, [60, 70, 40, 80, 100])
plt.show()
