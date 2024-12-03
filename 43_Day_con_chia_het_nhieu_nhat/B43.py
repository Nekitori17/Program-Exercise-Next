input_file = open("./B43.inp", "r")
row_1 = [int(x) for x in input_file.readline().split()]
so_k = row_1[1]
day_so = [int(x) for x in input_file.readline().split()]

def day_con_chia_k_dai_nhat(day_so, so_k):
  cac_day_con_chia_k: list[list[int]] = []

  for index in range(len(day_so)):
    day_con = []
    for x in day_so[index:]:
      if x % so_k == 0:
        day_con.append(x)
      else:
        break
    cac_day_con_chia_k.append(day_con)

  return max([len(x) for x in cac_day_con_chia_k])

print(day_con_chia_k_dai_nhat(day_so, so_k))                           