def function_hcf_recursive(a,b):
    if a == 0:
        return b
    else:
        return function_hcf_recursive(b % a, a)

def lcm_hcf_recursive(a,b):
    hcf = function_hcf_recursive(a,b)

    lcm = (a * b) // hcf

    return lcm, hcf

a = int(input("Enter number ="))
b = int(input("Enter number ="))

print(lcm_hcf_recursive(a,b))

