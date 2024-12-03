input_file = open("./B45.inp")
skipped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

def day_tang_tien_lon_nhat(day_so: list[int]) -> int:
  cac_day_tang_tien: list[list[int]] = []

  for index in range(len(day_so)):
    day_tang_tien = []
    so_hien_tai = day_so[index]
    for x in day_so[index:]:
      if x >= so_hien_tai:
        day_tang_tien.append(x)
        so_hien_tai = x
      else:
        break
    cac_day_tang_tien.append(day_tang_tien)

  return max([len(x) for x in cac_day_tang_tien])

print(day_tang_tien_lon_nhat(day_so))