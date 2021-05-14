#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = str(input("Введите фразу: "))
    s = 0
    a = list(a)
    for i in a:
        if i.isdigit():
            s += int(i)
    if s == 0:
        print("Чисел нет")
        exit(2)
    else:
        print(s)
        exit(1)
