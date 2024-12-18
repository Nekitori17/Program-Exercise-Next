input_file = open("./DOLECH.inp", "r")
skipped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

print(max(day_so) - min(day_so))