import random
from core.models import Customer, Seller, Sale, SaleDetail, Product
from fixtures.gen_random_values import *

REPEAT = 200
qcustomers = Customer.objects.count()
qsellers = Seller.objects.count()
qproducts = Product.objects.count()

for i in range(REPEAT):
    c = random.randint(1, qcustomers)
    customer = Customer.objects.get(pk=c)
    s = random.randint(1, qsellers)
    seller = Seller.objects.get(pk=s)
    obj = Sale(
        customer=customer,
        seller=seller,
    )
    obj.save()
    print(obj.pk)
    for j in range(random.randint(1, 10)):
        sale = Sale.objects.get(pk=obj.pk)
        p = random.randint(1, qproducts)
        product = Product.objects.get(pk=p)
        quantity = random.randint(1, 50)
        price_sale = product.price
        ipi_sale = product.ipi
        sd = SaleDetail(
            sale=sale,
            product=product,
            quantity=quantity,
            price_sale=price_sale,
            ipi_sale=ipi_sale,
        )
        sd.save()

print('%d Vendas salvo com sucesso.' % REPEAT)
