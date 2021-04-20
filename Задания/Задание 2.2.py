#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a=str(input("Введите слово: "))
    s=a.split()
    if len(s)>=2:
        print("Введите одно слово")
        exit(1)
    else:
        b=len(a)
        if b%2!=0:
            print("Колличество букв в слове нечётное")
            exit(2)
        else:
            r = ''
            for i in range(0, len(a), 2):
                r += a[i + 1] + a[i]
            a = r
        print("Результат работы программы: ", a)