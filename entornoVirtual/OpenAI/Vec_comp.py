from numpy import dot
from numpy.linalg import norm

vector0 = []
vector1 = []
vector2 = []

cos_sim = dot(vector0, vector1)/(norm(vector0)*norm(vector1))
print("similitu entre orden y frase 1 es: ", cos_sim)

cos_sim = dot(vector0, vector2)/(norm(vector0)*norm(vector2))
print("similitu entre orden y frase 2 es: ", cos_sim)