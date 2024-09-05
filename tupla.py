#atividade 4 tupla
def calcular_valor_medio(tupla_de_tuplas):
    total_elementos = 0
    soma_total = 0

    for tupla in tupla_de_tuplas:
        for elemento in tupla:
            soma_total += elemento
            total_elementos += 1

    if total_elementos == 0:
        return None  # Evitando divisão por zero

    valor_medio = soma_total / total_elementos
    return valor_medio

# Exemplo de uso
minha_tupla_de_tuplas = ((10, 20, 30), (15, 25, 35), (12, 22, 32))

media = calcular_valor_medio(minha_tupla_de_tuplas)
if media is not None:
    print(f"O valor médio dos números é: {media:.2f}")
else:
    print("A tupla está vazia.")

# Lembre-se de adaptar a tupla de acordo com seus dados reais!