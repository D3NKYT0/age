__prefixo__ = "age_"

__title__ = "Conecta Age"

__terms_of_service__ = "https://github.com/D3NKYT0/age/blob/master/LICENSE"

__description__ = """
A ConectaAGE é uma api em desenvolvimento (atualmente) para AGE-PE afim de intercomunicar suas aplicações WEB/MOBILE com a agencia.

## Caracteristicas

 - Você pode **em breve...**.

## Recursos

Você será habilitado à:

* **Em Breve...** (_não implementado_).
"""

__tags_metadata__ = [
    {
        "name": "users",
        "description": "Operações com Usuarios. Necessário **login** para acessar esses recursos.",
    },
    {
        "name": "clients",
        "description": "Operações com clientes. Necessário **login** para acessar esses recursos.",
    },
    {
        "name": "ti",
        "description": "Operações da TI. Necessário **login** para acessar esses recursos.",
    },
    {
        "name": "auth",
        "description": "Área de Autorização. Então _Auth_ têm seu próprio documento.",
        "externalDocs": {
            "description": "doc externa",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

__contact__ = {
        "name": "Daniel Amaral",
        "url": "https://github.com/D3NKYT0/age",
        "email": "danielamaral.f@age.pe.gov.br",
    }

__license_info__ = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }

# origins
origins = [
    'http://localhost:3000'  # teste local
]


authotizations = {
    "15": "root",
    "16": "admin",
    "17": "user",
    "18": "reader",
    "19": "manager",
    "25": "system"
}
