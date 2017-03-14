# coding: utf-8

import os


def populate():
    leonardo_cantor = add_cantor('Leonardo')
    maria_rodolfo_cantor = add_cantor('Maria Cecilia & Rodolfo')
    jorge_matheus_cantor = add_cantor('Jorge & Matheus')
    jimi_hendrix_cantor = add_cantor('Jimi Hendrix')
    elvis_cantor = add_cantor('Elvis Presley')
    john_lennon_cantor = add_cantor('John Lennon')
    diana_krall_cantor = add_cantor('Diana Krall')

    sertanejo_gen = add_genero('Sertanejo')
    rock_roll_gen = add_genero('Rock and Roll')
    jazz_gen = add_genero('Jazz')

    add_disco(
        titulo='Live In London - At The Royal Albert Hall',
        genero=sertanejo_gen,
        ano_lancamento=2013,
        cantor=jorge_matheus_cantor,
        valor=19.90
    )

    add_disco(
        titulo='A Hora É Agora - Ao Vivo em Jurerê',
        genero=sertanejo_gen,
        ano_lancamento=2012,
        cantor=jorge_matheus_cantor,
        valor=11.88
    )

    add_disco(
        titulo='Essencial',
        genero=sertanejo_gen,
        ano_lancamento=2012,
        cantor=jorge_matheus_cantor,
        valor=15.90
    )

    add_disco(
        titulo='Com você',
        genero=sertanejo_gen,
        ano_lancamento=2013,
        cantor=maria_rodolfo_cantor,
        valor=21.99
    )

    add_disco(
        titulo='Ao vivo em São Paulo',
        genero=sertanejo_gen,
        ano_lancamento=2010,
        cantor=maria_rodolfo_cantor,
        valor=10.54
    )

    add_disco(
        titulo='CD & DVD Ao Vivo Em Goiânia',
        genero=sertanejo_gen,
        ano_lancamento=2009,
        cantor=maria_rodolfo_cantor,
        valor=14.90
    )

    add_disco(
        titulo='Vivo Apaixonado',
        genero=sertanejo_gen,
        ano_lancamento=2013,
        cantor=leonardo_cantor,
        valor=21.90
    )

    add_disco(
        titulo='Alucinação',
        genero=sertanejo_gen,
        ano_lancamento=2010,
        cantor=leonardo_cantor,
        valor=14.90
    )

    add_disco(
        titulo='Coração Bandido',
        genero=sertanejo_gen,
        ano_lancamento=2008,
        cantor=leonardo_cantor,
        valor=9.90
    )

    add_disco(
        titulo='People, Hell & Angels',
        genero=rock_roll_gen,
        ano_lancamento=2013,
        cantor=jimi_hendrix_cantor,
        valor=26.91
    )

    add_disco(
        titulo='Valleys Of Neptune',
        genero=rock_roll_gen,
        ano_lancamento=2010,
        cantor=jimi_hendrix_cantor,
        valor=25.11
    )

    add_disco(
        titulo='Live at Berkeley',
        genero=rock_roll_gen,
        ano_lancamento=2003,
        cantor=jimi_hendrix_cantor,
        valor=26.94
    )

    add_disco(
        titulo='The Sun Sessions',
        genero=rock_roll_gen,
        ano_lancamento=1955,
        cantor=elvis_cantor,
        valor=107.22
    )

    add_disco(
        titulo='Elvis Plesley',
        genero=rock_roll_gen,
        ano_lancamento=1956,
        cantor=elvis_cantor,
        valor=24.90
    )

    add_disco(
        titulo='Elvis Christmas Album',
        genero=rock_roll_gen,
        ano_lancamento=1957,
        cantor=elvis_cantor,
        valor=11.56
    )

    add_disco(
        titulo='Working Class Hero: The Definitive Lennon',
        genero=rock_roll_gen,
        ano_lancamento=2005,
        cantor=john_lennon_cantor,
        valor=150.41
    )

    add_disco(
        titulo='Acoustic',
        genero=rock_roll_gen,
        ano_lancamento=2004,
        cantor=john_lennon_cantor,
        valor=27.89
    )

    add_disco(
        titulo='Anthology',
        genero=rock_roll_gen,
        ano_lancamento=1998,
        cantor=john_lennon_cantor,
        valor=168.09
    )

    add_disco(
        titulo='Glad Rag Doll',
        genero=jazz_gen,
        ano_lancamento=2012,
        cantor=diana_krall_cantor,
        valor=32.90
    )



def add_disco(titulo, genero, ano_lancamento, cantor, valor):
    d = Disco.objects.get_or_create(titulo=titulo, genero=genero, ano_lancamento=ano_lancamento, cantor=cantor, valor=valor)


def add_genero(nome):
    g = Genero.objects.get_or_create(nome=nome)[0]
    return g


def add_cantor(nome):
    c = Cantor.objects.get_or_create(nome=nome)[0]
    return c


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lojavirtual.settings')
    from loja.models import Disco, Cantor, Genero
    populate()