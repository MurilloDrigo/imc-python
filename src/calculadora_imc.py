def calcular_imc(peso, altura):
    # Calcula o Índice de Massa Corporal (IMC) com base no peso e altura.
    # Args:
    #     peso (float): Peso da pessoa em quilogramas (kg).
    #     altura (float): Altura da pessoa em metros (m).
    # Returns:
    #     float: O IMC calculado.
    return peso / altura**2


def classificar_imc(imc):
    # Classifica o IMC em uma categoria específica.
    # Args:
    #     imc (float): Índice de Massa Corporal (IMC) calculado.
    # Returns:
    #     str: A categoria do IMC.
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


def main():
    print("Calculadora de IMC\n")
    try:
        peso = float(input("Por favor, insira seu peso em kg: "))
        altura = float(input("Insira sua altura em metros(EXEMPLO:1.70): "))
        imc = calcular_imc(peso, altura)
        categoria = classificar_imc(imc)
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Você está dentro da faixa de {categoria}.")
    except ValueError:
        print("Por favor, insira números válidos para peso e altura.")


if __name__ == "__main__":
    main()
