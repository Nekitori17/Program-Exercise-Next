input_file = open("./B9.inp", "r")

day_so_nhi_phan = [int(x) for x in input_file.readline().split()]
day_so_thap_phan = [int(x) for x in input_file.readline().split()]

def chuyen_nhi_phan(thap_phan: int) -> int:
  if thap_phan == 0:
    return 0
    
  thap_phan_copy = thap_phan
  tong = ""

  while thap_phan_copy > 0:
    tong += str(thap_phan_copy % 2)
    thap_phan_copy //= 2

  return int(tong[::-1])


def chuyen_thap_phan(nhi_phan: int) -> int:
  if nhi_phan == 0:
    return 0
  
  tong = 0
  he_so = 1
  for index in range(len(str(nhi_phan)) - 1, -1, -1):
    if str(nhi_phan)[index] == "1":
      tong += he_so
    if he_so == 1:
      he_so = 2
    else:
      he_so *= 2
  return tong

with open("./B9.out", "w") as output_file:
  output_file.writelines([
    f"> Day so nhi phan: " + "\n" +
    f"{"\n".join([str(chuyen_thap_phan(x)) for x in day_so_nhi_phan])}" + "\n",
    f"> Day so thap phan: " + "\n" +
    f"{"\n".join([str(chuyen_nhi_phan(x)) for x in day_so_thap_phan])}"
  ])
