def salida(entrada):
    for i in range(1000):
        if (i*i)==entrada:
            if entrada%2==0:
                return "Ambos"
            else:
                return "Cuadrado"
        elif (i*i)>entrada:
            n=2
            while n<=1000000:
                if (entrada%n==0 and n!=entrada):
                    return "Rectangulo"
                elif n==entrada:
                    return "Es primo"
                else:
                    n = n+1

print(salida(524288))
