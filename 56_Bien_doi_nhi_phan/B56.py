input_file = open("./B56.inp")
skipped = input_file.readline()
day_nhi_phan = [int(x) for x in input_file.readline().split()]

class BienDoiNhiPhan:
  def __init__(self, binary_arr: list[int]):
    self.binary_arr: list[int] = binary_arr
  
  def not_nhi_phan(self, binary: list[int]):
    da_not: list[int] = []
    for i in binary:
      if i == 0:
        da_not.append(1)
      else:
        da_not.append(0)
    return da_not

  def __call__(self):

    cac_day_da_dich: list[list[int]] = []
    for i1 in range(len(self.binary_arr) + 1):
      for i2 in range(i1 + 1, len(self.binary_arr) + 1):
        day_con_hien_tai = self.binary_arr[i1:i2]
        
        if i1 == 0 and i2 == len(self.binary_arr) + 1:
          cac_day_da_dich.append(self.not_nhi_phan(day_con_hien_tai))
        elif i1 == 0:
          cac_day_da_dich.append(self.not_nhi_phan(day_con_hien_tai) + self.binary_arr[i2:])
        elif i2 == len(self.binary_arr) + 1:
          cac_day_da_dich.append(self.binary_arr[:i1] + self.not_nhi_phan(day_con_hien_tai))
        else:
          cac_day_da_dich.append(self.binary_arr[:i1] + self.not_nhi_phan(day_con_hien_tai) + self.binary_arr[i2:])
    dem_so_1 = []
    for day_da_dich in cac_day_da_dich:
      dem_so_1.append(day_da_dich.count(1))
        
    return max(dem_so_1)


print(BienDoiNhiPhan(day_nhi_phan)())