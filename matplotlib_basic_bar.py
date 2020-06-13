# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:12:38 2020

@author: yomer
"""
import matplotlib.pyplot as plt

plt.style.use('ggplot')
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
rects = ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# 막대그래프에 y값의 label표시하기
for p in ax1.patches:
    left, bottom, width, height = p.get_bbox().bounds
    ax1.annotate(height, (left+width/2, height*1.01), ha='center')

plt.xticks(customers_index, customers, rotation=0, fontsize='small')
plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')
#plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()