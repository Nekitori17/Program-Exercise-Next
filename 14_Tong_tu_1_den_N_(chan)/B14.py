so_vao = int(open("./B14.inp", "r").readline())

def tong_tu_1_den_N_chan(so: int) -> int:
  if so == 0 or so == 2:
    return 0
  return int((so * (so - 2)) / 4)

with open("./B14.out", "w") as output_file:
  output_file.write(f"{tong_tu_1_den_N_chan(so_vao)}")