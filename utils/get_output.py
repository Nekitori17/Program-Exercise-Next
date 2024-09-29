from utils.fraction_operation import *
from typing import *
import re

def in_ra_phan_so(text: str, object: Tuple[int, int] | float, decimal: str = "/") -> None:
  if isinstance(object, tuple):
    print(str(text).format(f"{object[0]}{decimal}{object[1]}"))
  else:
    print(str(text).format(object))

def tuple_hay_so(so_bi_chia: int, so_chia: int) -> Tuple[int, int] | float:
  if so_bi_chia % so_chia != 0:
    return rut_gon(so_bi_chia, so_chia)
  else:
    return so_bi_chia / so_chia

_regex_phan_so = r"([+-]?\d+([+\-*/]\d+)*)\/([+-]?\d+([+\-*/]\d+)*)"

def phan_so_thanh_tuple(phan_so: str, regex: str = _regex_phan_so) -> Tuple[int, int] | None:
  fullmatch = re.fullmatch(regex, phan_so)
  if fullmatch:
    return eval(fullmatch.group(1)), eval(fullmatch.group(3))
  return None

def sap_xep_so(arr: List[int]) -> List[int]:
  array = arr.copy()

  for index in range(len(array)):
    min_index = index
    for j in range(index + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j
    array[index], array[min_index] = array[min_index], array[index]

  return array