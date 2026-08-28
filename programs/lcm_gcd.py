
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = 12, 8
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))


# finding extra candies
def find(list1, candies):
    maximum = max(list1)
    total = []
    # for i in list1:
    #     if candies+i >= maximum:
    #         total.append(True)
    #     else:
    #         total.append(False)
    total = [True if candies+i >= maximum else False for i in list1]
    return total

list1 = [2, 3, 5, 1, 4]
candies = 3
print(find(list1, candies))
