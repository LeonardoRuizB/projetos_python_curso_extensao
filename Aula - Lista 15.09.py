      #        0    1      2      3        4       5          6        7        8
minha_lista = [1, 'Pedro', 25, 'Civc', 'Celta', 'Toyotao', 'Subaru', 'BMW', 'Mercedes']

elemento = 0

for indice, elemento in enumerate (minha_lista):
    
    if indice == 3:
            continue #Pula para a próxima iteração
          # break #Para a execução do Loop   
    
    print(f"O índice é: {indice} = {elemento}")
            
print("Parei de executar!")