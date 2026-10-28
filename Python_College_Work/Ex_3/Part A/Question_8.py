def find_lcm_hcf(a,b):
    if a > 0 and b > 0:
        if a > b:
            high = a
            low = b
        else:
            high = b
            low = a

        for i in range(low, 0, -1):
            if low % i == 0:
                if high % i == 0:
                    hcf = i
                    break
                else:
                    continue
        lcm = (a * b) // hcf

        return hcf, lcm

    else:
        return "Invalid Input"


