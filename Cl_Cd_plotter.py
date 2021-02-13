# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/3 20:21
@Author  : Junfei Sun
@Email   : sjf2002@sohu.com
@File    : Cl_Cd_plotter.py
'''

import matplotlib.pyplot as plt
Re=input('renolds number')
while True:
    filej=input('Do you want to input a new file?[y/n]')
    if filej=='y':
        note=input('note')
        name=input('airfoil name')
        file_name=input('please input your file name')
        f=open(file_name,'r')
        data=f.readlines()
        f.close()
        counter=0
        xcoord=[]
        ycoord=[]
        for line in data:
            counter+=1
            line=line.strip()
            line = line.strip('\n')
            line=line.split(' ')
            for i in range(line.count('')):
                line.remove('')
            if counter>=13:
                ycoord.append(float(line[1])/float(line[2]))
                xcoord.append(float(line[0]))
        plt.plot(xcoord, ycoord, '-%s'%note, label=name+',Re=%s'%Re)
    else:
        break
plt.xlabel('α(°)')
plt.ylabel('Cl/Cd')
plt.legend(loc=1)
plt.title('Cl/Cd-α graph')
plt.show()