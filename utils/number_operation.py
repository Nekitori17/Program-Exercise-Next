from typing import *

def kiem_tra_so_nt(so: int) -> bool:
  if so == 1:
    return False
  elif so == 2:
    return True
  else:
    for i in range(2, so):
        if so % i == 0:
            return False
  return True