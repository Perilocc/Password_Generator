import random

upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'
numerical_case = '1234567890'
simbols_case = '!@#$%&*+-=<>:;?'
password_list = []
x = 1
caracteres = (upper_case + lower_case + numerical_case + simbols_case)

n_caracteres = int(input('Digite quantos caracteres sua senha deve possuir: '))

password = ''.join(random.sample(caracteres, n_caracteres))
password_list.append('Senha {}: {}'.format(x, password))
print('Essa é a sua senha gerada: {}'.format(password))

feedback = str(input('Deseja outra senha? '))
while (feedback != '' or feedback != ''):
    if feedback == 'Sim' or feedback == 'sim':
        n_caracteres = int(input('Digite quantos caracteres sua senha deve possuir: '))
        password = ''.join(random.sample(caracteres, n_caracteres))
        x +=1
        password_list.append('Senha {}: {}'.format(x, password))
        print('Essa é a sua senha gerada: {}'.format(password))
        feedback = str(input('Deseja outra senha? '))
        
        if feedback == 'Sim' or feedback == 'sim':
            continue
        else:
            break
        
    else:
        break
password_list_formato = '\n'.join(password_list)
print('==============Obrigado por utilizar nosso serviço==============')
print('Obrigado por utilizar nosso serviço')
print('Aqui está sua lista de senhas:')
print(password_list_formato)
print('===============================================================')



