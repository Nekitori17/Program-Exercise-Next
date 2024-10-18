import string

bang_chu_cai = string.printable[10:36]*2

input_file = open("./B17.inp", "r")
dong_vao = input_file.readline()
do_dich_chuyen = int(input_file.readline())

def giai_ma_tin(chuoi: str, dich_chuyen: int) -> tuple[int, str]:
  da_chuan_hoa = [x for x in chuoi.split("#") if not x.isspace()]

  vi_tri_nhieu_nhat = 0
  for index in range(len(da_chuan_hoa)):
    if len(da_chuan_hoa[index]) > len(da_chuan_hoa[vi_tri_nhieu_nhat]):
      vi_tri_nhieu_nhat = index
    
  chuoi_da_giai = ""
  for chu in da_chuan_hoa[vi_tri_nhieu_nhat]:
    if chu.lower() in bang_chu_cai:
      chuoi_da_giai += bang_chu_cai[bang_chu_cai.index(chu.lower()) - dich_chuyen]
    
  return len(da_chuan_hoa), chuoi_da_giai

with open("./B17.out", "w") as output_file:
  output_file.writelines([
    "\n".join([str(x) for x in giai_ma_tin(dong_vao, do_dich_chuyen)])
  ])