#https://www.acmicpc.net/problem/1085
import sys
x, y, w, h = map(int, input().split())

min_x = x
min_y = y

if (w/2) < x:
    min_x = w - x

if (h/2) < y:
    min_y = h - y

if min_x < min_y:
    print(min_x)
else:
    print(min_y)