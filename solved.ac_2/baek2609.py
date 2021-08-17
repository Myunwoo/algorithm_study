#https://www.acmicpc.net/problem/2609
A,B=map(int, input().split())
b,a=A,B

#서로 나눈 나머지로 각자의 값을 바꿔줌(0이 되지 않는 동안)
while b != 0:
    a = a % b
    a, b = b, a

print(a)

print(A*B//a)