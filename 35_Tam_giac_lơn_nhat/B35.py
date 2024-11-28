import math

input_file = open("./B35.inp", "r")
diem_a = [float(x) for x in input_file.readline().split()]
cac_diem_bc = [float(x) for x in input_file.readline().split()]

def tinh_cac_canh(A: list[float], B: list[float], C: list[float]) -> list[float]:
  AB = math.sqrt(abs(B[0] - A[0])**2 + A[1]**2)
  BC = abs(C[0] - B[0])
  AC = math.sqrt((C[0] - A[0])**2 + A[1]**2)
  return [AB, BC, AC]

def to_hop_tam_giac(A: list[float], B_C: list[float]) -> list[list[list[float]]]:
  cac_tam_giac: list[list[list[float]]]= []
  for i in range(len(B_C)):
    if i == 0:
      cac_tam_giac.append([A, [0, 0], [B_C[i], 0]])
    else:
      cac_tam_giac.append([A, [B_C[i - 1], 0], [B_C[i], 0]])
  
  return cac_tam_giac

def tinh_tam_giac_max(A: list[float], B_C: list[float]) -> tuple[float, list[int | float]]:
  cac_tam_giac = to_hop_tam_giac(A, B_C)
  cac_dien_tich_tam_giac: list[float] = []
  for tam_giac in cac_tam_giac:
    cac_canh_tam_giac = tinh_cac_canh(A, tam_giac[1], tam_giac[2])
    p = cac_canh_tam_giac[0] + cac_canh_tam_giac[1] + cac_canh_tam_giac[2]
    s = math.sqrt((p - cac_canh_tam_giac[0]) * (p - cac_canh_tam_giac[1]) * (p - cac_canh_tam_giac[2]))
    cac_dien_tich_tam_giac.append(s)
  
  max_dientich = max(cac_dien_tich_tam_giac)
  index = cac_dien_tich_tam_giac.index(max_dientich)
  print(index)
  # return round(max_dientich, 2), [float(x) if x % 1 != 0 else int(x) for x in cac_tam_giac[index][2]]
  return round(max_dientich, 2), [index, 0]


with open("./B35.out", "w") as output_file:
  ket_qua = tinh_tam_giac_max(diem_a, cac_diem_bc)
  output_file.writelines([
    str(ket_qua[0]) + "\n",
    " ".join([str(x) for x in ket_qua[1]])
  ])