
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc


def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"


peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))


indice_massa_corporal = calcular_imc(peso, altura)

print(f"O Índice de Massa Corporal (IMC) é: {indice_massa_corporal:.2f}")
print("Situação: ", interpretar_imc(indice_massa_corporal))
