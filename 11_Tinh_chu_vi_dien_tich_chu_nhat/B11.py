input_file = open("./B11.inp", "r")

list_diem = [int(x) for x in input_file.readline().split()]
a: tuple[int, int] = (list_diem[0], list_diem[1])
b: tuple[int, int] = (list_diem[2], list_diem[3])

def xac_dinh_chu_nhat(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | int:
  if a[0] == b[0] or a[1] == b[1]:
    return -1
  return (abs(a[0] - b[0]), abs(a[1] - b[1]))

def tinh_chu_vi(a: int, b: int) -> int:
  return 2 * (a + b)

def tinh_dien_tich(a: int, b: int) -> int:
  return a * b


chu_nhat = xac_dinh_chu_nhat(a, b)

with open("./B11.out", "w") as output_file:
  if chu_nhat == -1:
    output_file.write(str(chu_nhat))
  else:
    output_file.writelines([
      str(tinh_chu_vi(chu_nhat[0], chu_nhat[1])) + " ",
      str(tinh_dien_tich(chu_nhat[0], chu_nhat[1]))
    ])