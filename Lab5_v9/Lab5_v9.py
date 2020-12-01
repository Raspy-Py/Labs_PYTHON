sum_1 = 0 # Сума дільників першого числа (i)
sum_2 = 0 # Сума дільників другого числа (sum_1)
skip = False # Потрібна для уникнення повтору пар

for i in range(200, 301):
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            sum_1 += j

    if sum_1 >= 200 and sum_1 <= 300:
        for k in range(1, sum_1 // 2 + 1):
            if sum_1 % k == 0:
                sum_2 += k;
    
        if sum_2 == i and sum_1 != sum_2:
            if skip:
                skip = False
            else:
                print(i, "---", sum_1)
                skip = True

    sum_1 = 0
    sum_2 = 0
