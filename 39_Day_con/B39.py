input_file = open("./B39.inp")
skiped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

def day_con(day_chinh: list[int]) -> tuple[int, int]:
  day_chinh.sort()
  tong_le = 0
  for x in day_chinh:
    if x > 0 and x % 2 != 0:
      tong_le += x

  tong_day_con_co_buoc = []
  for step in range(2, day_chinh[-1]):
    cac_so = []
    for x in day_chinh:
      if x % step == 0:
        cac_so.append(x)
    tong_day_con_co_buoc.append(len(cac_so))

  return tong_le, max(tong_day_con_co_buoc)

print("\n".join([str(x) for x in day_con(day_so)]))