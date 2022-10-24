nome=input("Digite seu nome: ")
idade= int(input("Digite a idade do paciente: "));
if idade>=65:
    print('O paciente,', nome ,', possui prioridade máxima no atendimento')
else:
    doenca_contagiosa=input("Suspeita de doença contagiosa?: ").upper()
    if doenca_contagiosa=="SIM":
        print("O paciente " + nome + " deve ser direcionado para a sala reservada.")
    else:
        emergencia=input('É uma emergência médica, Sim ou Não?: ').upper()
        if emergencia=='SIM':
            print('O paciente,', nome ,', possui prioridade máxima no atendimento')
        else:
            x=int(input('Entre com a senha do paciente (de acordo com a ordem de chegada): '))                            
            print("O paciente, " + nome +  ', não possui atendimento prioritário, portanto detem a senha de número ',x, ', e deve aguardar na sala comum.')

