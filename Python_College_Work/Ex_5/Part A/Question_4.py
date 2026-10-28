#A list containing numbers from 1 to 50
l = [i for i in range(1,51)]
print(l)

#A list containing only the even numbers from 1 to 50
g = [i for i in range(1,51) if i%2==0]
print(g)


def enter_prices():
    n = int(input("Enter number of prices of products to be entered:"))
    p=[k:=int(input("Enter price:")) for i in range(n)]
    return p

prices = enter_prices()
print()

j = [i for i in prices if i >1000]
print("List with prices greater 1000",j)

k = [i*0.9 for i in prices]
print("List with prices after applying 10 percent discount",k)


