#https://www.acmicpc.net/problem/10825
import sys
N=int(sys.stdin.readline())
students=[]
for _ in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    students.append([name, int(kor), int(eng), int(math)])

students.sort(key=lambda x:[-x[1],x[2],-x[3],x[0]])

for s in students:
    print(s[0])