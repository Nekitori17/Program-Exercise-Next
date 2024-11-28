from operator import le


input_file = open("./B33.inp", "r")
so_vao = int(input_file.readline())
day_so = [int(x) for x in input_file.readline().split()]

def binary_search_modded(arr: list[int], left: int, right: int, x: int) -> int:
  if right >= left:
    mid = (right + left) // 2

    if arr[mid] == x:
      return mid
    elif right - left <= 1:
      if arr[right] <= x:
        return right
      elif arr[left] <= x:
        return left
      
    elif arr[mid] < x:
      return binary_search_modded(arr, mid, right, x)
    else:
      return binary_search_modded(arr, left, mid, x)
    
  return -1

def search_min_minius_result(day_so: list[int], so_vao: int) -> int:
  vi_tri = binary_search_modded(day_so, 0, len(day_so) - 1, so_vao)
  left = vi_tri
  right = vi_tri + 1

  if left >= 0 and right <= len(day_so) - 1:
    if abs(day_so[left] - so_vao) <= abs(day_so[right] - so_vao):
      return left
    else:
      return right
  else:
    if left == len(day_so) - 1:
      return left
    else:
      return -1
    
with open("./B33.out", "w") as output_file:
  output_file.write(str(search_min_minius_result(day_so, so_vao)))