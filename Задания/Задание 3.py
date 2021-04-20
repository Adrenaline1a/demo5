#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = str(input("Введите фразу: "))
    s = 0
    for i in range(len(a)):
        if a[i].isdigit():
            s += int(a[i])
    if s == 0:
        print("Чисел нет")
        exit(2)
    else:
        print(s)
        exit(1)