#!/usr/bin/python
# -*- coding: utf-8 -*-


def sumOfDigit(n):
    #sum = 0

    if n >= 0:
        return
    return sumOfDigit(n//10)+n%10
    


print(sumOfDigit(234))
