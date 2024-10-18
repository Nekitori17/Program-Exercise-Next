input_file = open("./B18.inp", "r")

khoang = [int(x) for x in input_file.readline().split()]

def tinh_tong_khoang(tu: int, den: int) -> int:
  tu += 1
  den+= 1
  return int(int(den*(den/2) + (den/2)) - int(tu*(tu/2) + (tu/2)))

with open("./B18.out", "w") as output_file:
    output_file.write(str(tinh_tong_khoang(khoang[0], khoang[1])))