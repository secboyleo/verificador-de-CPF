cpf = input("digite o seu cpf  (somente os números) >>>")
tam = len(cpf)
vetor_cpf = []
soma = 0
flag = False

#confere se o cpf tem 11 digitos
if tam < 11 or tam > 11:
    print('Digite um CPF válido.')
else:
    for num in range(tam):
        vetor_cpf.append(cpf[num])
    
    #verifica se o cpf é falso (numeros repetidos)
    cont = False
    for num in range(10):
        if vetor_cpf[num] == vetor_cpf[num + 1]:
            cont = True
            
    if cont == False:
        #verificador do primeiro digito
        i = 10
        for num in range(9):
            valor = int(vetor_cpf[num]) #transforma de str para int
            soma += valor * i
            i -= 1

        resto = (soma * 10) % 11
        soma = 0 #soma volta a valer zero
        
        if resto == int(vetor_cpf[9]):
            flag = True
        
        #verificador do segundo digito
        i = 11
        for num in range(10):
            valor = int(vetor_cpf[num])
            soma += valor * i
            i -= 1

        resto = (soma * 10) % 11
        flag = False
        if resto == int(vetor_cpf[10]):
            flag = True
        
if flag == True:
    print(f'O cpf {cpf} é VALIDO')
else:
    print(f'o cpf {cpf} é INVALIDO')
