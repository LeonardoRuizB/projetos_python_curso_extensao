vel_max = 0
r = ''

while r.lower() != 'n':
    
    n = int(input("Informe o numero de lesmas capturadas: "))
    
    for i in range(n):
        vel = int(input(f'Informe a velocidade da lesma {i+1}: '))
        
        if vel > vel_max:
            vel_max = vel
            
    if vel_max < 10:
        print('Nível 1')
        
    elif vel_max < 20:
        print ('Nível 2')
        
    else:
        print('Nível 3')
        
    r = input("deseja repetir? (s/n)")  
    vel_Max = 0
    
print("Fim do programa!")