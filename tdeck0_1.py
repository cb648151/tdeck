from PIL import Image
import random

A = ("tdeck_images/A.jpg")
B = ("tdeck_images/B.jpg")
C = ("tdeck_images/C.jpg")
D = ("tdeck_images/D.jpg")
E = ("tdeck_images/E.jpg")
F = ("tdeck_images/F.jpg")
G = ("tdeck_images/G.jpg")
H = ("tdeck_images/H.jpg")
I = ("tdeck_images/I.jpg")
J = ("tdeck_images/J.jpg")
K = ("tdeck_images/K.jpg")
L = ("tdeck_images/L.jpg")
M = ("tdeck_images/M.jpg")
N = ("tdeck_images/N.jpg")
O = ("tdeck_images/O.jpg")
P = ("tdeck_images/P.jpg")
Q = ("tdeck_images/Q.jpg")
R = ("tdeck_images/R.jpg")
S = ("tdeck_images/S.jpg")
T = ("tdeck_images/T.jpg")
U = ("tdeck_images/U.jpg")
V = ("tdeck_images/V.jpg")

tdeck_lib = (A, B, C, D, E, F, G, H, I, J, 
K, L, M, N, O, P, Q, R, S, T, U, V)

img = Image.open(random.choice(tdeck_lib))
img.show(tdeck_lib) #create a librarylist instead of just A