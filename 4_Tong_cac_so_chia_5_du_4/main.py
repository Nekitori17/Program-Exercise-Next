input_file = open("./main.inp", "r")

so_vao = int(input_file.readline())

tong = 0

for so in range(so_vao + 1):
  if so % 5 == 4:
    tong += so

with open("./main.out", "w") as output_file:
  output_file.write(f"Tong cac so chia 5 du 4: {tong}")