input_file = open("./B30.inp", "r")
ma_tran_tho = [x.split() for x in input_file.readlines()]
ma_tran = []
so_can_tim = int(ma_tran_tho.pop()[0])
for hang_ma_tran in ma_tran_tho:
  ma_tran.append([int(x) for x in hang_ma_tran])

def binary_search_modded(arr: list[int], left: int, right: int, x: int) -> int:
  if right >= left:
    mid = (right + left) // 2

    if right - left <= 1:
      if arr[left] == x:
        return left
      elif arr[right] == x:
        return right
      else:
        return mid - 1  
        
    elif arr[mid] > x:
      return binary_search_modded(arr, mid + 1, right, x)
    else:
      return binary_search_modded(arr, left, mid - 1, x)
    
  return -1

def binary_search(arr: list[int], left: int, right: int, x: int) -> int:
  if right >= left:
    mid = (right + left) // 2

    if arr[mid] == x:
      return mid     
    elif arr[mid] < x:
      return binary_search(arr, mid + 1, right, x)
    else:
      return binary_search(arr, left, mid - 1, x)
    
  return -1



def tim_ma_tran(ma_tran: list[list[int]], so_can_tim: int) -> tuple[int, int]:
  day_tan_cung = [x[-1] for x in ma_tran]
  hang_xac_dinh = binary_search_modded(day_tan_cung, 0, len(day_tan_cung) - 1, so_can_tim)
  print(hang_xac_dinh, ma_tran[hang_xac_dinh])
  cot_xac_dinh = binary_search(ma_tran[hang_xac_dinh], 0, len(ma_tran[0]) - 1, so_can_tim)

  if cot_xac_dinh == -1:
    return -1, -1
  else:
    return hang_xac_dinh, cot_xac_dinh
  
with open("./B30.out", "w") as output_file:
  output_file.write(" ".join([str(x) for x in tim_ma_tran(ma_tran, so_can_tim)]))