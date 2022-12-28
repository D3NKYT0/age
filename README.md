# ConectaAGE [0.0.12.1](http://192.168.0.100:8000/docs)

<img align="right" height="180" src="https://i.imgur.com/buvNhRO.png"/>

A ConectaAGE é uma api em desenvolvimento (atualmente) para AGE-PE afim de intercomunicar suas aplicações WEB/MOBILE com a agencia.

O projeto utiliza os frameworks FastAPI/SQLAlchemy/Alembic para seu núcleo de programação (demais requerimentos disponiveis no repositorio)

FastAPI é uma estrutura da Web moderna, rápida (de alto desempenho) para criar APIs com Python 3.7+ com base em dicas de tipo Python padrão.

SQLAlchemy é o kit de ferramentas Python SQL e Object Relational Mapper (ORM) que oferece aos desenvolvedores de aplicativos todo o poder e flexibilidade do SQL.

Alembic é uma ferramenta leve de migração de banco de dados para uso com o SQLAlchemy Database Toolkit for Python.

[![GitHub stars](https://img.shields.io/github/stars/D3NKYT0/age.svg?style=social&label=Stars&style=flat)](https://github.com/D3NKYT0/age/stargazers)
[![GitHub license](https://img.shields.io/github/license/D3NKYT0/age.svg)](https://github.com/D3NKYT0/age/blob/master/LICENSE)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/fastapi.svg)](#Installation)
<p align="center">
<img height="280" src="https://i.imgur.com/jv0Bmy3.png">
</p>


## Como iniciar

```bash
uvicorn src.server:app --reload --reload-dir=src --host 0.0.0.0
```


## Como versionar o banco de dados (PostgreSQL)

```bash
alembic revision --autogenerate -m "foo"
alembic upgrade head
```

## Estrutura do banco de dados

<img height="600" src="https://i.imgur.com/he4JtDN.png">

## Como testar (temporario / localhost)

```bash
http://192.168.0.100:8000/docs
```


## Sobre Mim
>Programador da AGE de Pernambuco - Daniel Amaral (29 Anos) Recife/PE
- Email: danielamaral.f@age.pe.gov.br
- Criado por: Denky#9370🤴 (discord)


## Grupo de Staffs:

**Núcleo de Programação**

- Denky#9370 (Daniel Amaral)
- Renan Nere

**Infraestrutura**

- Ailton Junior
- Renan Nere 

**Designers e Ilustradores**

- George Uamirin

**Scripts da IA**

- Denky#9370 (Daniel Amaral)
 
 **Superintedencia**

 - Vinicius Amelotti
 