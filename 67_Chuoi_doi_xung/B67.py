from typing import TypedDict
chuoi_vao = open("./B67.inp", "r").readline()

class DauHieuDoiXung(TypedDict):
  le: list[int]
  chan: list[int]

def tim_dau_hieu_doi_xung(chuoi: str):
  dau_hieu_doi_xung: DauHieuDoiXung = {"le": [], "chan": []}

  for i in range(len(chuoi) - 1):
    if chuoi[i] == chuoi[i + 1]:
      dau_hieu_doi_xung["chan"].append(i)
    elif not i == len(chuoi) - 2:
      if chuoi[i] == chuoi[i + 2]:
        dau_hieu_doi_xung["le"].append(i + 1)

  return dau_hieu_doi_xung


def tim_chuoi_doi_xung_dai_nhat(chuoi: str) -> str:
  cac_dau_hieu = tim_dau_hieu_doi_xung(chuoi)
  cac_chuoi: list[str] = []

  for vi_tri_chan in cac_dau_hieu["chan"]:
    start = vi_tri_chan
    end = vi_tri_chan + 1
    while start > 0 and end < len(chuoi):
      if chuoi[start] == chuoi[end]:
        start -= 1
        end += 1
      else:
        break
    
    cac_chuoi.append(chuoi[start + 1:end])

  for vi_tri_le in cac_dau_hieu["le"]:
    start = vi_tri_le - 1
    end = vi_tri_le + 1
    while start > 0 and end < len(chuoi):
      if chuoi[start] == chuoi[end]:
        start -= 1
        end += 1
      else:
        break
    
    cac_chuoi.append(chuoi[start + 1:end])
   
  return max(cac_chuoi, key=len)


print(tim_chuoi_doi_xung_dai_nhat(chuoi_vao))