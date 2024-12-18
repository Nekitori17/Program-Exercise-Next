import math

input_file = open("./TONG.inp", "r")
skipped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

def check(so: int) -> bool:
  tong = sum([int(x) for x in str(so)])
  if tong == 2:
    return True
  elif tong <= 2:
    return False
  else:
    for i in range(2, int(math.sqrt(tong)) + 1):
      if tong % i == 0:
        return False
    return True

print(sum([so for so in day_so if not check(so)]))