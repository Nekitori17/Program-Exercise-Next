input_file = open("./B4.inp", "r")

so_vao = int(input_file.readline())

tong = 0

for so in range(so_vao + 1):
  if so % 5 == 4:
    tong += so

with open("./B4.out", "w") as output_file:
  output_file.write(f"{tong}")