#definindo funções

def soma(x, y):
    return x + y

def quadrado(x):
    return x*x
    
def soma_quadrado(x, y):
    x2 = quadrado(x)
    y2 = quadrado(y)
    return (x2, y2, soma(x2, y2))


###################################################################
###################################################################

