nums = list(map(int, input().split()))

def GCD(a, b):
  while b:
    a, b = b, a%b
  return a

def LCM(a, b):
  return (a*b) // GCD(a, b)


print(GCD(nums[0], nums[1]), LCM(nums[0], nums[1]))