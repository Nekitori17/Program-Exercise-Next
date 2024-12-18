input_file = open("./B64.inp", "r")
cac_ve = set([int(x) for x in input_file.readlines()])
day_du = set(range(min(cac_ve), max(cac_ve) + 1))

print("".join([str(x) for x in day_du.difference(cac_ve)]))