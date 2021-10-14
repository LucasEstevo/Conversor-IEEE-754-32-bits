while (True):
    
    """ Função: sinal_iee():
     *  Apresentação => Fornece o sinal do número convertido
     *  return => 1 = Negativo | 0 = Positivo
    """
    def sinal_iee():
        if int(entrada, 16) >= 0:
            sinal = 0
        else:
            sinal = 1
        return sinal

    """ Função expoente_iee():
     *  Apresentação => Calcula o expoente da conversão IEE
     *  return => Expoente do IEE
    """
    def expoente_iee():
        bias = 127
        bin_expoente = bin((bias + (len(entrada_binario) - 3)))
        expoente = (str(bin_expoente))[2:(len(bin_expoente))]
        return expoente

    """ Função mantissa_iee():
     *  Apresentação => Calcula a mantissa da conversão IEE
     *  return => Valor da mantissa
    """
    def mantissa_iee():
        mantissa = entrada_binario[3:(len(entrada_binario))]
        while(30):
            mantissa = mantissa + mantissa
            if len(mantissa) > 23:
                mantissa = mantissa[0:23]
                break
        return mantissa

    entrada = '0x' + (input('Digite o valor Hexadecimal a ser convertido: '))
    
    entrada_binario = bin(int(entrada, 16))

    sinal = sinal_iee()
    expoente = expoente_iee()
    mantissa = mantissa_iee()

    print(sinal, expoente, mantissa)

    while(True):
        
        resposta = input('Deseja uma nova conversão? [Y/N]')
        
        if resposta == 'N':
            continuar = 'N'
            break
        elif resposta =='Y':
            continuar = 'Y'
            break

    if continuar == 'N':
        break
