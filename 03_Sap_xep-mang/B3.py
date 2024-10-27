input_file = open("./B3.inp", "r")

def sap_xep_so(mang: list[int]) -> list[int]:
  mang_copy = mang.copy()

  for index in range(len(mang_copy)):
    min_index = index
    for j in range(index + 1, len(mang_copy)):
      if mang_copy[j] < mang_copy[min_index]:
        min_index = j
    mang_copy[index], mang_copy[min_index] = mang_copy[min_index], mang_copy[index]

  return mang_copy

list_hang_1 = [int(x) for x in input_file.readline().split()]
list_hang_2 = [int(x) for x in input_file.readline().split()]

list_so_1 = sap_xep_so(list_hang_1)
list_so_2 = sap_xep_so(list_hang_2)

with open("./B3.out", "w") as output_file:
  output_file.write(f"{" ".join([str(x) for x in sap_xep_so(list_hang_1 + list_hang_2)])}")