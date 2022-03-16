#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/16 2:18 下午
# @Author : Jamerri
# @FileName: 4_1.py
# @Email : jamerri@163.com
# @Software: PyCharm


import matplotlib.pyplot as plt

plt.figure()

# 设置xtick和ytick的方向：in、out、inout
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0,  1])

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])

plt.show()
