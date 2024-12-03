import math

input_file = open("./B38.inp")
so_vao = int(input_file.readline())

def check_nguyen_to(so: int) -> bool:
  for x in range(2, math.ceil(math.sqrt(so)) + 1):
    if (so % x == 0):
      return False
  return True

def so_nguyen_to_doi_xung(den: int) -> int:
  cac_so_nguyen_to_doi_xung = [x for x in range(11, den) if check_nguyen_to(x) and x == int(str(x)[::-1])]
  return len(cac_so_nguyen_to_doi_xung)

print(so_nguyen_to_doi_xung(so_vao))