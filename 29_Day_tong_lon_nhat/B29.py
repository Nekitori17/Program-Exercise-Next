input_file = open("./B29.inp", "r")
day_so = [int(x) for x in input_file.readline().split()]

def day_con_lon_nhat(day_so: list[int]) -> list[int]:
  day_lon_nhat: list[int] = []
  so_lon_nhat = sum(day_so)
  day_con: list[int] = []
  tong_day_con = 0

  for vi_tri in range(len(day_so)):
    for index in range(vi_tri, len(day_so)):
      cache = tong_day_con + day_so[index]
      if cache <= so_lon_nhat and cache < tong_day_con:
        break

      day_con.append(day_so[index])
      tong_day_con += day_so[index]
    
    if tong_day_con > so_lon_nhat:
      so_lon_nhat = tong_day_con
      day_lon_nhat = day_con

    tong_day_con = 0
    day_con = []
  return day_lon_nhat

with open("./B29.out", "w") as output_file:
  output_file.write(" ".join([str(x) for x in day_con_lon_nhat(day_so)]))