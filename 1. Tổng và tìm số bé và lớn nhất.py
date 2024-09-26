try:
  tep_dau_vao = open("./src/1_sum_min_max.inp", "r")

  list_hang_1 = [int(x) for x in tep_dau_vao.readline().split()]
  list_hang_2 = [int(x) for x in tep_dau_vao.readline().split()]
  
  with open("./build/1_sum_min_max.out", "w") as out:
    out.writelines([
      f"Tổng các dòng: {sum(list_hang_1)} | {sum(list_hang_2)}" + "\n",
      f"Trung bình cộng các dòng là: {sum(list_hang_1) / len(list_hang_1)} | {sum(list_hang_2) / len(list_hang_2)}" + "\n",
      f"Các số được sắp xếp: {sorted(list_hang_1)} | {sorted(list_hang_2)}" + "\n",
      f"Số lớn và bé nhất (bé/lớn): {min(list_hang_1)}/{max(list_hang_1)} | {min(list_hang_2)}/{max(list_hang_2)}"
    ])
except Exception as e:
  print(f"Đã có một lỗi xảy ra: {e}")