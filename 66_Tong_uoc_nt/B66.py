import math

so_vao = int(open("./B66.inp", "r").readline())

def kiem_tra_nt(n: int) -> bool:
  if n < 2:
    return False
  elif n == 2:
    return True
  for x in range(2, math.ceil(math.sqrt(n)) + 1):
    if n % x == 0:
      return False
  return True

def tim_tong_uoc_nt(n: int) -> int:
  cac_uoc: list[int] = []
  for x in range(2, int(n**0.5) + 1):
    if n % x == 0:
      cac_uoc.append(x)
      cac_uoc.append(n // x)
  return sum([x for x in cac_uoc if kiem_tra_nt(x)])

print(tim_tong_uoc_nt(so_vao))