def adder(*args):
    result = sum(args)
    return result
sum_result = adder(1, 2, 3, 4, 5,5,6,7,6,7,8,5,4,3,2,5,7,8,9,7,65,4,3,2,1,4,6,7,8,9)
print(f"Sum: {sum_result}")