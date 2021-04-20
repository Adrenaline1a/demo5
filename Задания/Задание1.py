#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    f=''
    a=str(input("Введите предложение: "))
    p=0
    i=1
    while (i<=len(a) and p==0):
        if a[i]==',':
            p=i
        else:
            i=i+1
        if p==0:
            print("В предложении нет запятой")
            exit(1)
        elif p==1:
            print("Запятая первый символ в строке")
            exit(2)
        else:
            i=1
            while a[i]!=',':
                f+=a[i]
    print(f)
    exit(3)

