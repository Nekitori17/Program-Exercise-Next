input_file = open("./B42.inp", "r")
skipped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

def binary_search_modded(arr: list[int], left: int, right: int, x: int) -> int:
  if right >= left:
    mid = (right + left) // 2

    if right - left <= 1:
      if arr[left] == x:
        return left
      else:
        return right
      
    elif arr[mid] < x:
      return binary_search_modded(arr, mid, right, x)
    else:
      return binary_search_modded(arr, left, mid, x)
    
  return -1

def tim_so_tang_tien_lon_nhat(day_so: list[int]) -> int:
  so_luong_ele_cac_day_con: list[int] = []

  for step in range(2, day_so[-1] + 1):
    cac_so = []
    for x in day_so:
      if x % step == 0:
        cac_so.append(x)
    so_luong_ele_cac_day_con.append(len(cac_so))
  
  return max(so_luong_ele_cac_day_con)
  

def day_toan_duong(day_so: list[int]) -> int:
  day_so.sort()
  so_duong_gan_nhat = binary_search_modded(day_so, 0, len(day_so) - 1, 0)
  day_toan_duong = day_so[so_duong_gan_nhat:]

  cac_so_duy_nhat = []
  for i in range(1, day_toan_duong[-1] + 1):
    if i in day_toan_duong:
      cac_so_duy_nhat.append(i)
    
  return tim_so_tang_tien_lon_nhat(cac_so_duy_nhat)

print(day_toan_duong(day_so))