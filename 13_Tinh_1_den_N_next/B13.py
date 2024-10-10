input_file = open("./B13.inp", "r")

so_vao = int(input_file.readline())

def tinh_t_den_n(so: int) -> int:
  return int((so * (so/2)) + so/2)

with open("./B13.out", "w") as output_file:
  output_file.write(str(tinh_t_den_n(so_vao)))