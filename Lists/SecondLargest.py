def second_lar(n):
    largest=second_largest=float('-inf')
    for num in n:
        if num>largest:
            second_largest=largest
            largest=num
        if num>second_largest and num!=largest:
            second_largest=num
    return second_largest if second_largest!= float('-inf') else None
list=[10,20,30,50]
print(second_lar(list))


