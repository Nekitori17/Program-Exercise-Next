input_file = open("./B19.inp", "r")
day_so = [int(x) for x in input_file.readlines()]
 
def tim_so_mat(list_so: list[int]) -> int:
  so_mat = 0
     
  for so in range(min(list_so), max(list_so)):
    if so not in list_so and so > so_mat:
      so_mat = so
  return so_mat

with open("./B19.out", "w") as output_file:
    output_file.write(str(tim_so_mat(day_so)))