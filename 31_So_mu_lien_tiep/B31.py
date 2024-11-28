so_vao = int(open("./B31.inp").readline())

with open("./B31.out", "w") as output_file:
  output_file.write(f"{(so_vao * (so_vao + 1) * (2 * so_vao + 1)) // 6}")