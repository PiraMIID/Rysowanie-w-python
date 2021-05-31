from IPython.display import display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


def splot(RGB, Mf):
    r = int(len(Mf)/2) 
    nr = 0
    for i in range(len(Mf)):
        for j in range(len(Mf[0])): 
            nr += Mf[i][j]
    print(nr)
    nr = max(nr, 1)
    print("rozmiar:", RGB.shape)
    RGB = zabezpieczenie_przed_ramka(RGB)
    print("wartość :", RGB[225][641])
    RGB2 = np.zeros((len(RGB), len(RGB[0]),3), dtype=np.uint8,)
    print("rozmiar:", RGB2.shape)
    for x in range(r, len(RGB)-r): 
        for y in range(r, len(RGB[0])-r):
            tmp = np.zeros(3) 
            for i in range(len(Mf)):  
                for j in range(len(Mf[0])): 
                    tmp += RGB[x-r+i][y-r+j]*Mf[i][j] 
                    
                
            tmp = abs(tmp) #bierze wartość absolutną sumy wyników 
            tmp /= nr  # dzili sie przez sumę elemętów macieży Mf
            tmp = np.array([i if  i <255 else 255 for i in tmp])
            RGB2[x][y] = tmp
    print("rozmiar:", len(RGB2[0]))
    RGB2 = np.delete(RGB2, (0,len(RGB2[0])-1),1)
    print("rozmiar:", len(RGB2[0]))
    print("rozmiar:", RGB2[0:-1].shape)
    return RGB2[1:-1]

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



def convolve_edge(RGB, type="P"):
    #black_white = 
    roberts = [[[0,1],[-1,0]],[[1,0],[0,-1]]]  #45 135
    prewitts = [[[-1,0,1],[-1,0,1],[-1,0,1]], [[1,1,1],[0,0,0],[-1,-1,-1]]] #0 90
    sobel =  [[[-1,-2,-1],[0,0,0],[1,2,1]],[[-2,-1,0],[-1,0,0],[0,1,2]],[[-1,0,1],[-2,0,2],[-1,0,1]],[[0,1,2],[-1,0,1],[-2,-1,0]]] #0 45 90 135
    RGB2 = np.zeros((len(RGB), len(RGB[0]),3), dtype=np.uint8)
    RGB3 = RGBtoGSmax(RGB)
    tmp = np.zeros(3, dtype=np.uint8)
    if type=="P":
        prewitt0 = RGBtoGSmax(splot(RGB3, prewitts[0])) 
        prewitt90 = RGBtoGSmax(splot(RGB3, prewitts[1])) 
        for i in range(len(prewitt0)):
            for j in range(len(prewitt0[0])):
                RGB2[i][j] = max(prewitt0[i][j][0] , prewitt90[i][j][1])
    elif type=="R":
        robert45 = RGBtoGSmax(splot(RGB3, roberts[0])) 
        robert135 = RGBtoGSmax(splot(RGB3, roberts[1])) 
        for i in range(len(robert45)):
            for j in range(len(robert45[0])):
                RGB2[i][j] = max(robert45[i][j][0] , robert135[i][j][1])
    elif type=="S":
        sobel0 = RGBtoGSmax(splot(RGB, sobel[0]))
        sobel45 = RGBtoGSmax(splot(RGB, sobel[2]))
        sobel90 = RGBtoGSmax(splot(RGB3, sobel[2]))
        sobel135 = RGBtoGSmax(splot(RGB3, sobel[3]))            
        for i in range(len(sobel0)):
            for j in range(len(sobel0[0])):
                RGB2[i][j] = max(sobel0[i][j][0] , sobel45[i][j][0],  sobel90[i][j][0] , sobel135[i][j][0])
    return RGB2


path=r"D:\grafika_zadania\Koloseum.png"
img = Image.open(path)

display(img)

arr = np.array(img)

arr1 = convolve_edge(arr, "S")
img1 = Image.fromarray(arr1, 'RGB')
img1.show()
display(img1)