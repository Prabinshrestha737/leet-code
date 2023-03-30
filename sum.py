
#sum of two number that add upto target
def twoSum(numbers, target):
    dictt = {}
    for i in range(len(numbers)):
        if numbers[i] in dictt:
            return [dictt[numbers[i]], i]
        else:
            dictt[target - numbers[i]] = i
    return []
