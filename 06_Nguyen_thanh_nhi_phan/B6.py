input_file = open("./B6.inp", "r")

day_so = [int(x) for x in input_file.readlines()]

def nguyen_thanh_nhi_phan(n: int) -> int:
  if n == 0:
    return 0
  else:
    return n % 2 + 10 * nguyen_thanh_nhi_phan(n // 2)

with open("./B6.out", "w") as output_file:
  output_file.writelines([
    f"{"\n".join([str(nguyen_thanh_nhi_phan(x)) for x in day_so])}"
  ])