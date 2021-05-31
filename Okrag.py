# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#Zadanie 2 Okrąg metodą Breshenhama\
    
def rysuj( xc, yc, i, y, RGB):
    # RGB[xc+i][yc+y] = 0
    # RGB[xc-i][yc+y] = 0
    # RGB[xc+i][yc-y] = 0
    # RGB[xc-i][yc-y] = 0
    # RGB[xc+i][yc+y] = 0
    # RGB[xc-i][yc+y] = 0
    # RGB[xc+i][yc-y] = 0
    # RGB[xc-i][yc-y] = 0
    xs = [xc+i,xc-i,xc+i,xc-i,xc+i,xc-i,xc+i,xc-i]
    ys = [yc+y,yc+y,yc-y,yc-y,yc+y,yc+y,yc-y,yc-y]
    for i in range(len(xs)):
        if xs[i] > 0 and ys[i] > 0 and xs[i]<200 and ys[i]<200:
            RGB[xs[i]][ys[i]] = 0
            
    return RGB
    


def okrag_bershenhama(xc, yc, r):
    RGB = np.zeros((200, 200, 3), dtype = np.uint8)
    RGB.fill(255)
    
    
    d = 3 - 2*r
    y = r
    i = 0
    
    rysuj( xc, yc, i, y, RGB)
    
    while i <= y :
        i += 1
        
        if (d>0):
            y-=1
            d = d + 4 * (i - y) + 10
            
        else:
            d = d + i*4 + 6
            
        rysuj( xc, yc, i, y, RGB)
        rysuj( xc, yc, y, i, RGB)
    return RGB

data = okrag_bershenhama(190, 180, 80)
plt.imshow(data, interpolation='none', aspect=1)
plt.show()
plt.imsave('test.png', data, format='png')
        
        
