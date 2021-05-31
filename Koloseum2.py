# -*- coding: utf-8 -*-
from IPython.display import display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


path=r"D:\grafika_zadania\Koloseum.png"
img = Image.open(path)

# display(img)

arr = np.array(img)
arr.shape

def splot(RGB, Mf):
    r = int(len(Mf)/2) 
    nr = 0
    for i in range(len(Mf)):
        for j in range(len(Mf[0])): 
            nr += Mf[i][j]
    nr = max(nr, 1)
    przyciecie = Mf.shape[0]//2
    for i in range(przyciecie):
        RGB = zabezpieczenie_przed_ramka(RGB)
    RGB2 = np.zeros((len(RGB), len(RGB[0]),3), dtype=np.uint8,)
    for x in range(r, len(RGB)-r):  
        for y in range(r, len(RGB[0])-r):
            tmp = np.zeros(3) 
            for i in range(len(Mf)):  
                for j in range(len(Mf[0])): 
                    tmp += RGB[x-r+i][y-r+j]*Mf[i][j]                        
            tmp = abs(tmp) 
            tmp /= nr  
            tmp = np.array([i if  i <255 else 255 for i in tmp])
            RGB2[x][y] = tmp
    for i in range(przyciecie):
        RGB2 = np.delete(RGB2, (0,len(RGB2[0])-1),1)
    return RGB2[przyciecie:-przyciecie]

def RGBtoGSmax(RGB):
    h = len(RGB)
    w = len(RGB[0])
    RGB2 = np.zeros((h, w,3), dtype=np.uint8)
    for i in range(0, h):
        for j in range(0, w):
            RGB2[i][j] = max(RGB[i][j][0],RGB[i][j][1],RGB[i][j][2])
    return RGB2

def zabezpieczenie_przed_ramka(RGB):
    h = len(RGB)+2
    w = len(RGB[0])+2
    RGB2 = np.zeros((h, w,3), dtype=np.uint8)
    for i in range(1, h-1):
        for j in range(1, w-1):
            if (j==1):
                RGB2[i][j-1] = RGB[i-1][j-1]
                RGB2[i][j] = RGB[i-1][j-1]
            elif (j==w-2):
                
                RGB2[i][j+1] = RGB[i-1][j-1]
                RGB2[i][j] = RGB[i-1][j-1]
            elif (i==1):
                RGB2[i-1][j] = RGB[i-1][j-1]
                RGB2[i][j] = RGB[i-1][j-1]
            elif (i==h-2):
                RGB2[i+1][j] = RGB[i-1][j-1]   
                RGB2[i][j] = RGB[i-1][j-1] 
            else:
                RGB2[i][j] = RGB[i-1][j-1]
    RGB2[0][0] = RGB[1][1] 
    RGB2[0][w-1] = RGB[1][w-3] 
    RGB2[h-1][0] = RGB[h-3][1] 
    RGB2[h-1][w-1] = RGB[h-3][w-3] 
    return RGB2


def make_filrt_gaussa(n, sigma):
    assert n%2!=0 and n>2
    matrx = np.zeros((n,n))     
    max_power = sigma**(n//2+2)
    half = n//2
    matrx.fill(max_power)
    if sigma<1:
        for i in range(n):
            for j in range(n):
                matrx[i][j] = 1 - sigma**(n - abs(half-i) - abs(half-j)-1) 
    else:
        for i in range(n):
            for j in range(n):
                matrx[i][j] = sigma**(n - abs(half-i) - abs(half-j)-1) 
    return matrx
print(make_filrt_gaussa(5,3))

def smoothGauss(RGB, sigma, r):
    assert r<12
    RGB2 = np.zeros((len(RGB), len(RGB[0]),3), dtype=np.uint8)
    RGB3 = RGBtoGSmax(RGB)
    gauss_filetr = make_filrt_gaussa(2*r+1, sigma)
    gauss = RGBtoGSmax(splot(RGB3, gauss_filetr)) 
    return gauss

# arr1 = smoothGauss(arr,0.5,4)
arr1 = smoothGauss(arr,2,2)
img1 = Image.fromarray(arr1, 'RGB')
img1.show()
display(img1)