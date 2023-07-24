import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/malgun.TTF"
font=font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
sub_plt1 = fig.add_subplot(2, 1, 1) # 총갯수, 행, 렬
sub_plt2 = fig.add_subplot(2, 1, 2) 

x_val = range(0, 101)
y1_val = [2*x for x in x_val]
y2_val = [x*x for x in x_val]

sub_plt1.plot(x_val, y1_val)
plt.subplot(2, 1, 1)
plt.title('서브플랏 1')

sub_plt2.plot(x_val, y2_val)
plt.subplot(2, 1, 2)
plt.title('서브플랏 2')

plt.show()

