# -*- coding: utf-8 -*-
import time
import numpy as np
import math
import matplotlib.pyplot as plt



def zaokraglij(x):
    return int(x+0.5)

def wyskokosc_padajaca_na_przeciwprostokatna(a,b):
    pole = a*b
    przeciw_prostoksokatna = math.sqrt(a**2+b**2)
    if (pole==0):
        return 0
    return pole/przeciw_prostoksokatna


def linePZ(m, n, P1, P2, d, RGB):
    assert type(d)==int and d>=1
    # RGB = np.zeros((m, n, 3), dtype=np.uint8)
    # RGB.fill(255)
    L=d
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    pozioma = False
    pionowa = False
    if x1>x2:
        x1,y1,x2,y2 = x2,y2,x1,y1

    if (y1-y2==0):
        pozioma = True
    elif x1-x2==0:
        pionowa = True
    
    else:
        a =(y2-y1)/(x2-x1)
        b = y1-a*x1
    if (pozioma):
        for i in range(x1 if x1>0 else 0, x2+1 if x2+1 <n else n):
            for j in range(y1-L if y1-L>0 else 0, y1+L+1 if y1+L+1<m else m):
                l = abs(y1 - j)
                if l*3<=L:
                    RGB[j][i] = 0
                elif l<L:
                    RGB[j][i] = int((l/L)*255 - 256-255/3)
    elif (pionowa):
        for i in range(x1-L if x1-L>0 else 0, x1+L+1 if x1+L+1 <n else n):
            for j in range(min(y1,y2) if min(y1, y2)>0 else 0, max(y1,y2)+1 if max(y1 ,y2)+1<m else m):
                l = abs(x1 - i)
                if l*3<=L:
                    RGB[j][i] = 0
                elif l<L:
                    RGB[j][i] = int((l/L)*255 - 256-255/3)                
    elif (abs(a)>1):
        for i in range(x1-L if x1-L > 0 else 0,x2+L+1 if x2+L+1<n else n):
            for j in range(min(y1,y2) if min(y1,y2)>0 else 0,max(y1,y2)+1 if max(y1,y2)+1<m else m):
                x = abs(i - (j-b)/a)               
                y = abs(j - (i*a+b))                                
                l = wyskokosc_padajaca_na_przeciwprostokatna(x, y)
                if l*3<=L:
                    RGB[j][i] = 0
                elif l<L:
                    RGB[j][i] = int((l/L)*255 - 256-255/3)
    else:
        for i in range(x1 if x1>0 else 0 ,x2+1 if x2+1<n else n):
            syy = zaokraglij(a*i+b)
            for j in range(syy-L if syy-L>0 else 0, syy+L+1 if syy+L+1 < m else m):
                x = abs(i - (j-b)/a)                
                y = abs(j - (i*a+b))        
                l = wyskokosc_padajaca_na_przeciwprostokatna(x, y)
                if l*3<=L:
                    RGB[j][i] = 0
                elif l<L:
                    RGB[j][i] = int((l/L)*255 - 256- 255/3)
        
    return RGB

data = np.zeros((100, 100, 3), dtype=np.uint8)
data.fill(255)

# przyklady
# plt.imshow(rysowanie(10, 40, 30, 20,2,data))
plt.imshow(linePZ(100, 100, [40, 20], [10,91],3,data))
# plt.imshow(linePZ(100, 100, [10, 20], [10,91],6,data))
# plt.imshow(linePZ(100, 100, [10, 20], [90,20],6,data))

m=10
n=10
# # test1
# data2 = np.zeros((m, n, 3), dtype=np.uint8)
# data2.fill(255)
# pukty_test = [[i,j] for i in range(-2,13,2) for j in range(-2,13,2)]
# print(pukty_test)
# for i in pukty_test:
#     for j in pukty_test:
#         data = linePZ(m, n, i, j,1,data2)
        
# plt.imshow(data)
 
# test2
# data2 = np.zeros((10, 10, 3), dtype=np.uint8)
# data2.fill(255)
# pukty_test = [[i,j] for i in range(-2,13,7) for j in range(-2,13,7)]
# for i in pukty_test:
#     for j in pukty_test:
#         data = linePZ(10, 10, i, j, 1, data2)
        
# plt.imshow(data2)
# print(pukty_test)

# for i in data2:
#     for j in i:
#         print(j)
        
# # test czasowy grubosci lini
# data3 = np.zeros((10, 10, 3), dtype=np.uint8)
# data3.fill(255)

# for i in range(1,11):
#     data3 = np.zeros((200, 200, 3), dtype=np.uint8)
#     data3.fill(255)
#     startT = time.time()
#     # time.sleep(0.001)
#     linePZ(200, 200, [1, 1], [199, 199], i, data3)
#     stopT = time.time()
#     print("Dla odcina o szerokosci: ", i," czas wykonania równa sie:",(stopT - startT)/200)
    
     