def somaLista (valores=[]):
    """
    A função somaLista, recebe uma lista de numeros e faz a soma de todos os numeros da lista e retorna o resultado da soma
    Parameters: []
    ----------------------------
    Valores: []
        lista de numeros para a soma 
    returns
    ----------------------------
    retorna a soma de uma lista
    """
    resultado = 0
    for i in valores:
        resultado+=i
    return resultado

def mairoValor (lista=[]):
    """
    encontra o maior valor em uma lista numerica
    """
    m = lista[0]
    for i in lista:
        if i > m:
            m=i
    return m

def inverter(palavra=""):
    #Comando len (length-comprimento) para saber a quantidade de caracteres
    qtd = len(palavra)
    invertida=""
    for i in range (qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida
    
def palindromo (palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
        return "E um palindromo"
    else:
        return "Não é um palindromo"
        