"""
51- Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua
distancia da origem (0,0).
"""

x = int(input("Escreva a cordenada X no R²: "))
y = int(input("Escreva a cordenada Y no R²: "))

print(f'A distancia da origem é: {((x**2)+(y**2)**0.5)}')
