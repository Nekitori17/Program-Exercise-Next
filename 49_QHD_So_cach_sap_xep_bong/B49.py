import math

so_n_bong = int(open("./B49.inp").readline())

def so_to_hop_bong_khong_lien_tiep_bong_do(so_bong: int) -> int:
  return math.comb(2*so_bong, so_bong) - math.comb(2*so_bong, so_bong-1)

print(so_to_hop_bong_khong_lien_tiep_bong_do(so_n_bong))