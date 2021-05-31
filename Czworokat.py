# -*- coding: utf-8 -*-
import time
import numpy as np
import math
import matplotlib.pyplot as plt


def zaokraglij(x):
    return int(x+0.5)

def czy_przekatne_sie_przecinaja(P1, P2, P3, P4):
    #rownolegle
    if ((P1[1]==P3[1]and P2[0]==P4[0]) or (P1[0]==P3[0]and P2[1]==P4[1])):
        print("1")
        return True
    if ((P1[1]==P3[1]and P2[1]!=P4[1]) or (P1[0]==P3[0]and P2[0]!=P4[0])):
        print("2")
        return True
    if ((P1[1]!=P3[1]and P2[1]==P4[1]) or (P1[0]!=P3[0]and P2[0]==P4[0])):
        return True
    if ((P1[0]==P3[0] and P2[0]!=P4[0]) or (P1[0]!=P3[0]and P2[0]==P4[0])):
        return True
    if ((P1[0]==P3[0] and P2[0]==P4[0]) or (P1[0]==P3[0]and P2[0]==P4[0])):
        return True
    a13, b13 = ab(P1,P3)
    a24, b24 = ab(P2,P4)
    
    if((P2[0] * a13 + b13 <= P2[1] and P4[0] * a13 + b13 <= P4[1]) or (P2[0] * a13 + b13 >= P2[1] and P4[0] * a13 + b13 >= P4[1])):
            if((P1[0] * a24 + b24 <= P1[1] and P3[0] * a24 + b24 <= P3[1]) or (P1[0] * a24 + b24 >= P1[1] and P3[0] * a24 + b24 >= P3[1])):
                return False
    return True

def quadrilateral(m, n, P1, P2, P3, P4, fill=0):
   
    RGB = np.zeros((m, n, 3), dtype=np.uint8)
    RGB.fill(255)
    check = [P1, P2, P3, P4]
    lista_punktow = []
    for i in range(4):
        for j in range(4):
            if check[i]==check[j] and i!=j:
                return 0
    if (czy_przekatne_sie_przecinaja(P1, P2, P3, P4)!=True):
        return 0
 
    plista = [P1, P2, P3, P4]
    for i in range(3):
        if (plista[i][1] != plista[i+1][1]):
            lista_punktow+=punty_prostej(m, n, plista[i], plista[i+1])
    if (P4[0] != P1[0]):
        lista_punktow+=punty_prostej(m, n, P4, P1)
    lista_punktow = sorted(lista_punktow)
    if (fill==1):
        while i<len(lista_punktow)-1:
            start = math.ceil(lista_punktow[i][1])
            stop = math.floor(lista_punktow[i+1][1])
            for y in range(start if start > 0 else 0,stop if stop < m else m):
                RGB[int(lista_punktow[i][0])][y] = 0
            i+=2

    else:
        for i in lista_punktow:
            if (zaokraglij(i[1] >= 0) and zaokraglij(i[1])<m):
                RGB[i[0]][zaokraglij(i[1])]=0
        lista_punktow = []
        for i in range(4):
            plista[i][0], plista[i][1] = plista[i][1], plista[i][0]
        for i in range(3):
            if (plista[i][1] != plista[i+1][1]):
                lista_punktow+=punty_prostej(m, n, plista[i], plista[i+1])
        if (P4[0] != P1[0]):
            lista_punktow+=punty_prostej(m, n, P4, P1)
        for i in lista_punktow:
            if (zaokraglij(i[1] >= 0 and zaokraglij(i[1])<m)):
                RGB[zaokraglij(i[1])][i[0]]=0    
    return RGB
            
    
    
def ab(P1,P2):    
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    if x1>x2:
        x1,y1,x2,y2 = x2,y2,x1,y1
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    return a,b
    

def punty_prostej(m, n, P1, P2):
    x1, y1, x2, y2 = P1[0], P1[1], P2[0], P2[1]
    tablica_punktow =[]
    if (x1 == x2):
        for i in range(min(y1,y2) if min(y1,y2)>0 else 0, max(y1,y2) if max(y1,y2)<m else m):
            tablica_punktow.append([i,x1])
        return tablica_punktow
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    a, b = ab(P1, P2)
    for y in range(min(y1,y2) if min(y1,y2)>0 else 0, max(y1,y2) if max(y1,y2)<m else m):
        x = (y-b)/a
        tablica_punktow.append([y,x])

            
    return tablica_punktow

# P1, P2, P3, P4 = [10,10],[10,20],[10,0],[20,0]
# print(czy_przekatne_sie_przecinaja(P1, P2, P3, P4))
# P1, P2, P3, P4 = [10,20],[20,30],[20,10],[30,20]
# print(czy_przekatne_sie_przecinaja(P1, P2, P3, P4))
# P1, P2, P3, P4 = [20,30],[30,20],[10,20],[10,10]
# print(czy_przekatne_sie_przecinaja(P1, P2, P3, P4))


# P1, P2, P3, P4 = [50,1],[10,90],[50,5],[90,90]
# data = quadrilateral(100, 100 ,P1, P2, P3, P4, 0)

# P1, P2, P3, P4 = [1,50],[10,1],[10,51],[90,90]
# data = quadrilateral(100, 100 ,P1, P2, P3, P4, 1)

P1, P2, P3, P4 = [1,1],[10,77],[80,60],[74,10]
data = quadrilateral(100, 100 ,P1, P2, P3, P4, 0)

# # print(data)
    
plt.imshow(data)

# # testy
# data2 = np.zeros((10, 10, 3), dtype=np.uint8)
# data2.fill(255)
# pukty_test = [[i,j] for i in range(-2,13,7) for j in range(-2,13,7)]
# for i in pukty_test:
#     for j in pukty_test:
#         for z in pukty_test:
#             for g in pukty_test:
#                 if(type(quadrilateral(m, n, i, j, z, g, 1))!=int):
#                     data2 = quadrilateral(m, n, i, j, z, g, 1)
#                     plt.imshow(data2)

                    
# print(type(data2))
# plt.imshow(data2)
                




