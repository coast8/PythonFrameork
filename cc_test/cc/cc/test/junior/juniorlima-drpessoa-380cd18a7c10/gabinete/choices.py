# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

PESSOA_TIPO = (('1', 'Pessoa Física'),
               ('2', 'Pessoa Jurídica')
)

# PESSOA_GRUPO é pra ser foreingkey
PESSOA_GRUPO = (
                ('1', 'Associação de Bairro'),
                ('2', 'Comunidade'),
                ('3', 'Educativo'),
                ('4', 'Esporte e Lazer'),
                ('5', 'Família'),
                ('6', 'Político'),
                ('7', 'Prestador de Serviços de TI'),
                ('8', 'Profissional Liberal'),
                ('9', 'Profissional de Comunicação'),
                ('10', 'Profissional da Saúde'),
                ('11', 'Religioso Católico'),
                ('12', 'Religioso Evangélico'),
                ('13', 'Religioso Protestante'),
                ('14', 'Sem Terra'),
                ('15', 'Sem Teto'),
                ('16', 'Vizinhança')
)

PESSOA_SEXO = (('1', 'Masculino'),
                ('2', 'Feminino'),
)

PESSOA_TRATAMENTO = (
                    ('1', 'Nenhum'),
                    ('2', 'Civis - Vossa Excelência'),
                    ('3', 'Civis - Vossa Magnificência'),
                    ('4', 'Civis - Vossa Senhoria'),
                    ('5', 'Diversos - Digníssimo'),
                    ('6', 'Diversos - Dom, Dona'),
                    ('7', 'Diversos - Ilustríssimo'),
                    ('8', 'Diversos - Professor'),
                    ('9', 'Diversos - Senhor'),
                    ('10', 'Diversos - Senhora'),
                    ('11', 'Eclesiásticas - Vossa Alteza'),
                    ('12', 'Eclesiásticas - Vossa Eminência Reverendíssima'),
                    ('13', 'Eclesiásticas - Vossa Majestade'),
                    ('14', 'Eclesiásticas - Vossa Revenrendíssima'),
                    ('15', 'Eclesiásticas - Vossa Santidade'),
                    ('16', 'Judiciárias - Meritíssimo Juiz'),
                    ('17', 'Judiciárias - Vossa Excelência'),
                    ('18', 'Militares - Vossa Excelência'),
                    ('19', 'Militares - Vossa Senhoria'),
)

PESSOA_ENDERECO = (('1', 'Residencial'),
                   ('2', 'Comercial'),
                   ('3', 'Contato'),
)

TELEFONE_TIPO = (('1', 'Residencial'),
                 ('2', 'Comercial'),
                 ('3', 'Celular'),
                 ('4', 'Recado'),
                 ('5', 'Fax'),
)

PESSOA_GRAU = (('1', 'Analfabeto'),
               ('2', 'Ensino Fundamental'),
               ('3', 'Ensino Médio'),
               ('4', 'Ensino Superior'),
               ('5', 'Superior Incompleto'),
)

PESSOA_FUNCAO = (
                    ('1', 'Assessor Administrativo'),
                    ('2', 'Assessor de Comunicações'),
                    ('3', 'Assessor de Gabinete'),
                    ('4', 'Assessor Financeiro e Contábil'),
                    ('5', 'Assessor Jurídico'),
                    ('6', 'Assessor Legislativo'),
                    ('7', 'Assessor Parlamentar'),
                    ('8', 'Assistente Legislativo'),
                    ('9', 'Auxiliar Serviços Gerais'),
                    ('10', 'Cabo Eleitoral'),
                    ('11', 'Chefe de Gabinete'),
                    ('12', 'Chief Commercial Officer'),
                    ('13', 'Chief Information Officer'),
                    ('14', 'Coordenador de Geral de Campanha'),
                    ('15', 'Coordenador Regional de Campanha'),
                    ('16', 'Digitador'),
                    ('17', 'Divulgador de Campanha'),
                    ('18', 'Motorista'),
                    ('19', 'Parlamentar / Usuário'),
                    ('20', 'Supervisor de Campanha'),
)

# PESSOA_GRUPO é pra ser foreingkey
SOLICITACAO_ASSUNTO  = (
                           ('1', 'Asfalto, Calçada e Patrolamento'),
                    ('2', 'Auxilio Doença'),
                    ('3', 'Auxílio Alimentação'),
                    ('4', 'Auxílio Funeral'),
                    ('5', 'Assessor Jurídico'),
                    ('6', 'Encaminhamento Médico'),
                    ('7', 'Iluminação Pública'),
                    ('8', 'Instalação de Creches e Escolas'),
                    ('9', 'Patrocínio Cultural'),
                    ('10', 'Patrocínio Esportivo'),
                    ('11', 'Pedidos Filantrópicos'),
                    ('12', 'Placas, Lombadas e Sinais'),
                    ('13', 'Poda de Árvore'),
                    ('14', 'Saneamento, Água e Esgoto'),
                    ('15', 'Segurança Pública'),
                    ('16', 'Transporte Coletivo'),
                    ('17', 'Vaga em Escolas e Creches'),
)

SOLICITACAO_STATUS = (
                    ('1', 'Andamento'),
                    ('2', 'Concluído'),
                    ('3', 'Encaminhado'),
                    ('4', 'Pendente'),
)

SOLICITACAO_PRIORIDADE = (
                 ('1', 'Normal'),
                 ('2', 'Alta'),
                 ('3', 'Baixa'),
)

SOLICITACAO_TIPO = (
    ('1', 'Pessoal'),
     ('2', 'Email'),
                 ('3', 'Fax'),
                 ('4', 'Ofício'),
                 ('5', 'Por Terceiros'),
                 ('6', 'SMS'),
                 ('5', 'Whatsapp'),
)

ATENDIMENTO_STATUS = (
                         ('1', 'Aguardando'),
                    ('2', 'Encaminhado'),
                    ('3', 'Atendimento'),
)
