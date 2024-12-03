import math


input_file = open("./B47.inp", "r")
day_so = [int(x) for x in input_file.readline().split()]

def la_so_nguyen_to(n: int) -> bool:
  if n < 2:
    return False
  elif n == 2:
    return True
  for x in range(2, math.ceil(math.sqrt(n)) + 1):
    if n % x == 0:
      return False
  return True

def day_con_nguyen_to_tong_lon_nhat(day_so: list[int]) -> list[int]:
  cac_day_con: list[list[int]] = []
  for index in range(len(day_so)):
    day_con = []
    for x in day_so[index:]:
      if la_so_nguyen_to(x):
        day_con.append(x)
      else:
        break
    cac_day_con.append(day_con)
  cac_tong_day_con = [sum(x) for x in cac_day_con]

  return cac_day_con[cac_tong_day_con.index(max(cac_tong_day_con))]

print(" ".join([str(x) for x in day_con_nguyen_to_tong_lon_nhat(day_so)]))