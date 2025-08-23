import numpy as np
from scipy.interpolate import lagrange

# Define the matrices
A = np.array([
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [5, 0, 0, 0, 0, 1]
])

B = np.array([
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0]
])

C = np.array([
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0]
])

# Transpose the matrices
A_T = A.transpose()
B_T = B.transpose()
C_T = C.transpose()

# Print transposed matrices
print("Transposed Matrix A:")
print(A_T)
print("\nTransposed Matrix B:")
print(B_T)
print("\nTransposed Matrix C:")
print(C_T)

# Function to perform Lagrange interpolation on a row
def interpolate_row(row):
    x = np.arange(1, len(row) + 1)  # x-coordinates (1, 2, 3, 4)
    y = row                         # y-coordinates (row values)
    poly = lagrange(x, y)           # Compute Lagrange polynomial
    return poly

# Initialize matrices to store interpolation polynomials
interpolations_A = []
interpolations_B = []
interpolations_C = []

# Perform Lagrange interpolation for each row of transposed matrices
for i in range(A_T.shape[0]):
    interpolations_A.append(interpolate_row(A_T[i]))

for i in range(B_T.shape[0]):
    interpolations_B.append(interpolate_row(B_T[i]))

for i in range(C_T.shape[0]):
    interpolations_C.append(interpolate_row(C_T[i]))

# Print the interpolation matrices evaluated at points 1, 2, 3, 4
eval_points = [1, 2, 3, 4]

# Convert polynomial coefficients to matrices
def poly_to_coeffs(poly, degree=3):
    """Convert polynomial to coefficient array [x^3, x^2, x, constant]"""
    if hasattr(poly, 'coeffs'):
        coeffs = poly.coeffs  # Keep original order [x^3, x^2, x, constant]
        # Pad with zeros if needed
        while len(coeffs) < degree + 1:
            coeffs = np.append([0], coeffs)
        return coeffs[:degree + 1]
    else:
        return np.array([0, 0, 0, 0])

# Create coefficient matrices
matrix_A = np.array([poly_to_coeffs(poly) for poly in interpolations_A])
matrix_B = np.array([poly_to_coeffs(poly) for poly in interpolations_B])
matrix_C = np.array([poly_to_coeffs(poly) for poly in interpolations_C])

print("\nInterpolation Matrix A (coefficients: [x^3, x^2, x, constant]):")
print(matrix_A)

print("\nInterpolation Matrix B (coefficients: [x^3, x^2, x, constant]):")
print(matrix_B)

print("\nInterpolation Matrix C (coefficients: [x^3, x^2, x, constant]):")
print(matrix_C)

# Define S vector
S = np.array([1, 35, 3, 9, 27, 30])

# Compute T(x) = S · A_m * S · B_m - S · C_m
S_A = np.dot(S, matrix_A)  # S · A_m (degree 3 polynomial)
S_B = np.dot(S, matrix_B)  # S · B_m (degree 3 polynomial)
S_C = np.dot(S, matrix_C)  # S · C_m (degree 3 polynomial)

# Reverse coefficients to get [constant, x, x^2, x^3] order
S_A_rev = S_A[::-1]
S_B_rev = S_B[::-1]
S_C_rev = S_C[::-1]

print(f"\nS = {S}")
print(f"A . s = {S_A_rev}")
print(f"B . s = {S_B_rev}")
print(f"C . s = {S_C_rev}")

# Polynomial multiplication: A.s * B.s (results in degree 6 polynomial)
poly_product = np.convolve(S_A_rev, S_B_rev)

# Extend C.s to degree 6 by padding with zeros for higher degree terms
S_C_extended = np.concatenate([S_C_rev, np.zeros(3)])  # [c0, c1, c2, c3, 0, 0, 0]

# Subtract C.s from the product
T_x = poly_product - S_C_extended

print(f"\nNow, A . s * B . s — C . s:")
print(f"t = {T_x}")