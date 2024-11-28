input_file = open("./B32.inp", "r")
skipped = input_file.readline()
menh_gia_ve = [int(x) for x in input_file.readline().split()]
ngan_sach = [int(x) for x in input_file.readline().split()]

def binary_search_modded(arr: list[int], left: int, right: int, target: int) -> int:
  if right > left:
    mid = (right + left) // 2

    if right - left <= 1:
      if arr[right] <= target:
        return right
      elif arr[left] <= target:
        return left
      
    elif arr[mid] > target:
      return binary_search_modded(arr, left, mid, target)
    else:
      return binary_search_modded(arr, mid, right, target)
    
  return -1

def tickets_purchased(menh_gia_ve: list[int], ngan_sach: list[int]) -> list[int]:
  ve_da_mua: list[int] = []
  menh_gia_ve.sort()
  for tien in ngan_sach:
    ve_bi_mua = binary_search_modded(menh_gia_ve, 0, len(menh_gia_ve) - 1, tien)
    if not ve_bi_mua == -1:
      ve_da_mua.append(menh_gia_ve[ve_bi_mua])
      menh_gia_ve.remove(menh_gia_ve[ve_bi_mua])
    else:
      ve_da_mua.append(-1)

  return ve_da_mua

with open("./B32.out", "w") as output_file:
  output_file.write("\n".join([str(x) for x in tickets_purchased(menh_gia_ve, ngan_sach)]))
