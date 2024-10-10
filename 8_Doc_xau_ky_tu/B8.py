from typing import *

input_file = open("./B8.inp", "r")

chuoi = input_file.readline()
tong_so = 0

for chu in chuoi:
  if chu.isnumeric():
    tong_so += int(chu)

def chu_nhieu_nhat(chuoi: str) -> Tuple[str, int]:
  cache_chu = []
  nhieu_nhat: Tuple[str, int] = ("", 0)
  for chu in chuoi.lower():
    if chu not in cache_chu and chuoi.count(chu) > nhieu_nhat[1] and chu.isalpha():
      nhieu_nhat = (chu, chuoi.count(chu))
    cache_chu.append(chu)
  return nhieu_nhat

def co_the_doc_hoa(chuoi: str) -> str:
  day_chuoi = chuoi.split()
  day_chuoi_sau = []

  for chu in day_chuoi:
    if not chu.isspace():
      day_chuoi_sau.append(chu)
  return " ".join(day_chuoi_sau)

with open("./B8.out", "w") as output_file:
  output_file.writelines([
    f"{tong_so}" + "\n",
    f"{chu_nhieu_nhat(chuoi)[0]} xuat hien nhieu nhat: {chu_nhieu_nhat(chuoi)[1]} lan" + "\n",
    f"{co_the_doc_hoa(chuoi)}"
  ])