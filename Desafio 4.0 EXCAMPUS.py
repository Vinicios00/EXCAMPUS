from time import sleep
import random
sleep(1)
total = 0
print  ('SEJA BEM VINDO A LOJA EXCAMPUS❣️...❣️')
sleep (1)
print (' ')            # BEM VINDO
print (' ')
print (' ')
pessoa = input ('Digite seu nome ✨ :')
sleep (0.5)
print (' ')
print (' ') 
print (f'Bem vindo {pessoa} ! Nós da loja Excampus ficamos muito feliz pela preferencia!')
print (' ')            # Mensagem de boas vindas
print (' ')
sleep (0.5)
print ('                    »»————-　★　————-««')    
tenis = 0
while tenis != '':
  print (' ')
  print (' ')            # Apresentação da loja
  sleep (1)
  print ('Aqui voce irá encomtrar as melhores marcas de tenis!')
  sleep (0.1)
  print ('[ 1 ] Nike')
  sleep (1)
  print ('[ 2 ] Adidas')                 # Marcas
  sleep (1)
  print ('[ 3 ] Puma')
  sleep (1)
  print ('[ 4 ] Olympikus')
  sleep (1)
  print('Ou aperte ENTER para sair.')
  print ('')
  print ('')
  tenis = str(input('Selecione uma marca de tenis:'))
  print ('')
  print ('')
  print ('                    »»————-　★　————-««')
  if tenis == '1':                        
  
  #                              Modelos1
    sleep (1)
    print ('Temos os seguintes modelos:')
    sleep (1)
    print (' [ 1 ] 👟 Air Force - R$ 500,00')
    sleep (1)
    print (' [ 2 ] 👞 Air Max - R$ 390,00')
    print ('')
    print ('')
    sleep (1)
    nike = input('Selecione um modelo de tenis:')
    if nike == '1':
      print('Valor = R$: 500,00 ')
      total += 500
    elif nike == '2':
      print('Valor = R$: 390,00')
      total += 390 
    else:
      print('Apenas 1 ou 2')
    

  print ('')
  print ('') 
  if tenis == '2':    
    #               Modelos2
    sleep(1)                      
    print ('Temos os seguintes modelos')
    sleep (1)
    print('[ 1 ] 👟 Runfalcon - R$ 200,00')
    sleep (1)
    print('[ 2 ] 👞 Sonkei - R$ 100,00')
    print ('')
    print ('')
    sleep (1)
    adidas = input('Selecione um modelo de tenis:')
    if adidas == '1':
      print('Valor = R$: 200,00')
      total += 200
    elif adidas == '2':
      print('Valor = R$: 100,00')
      total += 100  #total = total + 10
    else:
      print('Apenas 1 ou 2')
  if tenis == '3': 
    #                              Modelos3
    sleep(1)                         
    print ('Temos os seguintes modelos')
    sleep (1)
    print('[ 1 ] 👟  Enzo R$: 270,00')
    sleep (1)
    print('[ 2 ] 👞 Wired R$: 150,00')
    print ('')
    print ('')
    sleep (1)
    puma = input('Selecione um modelo de tenis:')
    if puma == '1':
      print('Valor = R$: 270,00 ')
      total += 270
    elif puma == '2':
      print('Valor = R$: 150,00')
      total += 150 
    else:
      print('Apenas 1 ou 2')
  if tenis == '4':    
    #                              Modelos4
    sleep (1)                     
    print ('Temos os seguintes modelos')
    sleep (1)
    print('[ 1 ] 👟 Globe R$: 130,00')
    sleep (1)
    print('[ 2 ] 👞 Drift 2 R$: 85,00')
    print ('')
    print ('')
    sleep (1)
    olympikus = input('Selecione um modelo de tenis:')
    if olympikus == '1':
      print('Valor = R$: 130,00 ')
      total += 130
    elif olympikus == '2':
      print('Valor = R$: 85,00')
      total += 85 
    else:
      print('Apenas 1 ou 2')
sleep(1)
print ('')
print ('')
print('Finalizando o pedido')
sleep(1)
print(f'{pessoa}, o seu pedido foi concluído com sucesso.')
print(f'O valor total a pagar é de R$ {total},00')
sleep(1)
print(' O numero do seu boleto é: 00003435308210340')
sleep(1)
print ('')
print ('')
print('Após o seu pagamento o tenis chegará em 15 dias')
sleep(1)
print('Obrigado por sua compra, Volte sempre!')