data1 = [1, 3.5, 5-2j,]
data2 = [44, 56.6553, 89+7j]

for i in data1:
    for j in data2:
        product= i*j
        print(f"{i} x {j} = {product} type: {type(product)}")
        j += 1