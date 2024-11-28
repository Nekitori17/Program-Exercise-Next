import math

input_file = open("./B37.inp")
day_so_vao = [int(x) for x in input_file.readline().split()]

def check_nguyen_to(so: int) -> bool:
  for x in range(2,math.ceil(math.sqrt(so))):
    if (so % x == 0):
      return False
  return True

def tim_mat_khau(tu: int, den: int) -> list[int]:
  cac_so_da_giai = [x for x in range(tu, den + 1) if check_nguyen_to(x) and check_nguyen_to(sum([int(i) for i in str(x)]))]
  return cac_so_da_giai

print(" ".join([str(x) for x in tim_mat_khau(day_so_vao[0], day_so_vao[1])]))