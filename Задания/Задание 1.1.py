#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a=str(input("Введите предложение: "))
    d=a.find(',')
    if d==-1:
        print('Запятых нет')
        exit(1)
    elif d==0:
        print("Запятая на первой позиции")
        exit(2)
    else:
        for i in range(d):
            s=a.split(',')
            c=s[0]
        print("Символы до первой запятой: ", c)
        exit(3)