from typing import *
import math

khoang_so = [int(x) for x in open("./B15.inp", "r").readline().split()]

def kiem_tra_so_nguyen_to(so: int) -> bool:
  if so == 1:
    return False
  if so == 2:
    return True
  for i in range(2, math.ceil(so**0.5) + 1):
    if so % i == 0:
      return False
  return True

def lay_khoang_nt(tu: int, den: int) -> List[int]:
  danh_sach_nt = []
  for i in range(tu, den + 1):
    if kiem_tra_so_nguyen_to(i):
      danh_sach_nt.append(i)
  return danh_sach_nt

with open('./B15.out', "w") as output_file:
  output_file.write(f"{len(lay_khoang_nt(khoang_so[0], khoang_so[1]))}")