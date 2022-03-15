#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/15 11:01 上午
# @Author : Jamerri
# @FileName: 2_1.py
# @Email : jamerri@163.com
# @Software: PyCharm


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
#  y = 2*x + 1
y = x**2
plt.plot(x, y)
plt.show()
