menh_gia_goc = 300000
menh_gia_20 = menh_gia_goc * 0.2
menh_gia_50 = menh_gia_goc * 0.5
menh_gia_80 = menh_gia_goc * 0.8
input_file = open("./B55.inp", "r")
skipped = input_file.readline()
cac_khach_hang = [int(x) for x in input_file.readline().split()]

def tinh_doanh_thu(khach_hang: list[int]) -> float:
  doanh_thu = 0.0
  for tuoi in khach_hang:
    match tuoi:
      case tuoi if tuoi <= 5:
        continue
      case tuoi if tuoi <= 10:
        doanh_thu += menh_gia_20
        continue
      case tuoi if tuoi <= 15:
        doanh_thu += menh_gia_50
        continue
      case tuoi if tuoi >= 60:
        doanh_thu += menh_gia_80
        continue
      case _:
        doanh_thu += menh_gia_goc
  
  return doanh_thu

print(int(tinh_doanh_thu(cac_khach_hang)))