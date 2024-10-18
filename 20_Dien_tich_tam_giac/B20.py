input_file = open("./B20.inp")
cac_cap_diem_tho = [x.split() for x in input_file.readlines()]
cap_diem = []
for cap_diem_tho in cac_cap_diem_tho:
    cap_diem.append([int(x) for x in cap_diem_tho])

def dien_tich_tam_giac(diem1: tuple[int, int], diem2: tuple[int, int], diem3: tuple[int, int]) -> float:
    if diem1[0] == diem2[0] == diem3[0] or diem1[1] == diem2[1] == diem3[1]:
        return 0
    return abs((diem1[0] * (diem2[1] - diem3[1]) + diem2[0] * (diem3[1] - diem1[1]) + diem3[0] * (diem1[1] - diem2[1])) / 2.0)

    
dttg = dien_tich_tam_giac(cap_diem[0], cap_diem[1], cap_diem[2])
with open("./B20.out", "w") as output_file:
   output_file.write(str(dttg) if dttg else "No")