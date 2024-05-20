T = int(input())
wave = [0 for _ in range(101)]
wave[0]=1
wave[1]=1
wave[2]=1

for i in range(3, 101):
    wave[i] = wave[i-3] + wave[i-2]

for _ in range(T):
    N = int(input())
    print(wave[N-1])