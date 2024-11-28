input_file = open("./B36.inp", "r")
cac_ve = [int(x) for x in input_file.readline().split()]
ngan_sach = int(input_file.readline())

def mua_ve(cac_ve: list[int], ngan_sach: int) -> list[int]:
  cac_ve_da_mua: list[int] = []
  cac_ve.sort()
  if cac_ve[0] > ngan_sach:
    return [-1]
  else:
    for ve in cac_ve:
      if ve <= ngan_sach:
        ngan_sach -= ve
        cac_ve_da_mua.append(ve)
      else:
        break
    return cac_ve_da_mua
  
with open("./B36.out", "w") as output_file:
  cac_ve_da_mua = mua_ve(cac_ve, ngan_sach)
  output_file.writelines([
    f"{" ".join([str(x) for x in cac_ve_da_mua])}" + "\n",
    str(sum(cac_ve_da_mua)) if cac_ve_da_mua != [-1] else ""
  ])