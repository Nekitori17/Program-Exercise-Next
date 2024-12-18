from shlex import join


day_so = [int(x) for x in open("./B52.inp", "r").readline().split(", ")]

def day_con_tang_tien_hi_length(day_so: list[int]) -> list[int]:
  phan_tu_day_con: list[list[int]] = []
  for i in range(len(day_so)):
    cac_phan_tu_hien_tai = [day_so[i]]
    so_hien_tai = day_so[i]
    for so in day_so[i+1:]:
      if so > so_hien_tai:
        cac_phan_tu_hien_tai.append(so)
        so_hien_tai = so
    phan_tu_day_con.append(cac_phan_tu_hien_tai)

  return phan_tu_day_con[phan_tu_day_con.index(max(phan_tu_day_con, key=len))]

print(", ".join([str(x) for x in day_con_tang_tien_hi_length(day_so)]))