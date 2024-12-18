input_file = open("./B68.inp", "r")
skipped = input_file.readline()
cac_gia_da_quy = [int(x) for x in input_file.readline().split()]

def trich_day_con(day_so_vao: list[int]) -> list[int]:
  day_da_trich: list[list[int]] = []

  def trich(day_so: list[int], pos: int, day_hien_tai: list[int]):
    if pos == len(day_so):
      day_da_trich.append(day_hien_tai)
    elif day_so[pos] > day_hien_tai[-1]:
      day_hien_tai.append(day_so[pos])
      trich(day_so, pos + 1, day_hien_tai)
    else:
      for so in day_hien_tai[::-1]:
        if day_so[pos] > so:
          day_hien_tai_next = [x for x in day_hien_tai[day_hien_tai.index(so):] if x < day_so[pos]]
          day_so_next = [x for x in day_so[day_so.index(so):pos] if x < day_so[pos]] + day_so[pos:]
          trich(day_so_next, 1, day_hien_tai_next)
      trich(day_so, pos + 1, day_hien_tai)

  for index in range(len(day_so_vao)):
    trich(day_so_vao[index:], 1, [day_so_vao[index]])
  
  return day_da_trich

print(max([sum(x) for x in trich_day_con(cac_gia_da_quy)]))
