# DogHouse API


API desenvolvida com o intuito de adicionar, visualizar, atualizar e remover informações dos animais para adoção da Ong DogHouse.

***

Antes de começar é necessário a criação e ativação de uma VirtualEnv com Python 3.6.0, recomendo a utilização do pyenv.

Após isso, vá para a pasta raiz desse projeto (Concil_python_backend) e siga as instruções abaixo:

1. Instale os requisitos do projeto:

    ```bash
    $ make requirements_dev
    ```

2. Para aplicar as definições do modelo no banco:
    ```bash
    $ make migrate_db
    ```

3. Para subir a API utilize:
    ```bash
    $ make runserver
    ```

***
**4. Testando com curl:**
- Adiciona um animal:

   ```bash
    $ curl -X POST http://localhost:8000/animals/ -H "Content-Type: application/json" -d '{"name": "Ada","specie": "cat","gender": "female","age": "kitten","size": "small","hair": "short","color": "preto","description": "cute cat loves human","address": "SP","adopted": false}'
    ```

- Retorna todas os animais:

    - request:

    ```bash
    $ curl -X GET http://localhost:8000/animals/
    ```

    ou
    ```bash
    $ curl -X GET http://localhost:8000/animals/ | python -m json.tool
    # pretty view
    ```

    - response:

    ```bash
    [
    {
        "address": "SP",
        "age": "kitten",
        "color": "preto",
        "description": "cute cat loves human",
        "gender": "female",
        "hair": "short",
        "id": 1,
        "name": "Ada",
        "size": "small",
        "specie": "cat",
        "adopted": false
    },
    {
        "address": "SP",
        "age": "young",
        "color": "preto",
        "description": "cute cat loves human",
        "gender": "female",
        "hair": "long",
        "id": 2,
        "name": "Lovelace",
        "size": "small",
        "specie": "cat",
        "adopted": false
    }
    ]
    ```

- Retorna um animal em específico utilizando `id`:

    - request:

    ```bash
    $ curl -X GET http://localhost:8000/animals/1/
    ```

    ou

    ```bash
    $ curl -X GET http://localhost:8000/animals/1/ | python -m json.tool
    # pretty view
    ```

    - response

    ```bash
    {
        "address": "SP",
        "adopted": false,
        "age": "kitten",
        "color": "preto",
        "description": "cute cat loves human",
        "gender": "female",
        "hair": "short",
        "id": 1,
        "name": "Ada",
        "size": "small",
        "specie": "cat"
    }
    ```

- Atualiza um animal em específico utilizando `id`:

    ```bash
    $ curl -X PUT  http://localhost:8000/animals/1/ -H "Content-Type: application/json" -d '{"name": "Lovelace","specie": "cat","gender": "female","age": "kitten","size": "small","hair": "short","color": "preto","description": "adopted","address": "SP","adopted": true}'
    ```

- Remove um animal em específico utilizando `id`:

    ```bash
    $ curl -X DELETE  http://localhost:8000/animals/1/
    ```

***

5. Para executar os testes unitários utilize:

    ```bash
    $ make unit
    ```
