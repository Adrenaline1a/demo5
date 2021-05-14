#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = str(input("Введите слово: "))
    s = a.split()
    c = list(a)
    if len(s) >= 2:
        print("Введите одно слово")
        exit(1)
    else:
        b = len(a)
        if b % 2 != 0:
            print("Колличество букв в слове нечётное")
            exit(2)
        else:
            print(c)
            r = ''
            for i in enumerate(c, 0):
                j = i[0]
                if i[0] % 2 == 0:
                    r += a[j+1] + a[j]
            print("Результат работы программы: ", r)
