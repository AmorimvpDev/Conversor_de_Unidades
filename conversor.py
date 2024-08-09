print('''Sistema de (Medidas)
Sistema de (Massa)''')

sistemas = ['medidas', 'massa']
medidas = ['cm', 'm', 'km']
massas = ['kg', 'g', 't']

def medida_valida(medida, medidas):
    return medida in medidas

def massa_valida(massa, massas):
    return massa in massas


def converter_massas(valor_ma, massa_de, massa_para):
    conversoes = {
        'kg_g': lambda x: x * 1000,
        'kg_t': lambda x: x / 1000,
        'g_kg': lambda x: x / 1000,
        'g_t': lambda x: x / 1000000,
        't_kg': lambda x: x * 1000,
        't_g': lambda x: x * 1000000
    }
    chave = f"{massa_de}_{massa_para}"
    if chave in conversoes:
        return conversoes[chave](valor_ma)
    return None

def converter_medidas(valor_me, medida_de, medida_para):
    conversoes = {
        'cm_m': lambda x: x / 100,
        'cm_km': lambda x: x / 100000,
        'm_cm': lambda x: x * 100,
        'm_km': lambda x: x / 1000,
        'km_cm': lambda x: x * 100000,
        'km_m': lambda x: x * 1000
    }
    chave = f"{medida_de}_{medida_para}"
    if chave in conversoes:
        return conversoes[chave](valor_me)
    return None

continuar = True
while continuar:

    escolha = input('Deseja fazer a conversão de qual sistema?: ').strip().lower()

    while escolha not in sistemas:
        print('Sistema inválido')
        escolha = input('Deseja fazer a conversão de qual sistema?: ').strip().lower()

    if escolha == sistemas[0]:
        print('CM, M ou KM')

        valor_medida = input('Qual medida?: ').strip().lower()
        while not medida_valida(valor_medida, medidas):
            print('Medida inválida')
            valor_medida = input('Qual medida?: ').strip().lower()
        
        valor_medida1 = input('Para qual?: ').strip().lower()
        while not medida_valida(valor_medida1, medidas) or valor_medida == valor_medida1:
            if valor_medida == valor_medida1:
                print('Medida inválida: as medidas escolhidas são iguais.')
            else:
                print('Medida inválida')
            valor_medida1 = input('Para qual?: ').strip().lower()

        valor_me = float(input('Digite o valor a ser convertido: '))
        
        resultado_me = converter_medidas(valor_me, valor_medida, valor_medida1)
        if resultado_me is not None:
            print(f"{valor_me} {valor_medida} é igual a {resultado_me} {valor_medida1}")
        else:
            print("Conversão não suportada.")


    if escolha == sistemas[1]:
        print('KG, G(gramas) ou T(toneladas)')

        valor_massa = str(input('Deseja converter a unidade: ')).strip().lower()
        while not massa_valida(valor_massa, massas):
            print('Massa inválida')
            valor_massa = str(input('Deseja converter a unidade: '))
        
        valor_massa1 = str(input('Para a unidade: ')).strip().lower()
        while not massa_valida(valor_massa1, massas) or valor_massa == valor_massa1:
            if valor_massa == valor_massa1:
                print('Unidades iguais')
            else:
                print('Unidade inválida')
            valor_massa1 = str(input('para a unidade: ')).strip().lower()

        valor_ma = int(input('Digite o valor a ser convertido: '))
        resultado_ma = converter_massas(valor_ma, valor_massa, valor_massa1)
        if resultado_ma is not None:
            print(f'{valor_ma} {valor_massa} é igual a {resultado_ma} {valor_massa1}')
        else:
            print('Conversão não suportada.')

    continuar = str(input('Deseja continuar? (s/n): ')).strip().lower() == 's'