# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt

def elipse(n, m, O, a, b, fill = 1):
    RGB = np.zeros((m, n, 3), dtype=np.uint8)
    RGB.fill(255)
    x, y = O[0], O[1]
    
    if fill==1:
        for i in range(x-a if x-a>0 else 0, x+a+1 if x+a+1<m else m):
            for j in range(y-b if y-b>0 else 0 ,y+b+1 if y+b+1 < n else n):
                if ((x-i)**2/a**2)+((y-j)**2/b**2)<=1:
                    RGB[j][i] = 100
    else:
        for i in range(x-a if x-a>0 else 0, x+a+1 if x+a+1<m else m):
            for j in range(y-b if y-b>0 else 0 ,y+b+1 if y+b+1 < n else n):
                if ((x-i)**2/a**2)+((y-j)**2/b**2)<=1 and ((x-i)**2/a**2)+((y-j)**2/b**2)>=0.6:
                    RGB[j][i] =  5*abs((((x-i)**2/a**2)+(y-j)**2/b**2)-0.8)*255
                    
        
    return RGB

data = elipse(100, 100,[50,50], 20, 50, 0)
# data = elipse(100, 100,[50,50], 50, 20, 0)


plt.imshow(data)

# data2 = np.zeros((10, 10, 3), dtype=np.uint8)
# data2.fill(255)
# pukty_test = [[i,j] for i in range(-2,13,7) for j in range(-2,13,7)]
# for i in data:
#     for j in i:
#         if(j[0]!=255):
#             print(j)    
    
# for i in pukty_test:
#     for j in pukty_test:
#         data = elipse(10, 10, j, i[0], i[1], 0)

# plt.imshow(data)
        

# print(pukty_test)

# for i in data2:
#     for j in i:
#         print(j)
