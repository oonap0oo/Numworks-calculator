
# print an system of equations given by
# matrix A and vector b
def print_eq(A,b):
  row_n = 0
  for row_A, row_b in zip(A,b):
    print("|", end="")
    for element in row_A:
      print("{0:^5}".format(element), end="")
    if row_n == len(A) - 1:
      print("| .x= |", end="")
    else:
      print("|     |", end="")
    row_n += 1
    print("{0:^5}".format(row_b), end="")
    print("|")

# print a vector
def print_vector(x):
  for element in x:
    print("|", end="")
    print(" {0:^12.8f} ".format(element), end="")
    print("|")
    
# print a matrix        
def print_matrix(X):   
  for row in X:
    print("|", end="")
    for element in row:
      print(" {0:^12.8f} ".format(element), end="")
    print("|")

# calculate determinant of 2x2 matrix
# For a matrix [[a, b], [c, d]]
# the determinant is ad - bc
def det22(mat):
  return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]


# calculate determinant of 3x3 matrix
#     0 1 2
# 0 | a b c |
# 1 | d e f |
# 2 | g h i |
#
# |A| = a * det( |e f| ) - b * det( |d f| ) + c * det( |d e| )
#                |h i|              |g i|              |g h|
def det33(mat):
  submat1=[[mat[1][1], mat[1][2]],
           [mat[2][1], mat[2][2]]]
  submat2=[[mat[1][0], mat[1][2]],
           [mat[2][0], mat[2][2]]]
  submat3=[[mat[1][0], mat[1][1]],
           [mat[2][0], mat[2][1]]]
  det=mat[0][0]*det22(submat1)
  det-=mat[0][1]*det22(submat2)
  det+=mat[0][2]*det22(submat3)
  return(det)

# matrix is a list of lists, to make a copy, deepcopy is needed
# numworks does not have the deepcopy function, this function performs
# deepcopy of a matrix
def deepcopy(mat):
  new_mat = []
  for row in mat:
    new_mat.append(row.copy())
  return new_mat

# solve system of 2 equations with 2 variables
# using Cramer's rule
def solve_system_2(A, b):
  det_A = det22(A)
  if det_A==0:
    print("System has no solutions")
    return
  else:
    solution=[]
    for col in range(2):
      mat1=deepcopy(A)
      for row in range(2):
        mat1[row][col]=b[row]
      solution.append(det22(mat1) / det_A)
    return solution

# solve system of 3 equations with 3 variables
# using Cramer's rule
def solve_system_3(A, b):
  det_A = det33(A)
  if det_A==0:
    print("System has no solutions")
    return
  else:
    solution=[]
    for col in range(3):
      mat1=deepcopy(A)
      for row in range(3):
        mat1[row][col]=b[row]
      solution.append(det33(mat1) / det_A)
    return solution

# check a solution x of system
# A.x = b
# by calculating A.x, should be equal to b
def check_solution(A, x):
  N=len(A)
  b_check=[0]*N
  for row in range(N):
    for col in range(N):
      b_check[row]+=A[row][col]*x[col]
  return b_check

# a test with 2 equations, 2 variables
A=[[6, -5],
   [-7, 2]]

b=[2, -3]

print("System of 2 equations\nwith 2 variables")
print("A.x = b\n")
print_eq(A,b)
x=solve_system_2(A, b)
print("\nsolution found:\n x = ")
print_vector(x)
print("\nChecking x by\ncalculating vector b:")
print_vector(check_solution(A, x))

# a test with 3 equations, 3 variables
A=[[5,-6,7],
   [-3,5,4],
   [4,-8,2]]

b=[4,2,-3]

print("\nSystem of 3 equations\nwith 3 variables")
print("A.x = b\n")
print_eq(A,b)
x=solve_system_3(A, b)
print("\nsolution found:\n x = ")
print_vector(x)
print("\nChecking x by\ncalculating vector b:")
print_vector(check_solution(A, x))




