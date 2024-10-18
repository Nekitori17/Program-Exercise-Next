from typing import *

tep_vao = open("./B16.inp", "r")
day_so = [int(x) for x in tep_vao.readline().split()]
can_dat = int(tep_vao.readline())

def tim_tong_2_vi_tri(day_vao: List[int], can_dat: int) -> Tuple[int, int] | str:
  for so in day_so:
    for vi_tri in range(day_so.index(so) + 1, len(day_so) - 1):
      if so + day_so[vi_tri] == can_dat:
        return day_so.index(so), vi_tri
  return "No"

with open("./B16.out", "w") as output_file:
  output_file.write(" ".join([str(x) for x in tim_tong_2_vi_tri(day_so, can_dat)]))
                                    