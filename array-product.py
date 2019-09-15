

def productExceptSelf(nums):
    p = 1
    n = len(nums)
    left_products = []
    for i in range(0, n):
        left_products.append(p)
        p = p * nums[i]
    print('left products: ', left_products)

    p = 1
    right_products = []
    for i in range(n-1, -1, -1):
        right_products.append(p)
        p = p * nums[i]
    right_products.reverse()
    print('right products',right_products)

    return [a*b for a,b in zip(left_products, right_products)]


arr = [2,4,3]

print(arr)
print(productExceptSelf(arr))

