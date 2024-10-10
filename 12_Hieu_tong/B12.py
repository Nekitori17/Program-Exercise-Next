so_vao = int(open("./B12.inp", "r").readline())

def tinh_tong_hieu(so: int) -> int:
    return int(-((so+1)/2)) if (so+1) % 2 == 0 else int((so+2)/2)

with open("./B12.out", "w") as output_file:
    output_file.write(str(tinh_tong_hieu(so_vao)))

print(tinh_tong_hieu(5))