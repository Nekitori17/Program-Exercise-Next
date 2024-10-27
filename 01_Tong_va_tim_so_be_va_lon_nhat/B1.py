try:
  tep_dau_vao = open("./B1.inp", "r")

  list_hang_1 = [int(x) for x in tep_dau_vao.readline().split()]
  list_hang_2 = [int(x) for x in tep_dau_vao.readline().split()]
  
  with open("./B1.out", "w") as out:
    out.writelines([
      f"Tong cac dong: {sum(list_hang_1)} | {sum(list_hang_2)}" + "\n",
      f"Trung binh cong cac dong la: {sum(list_hang_1) / len(list_hang_1)} | {sum(list_hang_2) / len(list_hang_2)}" + "\n",
      f"Cac so duoc sap xep: {", ".join([str(x) for x in sorted(list_hang_1)])} | {", ".join([str(x) for x in sorted(list_hang_1)])}" + "\n",
      f"So lon va be nhat (be/lon): {min(list_hang_1)}/{max(list_hang_1)} | {min(list_hang_2)}/{max(list_hang_2)}"
    ])
except Exception as e:
  print(f"Đã có một lỗi xảy ra: {e}")