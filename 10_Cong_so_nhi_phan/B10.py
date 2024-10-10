input_file = open("./B10.inp", "r")

day_so_nhi_phan = [int(x) for x in input_file.readline().split()]

def chuyen_nhi_phan(thap_phan: int) -> int:
  if thap_phan == 0:
    return 0
    
  tong = ""
  while thap_phan > 0:
    tong += str(thap_phan % 2)
    thap_phan //= 2

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

def cong_so_nhi_phan(a: int, b: int) -> int:
  return chuyen_nhi_phan(chuyen_thap_phan(a) + chuyen_thap_phan(b))

with open("./B10.out", "w") as output_file:
  output_file.writelines([
    str(cong_so_nhi_phan(day_so_nhi_phan[0], day_so_nhi_phan[1]))
  ])