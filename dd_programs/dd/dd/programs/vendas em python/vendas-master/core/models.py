from django.db import models
from django.db.models import Sum, F
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import number_format

gender_list = [('M', 'masculino'), ('F', 'feminino')]


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        _('criado em'), auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        _('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel):

    """ Person is abstract model """
    # gender = models.CharField(_(u'gênero'), max_length=1, choices=gender_list)
    cpf = models.CharField(_('CPF'), max_length=11)
    firstname = models.CharField(_('Nome'), max_length=20)
    lastname = models.CharField(_('Sobrenome'), max_length=20)
    email = models.EmailField(_('e-mail'), unique=True)
    phone = models.CharField(_('Fone'), max_length=18)
    birthday = models.DateTimeField(_('Nascimento'))

    class Meta:
        abstract = True
        ordering = ['firstname']

    def __str__(self):
        return self.firstname + " " + self.lastname
    full_name = property(__str__)


class Customer(Person):
    pass

    class Meta:
        verbose_name = u'cliente'
        verbose_name_plural = u'clientes'

    # clica na pessoa e retorna os detalhes dela
    def get_customer_url(self):
        return u"/customers/%i" % self.id

    # clica em vendas e retorna as vendas da pessoa
    def get_sale_customer_url(self):
        return u"/sale/?customer=%i" % self.id

    # vendas por pessoa
    def get_sales_count(self):
        return self.customer_sale.count()


class Seller(Person):
    active = models.BooleanField(_('ativo'), default=True)
    internal = models.BooleanField(_('interno'), default=True)
    commissioned = models.BooleanField(_('comissionado'), default=True)
    commission = models.DecimalField(
        _(u'comissão'), max_digits=6, decimal_places=2, default=0.01, blank=True)

    class Meta:
        verbose_name = u'vendedor'
        verbose_name_plural = u'vendedores'

    # clica no vendedor e retorna os detalhes dele
    def get_seller_url(self):
        return u"/sellers/%i" % self.id

    # clica em vendas e retorna as vendas do vendedor
    def get_sale_seller_url(self):
        return u"/sale/?seller=%i" % self.id

    # vendas por pessoa
    def get_sales_count(self):
        return self.seller_sale.count()

    def get_commission(self):
        return u"%s" % number_format(self.commission * 100, 0)


class Brand(models.Model):
    brand = models.CharField(_('Marca'), max_length=50, unique=True)

    class Meta:
        ordering = ['brand']
        verbose_name = u'marca'
        verbose_name_plural = u'marcas'

    def __str__(self):
        return self.brand


class Product(models.Model):
    imported = models.BooleanField(_('Importado'), default=False)
    outofline = models.BooleanField(_('Fora de linha'), default=False)
    ncm = models.CharField(_('NCM'), max_length=8)
    brand = models.ForeignKey(Brand, verbose_name=_('marca'))
    product = models.CharField(_('Produto'), max_length=60, unique=True)
    price = models.DecimalField(_(u'Preço'), max_digits=6, decimal_places=2)
    ipi = models.DecimalField(
        _('IPI'), max_digits=3, decimal_places=2, blank=True)
    stock = models.IntegerField(_('Estoque atual'))
    stock_min = models.PositiveIntegerField(_(u'Estoque mínimo'), default=0)

    class Meta:
        ordering = ['product']
        verbose_name = u'produto'
        verbose_name_plural = u'produtos'

    def __str__(self):
        return self.product

    def get_price(self):
        return u"R$ %s" % number_format(self.price, 2)

    def get_ipi(self):
        return u"%s" % number_format(self.ipi * 100, 0)


class Sale(TimeStampedModel):
    customer = models.ForeignKey(
        'Customer', related_name='customer_sale', verbose_name=_('cliente'))
    seller = models.ForeignKey(
        'Seller', related_name='seller_sale', verbose_name=_('vendedor'))

    class Meta:
        verbose_name = u'venda'
        verbose_name_plural = u'vendas'

    def __str__(self):
        return u"%03d" % self.id + u"/%s" % self.created.strftime('%y')
    codigo = property(__str__)

    def get_detalhe(self):
        return u"/sale/%i" % self.id

    # conta os itens em cada venda
    def get_itens(self):
        return self.sales_det.count()

    def get_total(self):
        qs = self.sales_det.filter(sale=self.pk).values_list(
            'price_sale', 'quantity') or 0
        t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0] * q[1], qs))
        return u"R$ %s" % number_format(t, 2)


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sales_det')
    product = models.ForeignKey(
        Product, related_name='product_det', verbose_name=_('produto'))
    quantity = models.PositiveSmallIntegerField(_('quantidade'))
    price_sale = models.DecimalField(
        _(u'Preço de venda'), max_digits=6, decimal_places=2, default=0)
    ipi_sale = models.DecimalField(
        _(u'IPI'), max_digits=3, decimal_places=2, default=0.1)

    def __str__(self):
        return str(self.sale)

    def get_subtotal(self):
        return self.price_sale * (self.quantity or 0)

    subtotal = property(get_subtotal)

    def getID(self):
        return u"%04d" % self.id

    def price_sale_formated(self):
        return u"R$ %s" % number_format(self.price_sale, 2)

    def get_ipi(self):
        return u"%s" % number_format(self.ipi_sale * 100, 0)

    def subtotal_formated(self):
        return u"R$ %s" % number_format(self.subtotal, 2)
