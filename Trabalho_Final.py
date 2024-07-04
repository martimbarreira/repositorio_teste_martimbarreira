import math

def calcular_perimetro():
    # Pergunta ao usuário se todos os lados são iguais
    lados_iguais = input("Todos os lados são iguais? (s/n): ").strip().lower()

    # Inicializa a lista de lados
    lados = []

    if lados_iguais == 's':
        # Se todos os lados são iguais, pede o valor de um lado e o número de lados
        lado = float(input("Digite o comprimento do lado (caso seja um círculo, digite o diâmetro): "))
        
        
        if lado == 0:
            return "O comprimento do lado não pode ser zero. Por favor, forneça um comprimento de lado válido."
        
        num_lados = int(input("Digite o número de lados: "))

        if num_lados < 1:
            return "O número de lados deve ser pelo menos 1. Por favor, forneça um número de lados maior ou igual a 1."

        if num_lados == 1:
            # Calcula o perímetro de um círculo com o diâmetro dado
            perimetro = math.pi * lado
            return f"Um lado fornecido é interpretado como o diâmetro de um círculo. O perímetro do círculo é {perimetro:.4f}."

        # Verifica se o número de lados é menor que 3
        if num_lados < 3:
            return "Um polígono deve ter pelo menos 3 lados. Por favor, forneça um número de lados maior ou igual a 3."
        
        # Verifica se o número de lados ultrapassa o limite de 10
        if num_lados > 10:
            return "O número máximo de lados é 10. Por favor, forneça um número de lados menor ou igual a 10."
        
        # Calcula o perímetro
        perimetro = lado * num_lados
        
        return f"O perímetro do polígono é {perimetro}."
    
    elif lados_iguais == 'n':
        # Se os lados não são iguais, pede o comprimento de cada lado
        for i in range(10):
            lado = input(f"Digite o comprimento do lado {i+1} (ou pressione Enter para finalizar): ")
            if lado == '':
                break
            lado = float(lado)
            if lado == 0:
                return "O comprimento do lado não pode ser zero. Por favor, forneça um comprimento de lado válido."
            lados.append(lado)
        
        # Calcula o número de lados dados
        num_lados = len(lados)
        
        # Verifica se o número de lados é menor que 1
        if num_lados < 1:
            return "É necessário fornecer pelo menos 1 comprimento de lado."
        
        if num_lados == 1:
            return "Se apenas um lado foi fornecido, todos os lados são iguais."
        
        # Verifica se o número de lados é menor que 3
        if num_lados < 3:
            return "Um polígono deve ter pelo menos 3 lados. Por favor, forneça pelo menos 3 comprimentos de lados."
        
        perimetro = sum(lados)
                
        return f"O perímetro do polígono é {perimetro}."

resultado = calcular_perimetro()
print(resultado)