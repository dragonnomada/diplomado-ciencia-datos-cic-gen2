def calcular_primos(n=10):
    primos = []

    i = 2

    while len(primos) < n:
        es_primo = True # Creencia original
        # Recorremos cada primo en los primos
        for p in primos:
            if i % p == 0: # i es múltiplo de p
                # i no es primo
                es_primo = False
        if es_primo:
            primos.append(i) # Agregamos i a los primos

        i += 1

    return primos