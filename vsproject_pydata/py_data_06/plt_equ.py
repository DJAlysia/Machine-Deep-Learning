# 포물선 y = x*x
# x = 0~100까지
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

x_val = range(-100,101) # 101 포함이 안됨
# 10 * 10
y_val = [x*x for x in x_val]

font_path = "C:/Windows/Fonts/malgun.TTF"
font=font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

plt.rcParams['axes.unicode_minus'] = False

plt.title('2차원 포물선') # 맑은고딕 C:\Windows\Fonts\malgun.ttf
plt.plot(x_val, y_val)
plt.show()

