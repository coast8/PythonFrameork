
#Esse erro está ocorrendo porque você está tentando 
#multiplicar um inteiro por um tipo vazio. 

def get_subtotal(self):
    try:
        return self.price_sale * self.quantity
    except TypeError:
        return 0


=================================================================================
