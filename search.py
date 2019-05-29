#!/usr/bin/env python
# -*- coding: utf-8 -*-


def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, value):
    first=0
    last=len(data)-1
    while first <= last:
        middle = (first+last)//2
        if data[middle]==value:
            return middle
        elif data[middle] < value:
            first = middle + 1
        else:
            last = middle - 1
