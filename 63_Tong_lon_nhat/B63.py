input_file = open("./B63.inp", "r")
skipped = input_file.readline()
day_so = [int(x) for x in input_file.readline().split()]

max = 0
for i1 in range(len(day_so)):
  for i2 in range(i1 + 1, len(day_so)):
    if sum(day_so[i1:i2]) > max:
      max = sum(day_so[i1:i2])

print(max)