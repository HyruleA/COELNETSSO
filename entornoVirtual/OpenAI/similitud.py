from numpy import dot
from numpy.linalg import norm

#Obtiene la similitud de cosenos de dos vectores
def similitud_cos(vector1, vector2):
    cos_sim = dot(vector1, vector2)/(norm(vector1)*norm(vector2))
    return cos_sim