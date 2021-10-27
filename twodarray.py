r1 = int(input("How many rows: "))
c1 = int(input("How many cols: "))

print("Enter " + str(r1 * c1) + " values")
metrics1 = []
for i in range(0, r1):
    row = []
    for j in range(0, c1):
        v = int(input(""))
        row.append(v)
    metrics1.append(row)

# print(metrics)


r2 = int(input("How many rows: "))
c2 = int(input("How many cols: "))
print("Enter " + str(r2 * c2) + " values")
metrics2 = []
for i in range(0, r2):
    row = []
    for j in range(0, c2): # aatli loop purn row process krte
        v = int(input(""))
        row.append(v)
    metrics2.append(row)

# print(metrics)
print("Matrics 1: ")
for i in range(0, r1):
    for j in range(0, c1):
        print( metrics1[i][j] , end=" " )
    print("")

print("Matrics 2: ")
for i in range(0, r2):
    for j in range(0, c2):
        print(metrics2[i][j], end=" ")
    print("")