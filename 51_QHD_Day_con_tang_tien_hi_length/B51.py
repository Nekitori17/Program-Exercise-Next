day_so = [int(x) for x in open("./B51.inp", "r").readline().split(", ")]

def day_con_tang_tien_hi_length(day_so: list[int]) -> int:
  so_phan_tu_day_con: list[int] = []
  for i in range(len(day_so)):
    so_phan_tu_hien_tai = 1
    so_hien_tai = day_so[i]
    for so in day_so[i+1:]:
      if so > so_hien_tai:
        so_phan_tu_hien_tai += 1
        so_hien_tai = so
    so_phan_tu_day_con.append(so_phan_tu_hien_tai)

  return max(so_phan_tu_day_con)

print(day_con_tang_tien_hi_length(day_so))