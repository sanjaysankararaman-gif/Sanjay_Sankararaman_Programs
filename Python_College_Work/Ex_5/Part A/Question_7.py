mat1 = []
def enter_ele_mat(mat):
    for i in range(int(input("Enter number of rows"))):
        l=[]
        a=int(input("Enter element 1 in row",i,"="))
        b=int(input("Enter element 2 in row",i,"="))
        l.append([a,b])
        mat.append(l)

def matrix_transpose(m1):
    m = [[m1[j][i] for j in range(len(m1))] for i in range(len(m1[0]))]
    return m

enter_ele_mat(mat1)

def print_mat(m):
    for i in m:
        print(i)
print("Original Matrix:")
print_mat(mat1)

print("Matrix Transpose:")
print(matrix_transpose(mat1))