so_vao = int(open("./B21.inp", "r").readline())

with open("./B21.out", "w") as output_file:
  output_file.write(f"{pow(2, so_vao - 1)}")