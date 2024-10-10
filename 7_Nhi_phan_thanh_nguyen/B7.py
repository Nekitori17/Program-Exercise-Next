input_file = open("./B7.inp", "r");

day_so = [int(x) for x in input_file.readlines()]

def nhi_phan_thanh_nguyen(so) -> int:
  chuoi_so = str(so)
  he_so = 1
  tong = 0

  for index in range(len(chuoi_so) - 1, -1, -1):
    if chuoi_so[index] == "1":
      tong += he_so
    if he_so == 1:
      he_so = 2
    else:
      he_so *= 2
  return tong

with open("./B7.out", "w") as output_file:
  output_file.writelines([
    f"{"\n".join([str(y) for y in [nhi_phan_thanh_nguyen(x) for x in day_so]])}"
  ])