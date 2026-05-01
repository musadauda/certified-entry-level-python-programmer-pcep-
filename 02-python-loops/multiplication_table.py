# MULTIPLICATION TABLE
for i in range(1,13):
    for j in range(1,13):
        product = i*j
        print(f"{i} x {j} = {product}", end="\t")
        j += 1
    print()