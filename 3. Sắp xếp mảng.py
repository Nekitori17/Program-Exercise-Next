from utils.get_output import sap_xep_so

input_file = open("./src/3_sorting_int_list.inp", "r")

list_hang_1 = [int(x) for x in input_file.readline().split()]
list_hang_2 = [int(x) for x in input_file.readline().split()]



with open("./build/3_sorting_int_list.out", "w") as output_file:
  output_file.write(f"Danh sach duoc sap xep: {" ".join([str(x) for x in sap_xep_so(list_hang_1 + list_hang_2)])}")