def TwoSum(num, target):
    dice = dict()
    for i in range(len(num)):
        n = num[i]
        differ = target - n
        if n in dice:
            return [dice[n], i]
        else:
            dice[differ] = i

num = [2, 7, 5, 2, 2]
diff = 7
print(TwoSum(num, diff))