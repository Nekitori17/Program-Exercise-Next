input_file = open("./B24.inp", "r")
cac_so_hang = [int(x) for x in input_file.readline().split()]

def tinh_tien_photo(cac_so_hang: list[int]) -> int:
  if cac_so_hang[2] < 100:
    return ((300 + (cac_so_hang[1] - 1) * 100) * (2 if cac_so_hang[0] == 3 else 1)) * cac_so_hang[2]
  else:
    return ((250 + (cac_so_hang[1] - 1) * 100) * (2 if cac_so_hang[0] == 3 else 1)) * cac_so_hang[2]

with open("./B24.out", "w") as output_file:
  output_file.write(f"{tinh_tien_photo(cac_so_hang)}")