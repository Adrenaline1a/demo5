#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = str(input("Введите первое предложение: "))
    b = str(input("Введите второе предложение: "))
    k=''
    s1=a.split()
    s2=b.split()
    for i in s1:
        if i not in s2:
            k+=i+" "
    for j in s2:
        if j not in s1:
            k+=j+" "
    print("Слова удовлетворяющие условию: ", k)

