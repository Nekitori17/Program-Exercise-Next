input_file = open("./main.inp", "r")

day_so = [int(x) for x in input_file.readlines()]

def nguyen_thanh_nhi_phan(n: int) -> int:
  if n == 0:
    return 0
  else:
    return n % 2 + 10 * nguyen_thanh_nhi_phan(n // 2)

with open("./main.out", "w") as output_file:
  output_file.writelines([
    f"So nhi phan: " + "\n" +
    f"{"\n".join([str(nguyen_thanh_nhi_phan(x)) for x in day_so])}"
  ])