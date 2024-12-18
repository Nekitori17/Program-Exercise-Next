cac_thanh_sat = [int(x) for x in open("./B53.inp").readline().split()]

def tinh_dien_tich_max(cac_thanh: list[int]) -> int:
  cac_thanh.sort()
  return cac_thanh[0] * cac_thanh[2]

print(tinh_dien_tich_max(cac_thanh_sat))
