from typing import *

input_file = open("./B5.inp", "r");

ma_tran_tho = [x.split() for x in input_file.readlines()]
ma_tran = []
for hang_ma_tran in ma_tran_tho:
  ma_tran.append([int(x) for x in hang_ma_tran])

def tinh_duong_cheo(ma_tran: List[List[int]]) -> Tuple[int, int]:
  tong_cheo_1 = 0
  tong_cheo_2 = 0
  cot = 0

  for hang in ma_tran:
    tong_cheo_1 += hang[cot]
    cot += 1

  cot = len(ma_tran) - 1

  for hang in ma_tran:
    tong_cheo_2 += hang[cot]
    cot -= 1

  return tong_cheo_1, tong_cheo_2

tong_cac_duong_cheo = tinh_duong_cheo(ma_tran)

with open("./B5.out", "w") as output_file:
  output_file.writelines([
    f"{tong_cac_duong_cheo[0]}" + "\n",
    f"{tong_cac_duong_cheo[1]}"
])