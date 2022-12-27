__prefixo__ = "age_"

__title__ = "Conecta Age"

__terms_of_service__ = "https://github.com/D3NKYT0/age/blob/master/LICENSE"

__description__ = """
A ConectaAGE é uma api em desenvolvimento (atualmente) para AGE-PE afim de intercomunicar suas aplicações WEB/MOBILE com a agencia.

## Caracteristicas

 - Você pode **cadastrar clientes**.
 - Você pode **cadastrar clientes**.
 - Você pode **cadastrar clientes**.
 - Você pode **cadastrar clientes**.
 - Você pode **cadastrar clientes**.
 - Você pode **cadastrar clientes**.

## Recursos

Você será habilitado à:

* **Criar Usuarios** (_não implementado_).
* **Ler Usuarios** (_não implementado_).
"""

__tags_metadata__ = [
    {
        "name": "usuarios",
        "description": "Operações com usuários. Necessário **login** para acessar esses recursos.",
    },
    {
        "name": "produtos",
        "description": "Operações com produtos. Necessário **login** para acessar esses recursos.",
    },
    {
        "name": "pedidos",
        "description": "Operações com pedidos. Necessário **login** para acessar esses recursos.",
    },
    {
        "name": "email",
        "description": "Operações com email. Necessário **login** para acessar esses recursos.",
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
