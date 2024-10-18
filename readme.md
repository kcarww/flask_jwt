# Projeto Flask com JWT e PyMysql para a turma do super módulo da INFINITY SCHOOL
Este é um projeto básico Flask que utiliza PyMySQL para integração com o banco de dados MySQL e JWT (JSON Web Tokens) para autenticação. O projeto inclui instruções para configurar um ambiente virtual, instalar as dependências necessárias e criar o banco de dados através do arquivo db.sql.

### Pré-requisitos
Certifique-se de ter o seguinte instalado antes de configurar o projeto:

- **Python 3.12** (https://www.python.org/downloads/)
- **MySQL** (https://dev.mysql.com/downloads/installer/)
- **pip** (já incluído no Python 3.12)


Passo a Passo de Configuração


### 1. Clone o Repositório
Clone o repositório do projeto para sua máquina local.

### 2. Crie um Ambiente Virtual

``` bash
    python -m venv venv
```

### 3. Ative o Ambiente Virtual
Ative o ambiente virtual recém-criado.

``` bash
    venv\Scripts\activate
```

### 4. Instale as Dependências
Com o ambiente virtual ativo, instale as bibliotecas necessárias usando o requirements.txt.

``` bash
    python -r requirements.txt
```

### 5. Crie o banco de dados
Execute o script do arquivo db.sql no seu SGBD mysql

### 6. Execute o projeto
``` bash
    flask run
```