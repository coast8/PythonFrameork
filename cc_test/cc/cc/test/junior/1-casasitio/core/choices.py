# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

BUSINESS_STATUS_PROPOSTA = (
    ('1', 'Iniciado'),
    ('2', 'Em andamento - Sítios Piauí'),
    ('3', 'Em andamento - Proprietário'),
    ('4', 'Em andamento - Inquilino'),
    ('5', 'Concluído - Não Concretizado'),
    ('6', 'Concluído - A Realizar'),
    ('7', 'Concluído - Encerrado'),
)

BUSINESS_PROPOSTA_PRIORIDADE = (
    ('1', 'Baixa prioridade'),
    ('2', 'Média prioridade'),
    ('3', 'Alta prioridade'),
    ('4', 'Urgente'),
    ('5', 'DAR CONTINUIDADE'),
)

TIPO_CLIENTE = (
    ('1', 'Pré Cliente'),
    ('2', 'Cliente'),
)

ORIGEM_CHOICES = (
    ('1', 'Site'),
    ('2', 'Telefone'),
    ('3', 'Facebook Chat'),
    ('4', 'Whatsapp TIM'),
    ('5', 'Indicação'),
)

OPERADORA_CHOICES = (
    ('1', 'Não informado'),
    ('2', 'Tim'),
    ('3', 'Oi'),
    ('4', 'Claro'),
    ('5', 'Vivo'),
)

TIPO_COBRANCA_PROPRIEDADE = (
    ('1', 'Por diária'),
    ('2', 'Por pessoa'),
)

TIPO_CONTA_CHOICES = (
    ('1', 'Despesa'),
    ('2', 'Receita'),
)

PAGAMENTO_TIPO = (
    ('1', 'Dinheiro'),
    ('2', 'Transferência'),
    ('3', 'Cartão'),
    ('4', 'Cheque'),
)

TIPO_VISITA = (
    ('1', 'Captação'),
    ('2', 'Visita ao sítio'),
    ('3', 'Visita à cliente'),
    ('4', 'Visita ao proprietário'),
    ('5', 'Fechamento de negócio'),
    ('6', 'Divulgação'),
)


BUSINESS_ANDAMENTO_TIPO = (
    ('1', 'Visita'),
    ('2', 'Reunião'),
    ('3', 'Proposta'),
    ('4', 'Ligação'),
    ('5', 'Email'),
    ('6', 'WhatsApp')
)