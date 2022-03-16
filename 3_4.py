#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/16 1:38 下午
# @Author : Jamerri
# @FileName: 3_4.py
# @Email : jamerri@163.com
# @Software: PyCharm


import matplotlib.pyplot as plt
import numpy as np


# image data
a = np.array([0.31, 0.36, 0.42,
             0.36, 0.43, 0.52,
             0.42, 0.52, 0.65]).reshape(3, 3)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_method.html
"""
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()
