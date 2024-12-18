input_file = open("./B54.inp", "r")
xau = input_file.readline()
do_dai_so = int(input_file.readline())

def lay_so_tu_chuoi(chuoi: str, do_dai: int) -> int:
  cac_so_org = [int(x) for x in chuoi if x.isnumeric()]
  cac_so = cac_so_org.copy()
  cac_so_lon_nhat: dict[int, int] = {}

  for i in range(do_dai):
    if i > 0:
      so_lon_nhat = max(cac_so)
      cac_so_lon_nhat[len(cac_so_org) - 1 - cac_so_org[::-1].index(so_lon_nhat)] = so_lon_nhat
      cac_so.remove(so_lon_nhat)
    else: 
      so_lon_nhat = max(cac_so)
      cac_so_lon_nhat[cac_so_org.index(so_lon_nhat)] = so_lon_nhat
      cac_so.remove(so_lon_nhat)
    
  cac_so_lon_nhat_key = list(cac_so_lon_nhat.keys())
  cac_so_lon_nhat_key.sort()

  return int(str("".join([str(cac_so_lon_nhat[x]) for x in cac_so_lon_nhat_key])))

print(lay_so_tu_chuoi(xau, do_dai_so))