chu_vao = open("./DEMSO.inp", "r").readline()

chuoi = ""
so_luong = 0
for chu in chu_vao:
  if chu.isnumeric():
    chuoi += "@"
    so_luong += 1
  else:
    chuoi += chu

print(so_luong)
print(chuoi)