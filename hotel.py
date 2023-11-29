# Imprima todos os números exceto 13 com For.

for i in range(1, 21):
    if(i == 13):
     continue
    else:
     print(i)

# Imprima todos os números exceto 13 com While 

contador = 1
while(contador <= 20):
    if(contador == 13):
     contador = contador + 1
     continue
    else:
     print(contador)
     contador = contador + 1

# Imprima todos os números exceto 13 em ordem descendente

for i in range(20, 0, -1):
    if(i == 13):
     continue
    else:
     print(i)     