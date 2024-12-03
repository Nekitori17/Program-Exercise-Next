input_file = open("./B41.inp", "r")
skipped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

def tim_day_cung_so_lon_nhat(day_so: list[int]) -> int:
  cac_day_cung_so: list[list[int]] = []
  day_so.sort()

  for he_so in range(1, day_so[-1] + 1):
    day_cung_so: list[int] = []
    for so in day_so:
      if so == he_so:
        day_cung_so.append(so)
    cac_day_cung_so.append(day_cung_so)

  so_luong_ele_cac_day_con = [len(x) for x in cac_day_cung_so]
  return max(so_luong_ele_cac_day_con)

print(tim_day_cung_so_lon_nhat(day_so))