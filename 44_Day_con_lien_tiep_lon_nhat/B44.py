input_file = open("./B44.inp")
skipped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

def day_tang_tien_lon_nhat(day_so: list[int]) -> int:
  cac_day_tang_tien: list[list[int]] = []

  for index in range(len(day_so)):
    day_tang_tien = []
    for x in day_so[index:]:
      if x not in day_tang_tien:
        day_tang_tien.append(x)
      else:
        break
    cac_day_tang_tien.append(day_tang_tien)

  return max([len(x) for x in cac_day_tang_tien])

print(day_tang_tien_lon_nhat(day_so))