# Finding gradient, divergence, curl and their geometrical interpretation
from sympy.vector import CoordSys3D, gradient, curl, divergence

# Define coordinate system
N = CoordSys3D('N')

# Scalar field and vector field
scalar_field = N.x**2 + N.y**2 + N.z**2
vector_field = N.x*N.i + N.y*N.j + N.z*N.k

# Gradient
grad_f = gradient(scalar_field)
# Divergence
div_F = divergence(vector_field)
# Curl
curl_F = curl(vector_field)

grad_f, div_F, curl_F
