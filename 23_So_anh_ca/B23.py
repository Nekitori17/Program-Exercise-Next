input_file = open("./B23.inp", "r")
danh_sach_so = [x for x in str(input_file.readline())]
print(danh_sach_so)

def sap_xep_lon_nhat(list_so: list[int]) -> list[int]:
  list_so.sort(reverse=True)
  return list_so

with open("./B23.out", "w") as output_file:
  output_file.write("".join([str(x) for x in sap_xep_lon_nhat([int(x) for x in danh_sach_so])]))