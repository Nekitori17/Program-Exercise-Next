input_file = open("./B22.inp", "r");
cac_dong = [x.split() for x in input_file.readlines()]
cap_so: list[list[int]] = []
for dong in cac_dong:
  cap_so.append([int(x) for x in dong])
cap_so.__delitem__(0)

def so_luong_boi(cap_so: list[int]) -> int:
  if cap_so[0] == cap_so[1]:
    return -1
  return cap_so[1] // cap_so[0]

with open("./B22.out", "w") as output_file:
  output_file.write("\n".join([str(so_luong_boi(x)) for x in cap_so]))