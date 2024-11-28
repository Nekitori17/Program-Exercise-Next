hop_chat = open("./B40.inp", "r").readline()
nguyen_to_hoa_hoc = {
  "h": 1,
  "o": 16,
  "n": 14,
  "c": 12
}

def phan_tich_hop_chat(hop_chat: str) -> list[tuple[str, int]]:
  cac_nguyen_to_str: list[str] = []
  cac_nguyen_to = []
  for index in range(len(hop_chat)):
    if hop_chat[index].isnumeric():
      continue
    elif not index + 1 > len(hop_chat) - 1 and hop_chat[index + 1].isnumeric():
      cac_nguyen_to_str.append(hop_chat[index] + hop_chat[index + 1])
    else:
      cac_nguyen_to_str.append(hop_chat[index])

  for nguyen_to in cac_nguyen_to_str:
    if len(nguyen_to) == 1:
      gia_tri_1: tuple[str, int] = (nguyen_to[0].lower(), 1)
      cac_nguyen_to.append(gia_tri_1)
    else:
      gia_tri_2: tuple[str, int] = (nguyen_to[0].lower(), int(nguyen_to[1]))
      cac_nguyen_to.append(gia_tri_2)
  
  return cac_nguyen_to

def tinh_khoi_luong_dvc(cac_chat: list[tuple[str, int]]) -> int:
  tong = 0
  for nguyen_to in cac_chat:
    tong += nguyen_to_hoa_hoc[nguyen_to[0]] * nguyen_to[1]
  
  return tong

print(tinh_khoi_luong_dvc(phan_tich_hop_chat(hop_chat)))