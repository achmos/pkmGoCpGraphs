from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from pkmcp import *

# currently hardcoded for Arcanine temporaily
mon_id = 59  # arcanine
ivs = [1, 1, 1]  # change later

levels = np.arange(1, 41, 0.5)
cps = [calculateCP(mon_id, lvl, ivs[0], ivs[1], ivs[2]) for lvl in levels]
hps = [calculateHP(mon_id, lvl, ivs[2]) for lvl in levels]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

plt.title('Pokemon CP vs Level')
plt.xlabel('Level')
plt.ylabel('Combat Power')
plt.axis([0, 41, 0, 4200])
graph, = plt.plot(levels, cps)  # why does it work with the comma but not without????

axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.15, 0.15, 0.65, 0.03], axisbg=axcolor)
ax_d = plt.axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)
ax_s = plt.axes([0.15, 0.05, 0.65, 0.03], axisbg=axcolor)
attack_iv_slider = Slider(ax_a, 'Attack', 0.0, 15.0, valinit=1, valfmt='%1.0f')
defense_iv_slider = Slider(ax_d, 'Defense', 0.0, 15.0, valinit=1, valfmt='%1.0f')
stamina_iv_slider = Slider(ax_s, 'Stamina', 0.0, 15.0, valinit=1, valfmt='%1.0f')


def update(val):
    ivs[0] = round(attack_iv_slider.val)
    ivs[1] = round(defense_iv_slider.val)
    ivs[2] = round(stamina_iv_slider.val)
    new_cps = [calculateCP(mon_id, lvl, ivs[0], ivs[1], ivs[2]) for lvl in levels]
    graph.set_ydata(new_cps)


attack_iv_slider.on_changed(update)
defense_iv_slider.on_changed(update)
stamina_iv_slider.on_changed(update)

# plt.subplot(212)
# plt.title('Pokemon HP vs Level')
# plt.xlabel('Level')
# plt.ylabel('Health Points')
# plt.axis([0, 41, 0, 450])
# plt.plot(levels, hps)

plt.show()

# scalars = [CPScalar(lvl) ** 0.5 for lvl in levels]
# [print(level) for level in results]
# print(hps)
# print(scalars)

# print(calculateCP(mon_id, 30, ivs[0], ivs[1], ivs[2]))
# print(calculateHP(mon_id, 30, ivs[2]))
## results = [[lvl, calculateCP(mon_id, lvl, ivs[0], ivs[1], ivs[2]), calculateHP(mon_id, lvl, ivs[2])]for lvl in levels]
