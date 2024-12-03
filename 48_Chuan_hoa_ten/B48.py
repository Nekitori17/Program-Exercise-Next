chuoi_vao = open("./B48.inp", "r").readline()

def chuan_hoa_ten(chuoi: str) -> str:
  chuoi_da_chuan_hoa: list[str] = []
  for chu in chuoi.split(" "):
    if not chu.isspace():
      chuoi_da_chuan_hoa.append(chu[0].upper() + "".join([x.lower() for x in chu[1:] if x.isalpha()]))
  return " ".join(chuoi_da_chuan_hoa)

print(chuan_hoa_ten(chuoi_vao))