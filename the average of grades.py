N1 = float(input("Enter grade 1: "))
N2 = float(input("Enter grade 2: "))
N3 = float(input("Enter grade 3: "))

while N1 > 20 or N1 < 0 or N2 > 20 or N2 < 0 or N3 > 20 or N3 < 0:
    if N1 > 20 or N1 < 0:
        print("Please enter a correct grade for N1: ")
        N1 = float(input("Enter grade 1: "))
    if N2 > 20 or N2 < 0:
        print("Please enter a correct grade for N2: ")
        N2 = float(input("Enter grade 2: "))
    if N3 > 20 or N3 < 0:
        print("Please enter a correct grade for N3: ")
        N3 = float(input("Enter grade 3: "))

M = (N1 + N2 + N3) / 3
print("The average of the grades is:", M)

if M > 16:
    print("EXCELLENT")
elif 14 <= M < 16:
    print("GOOD")
elif 12 <= M < 14:
    print("SATISFACTORY")
elif 10 <= M < 12:
    print("PASS")
else:
    print("FAIL")
