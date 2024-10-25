# **App Clientes**
Este projeto é destinado ao gerenciamento de informações de clientes. Ele inclui scripts em Python para lidar com interações no banco de dados e templates HTML para renderizar a interface front-end.

### Estrutura do Projeto
- app_clients.py: Script principal que lida com as operações de clientes.
- app_clients_db.py: Contém os detalhes da conexão MySQL e funções de banco de dados.
t- emplates/: Pasta que contém os templates HTML para a interface web.

### Requisitos
- Python 3.x
- MySQL (Versão: 8.0.39)
- *Opicional: Testado em Ubuntu 24.04 LTS usando virtual environment (Link para ajudar na configuração:https://hostman.com/tutorials/how-to-install-python-and-pip-on-ubuntu-24-04/)
- *Opicional o uso de MySQL Workbench para gerir o banco. Caso use, execute esse comando para criação da tabela clientes e todos os campos necessários:
```USE db_users;

CREATE TABLE clientes ( 
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NOME VARCHAR(255),
    EMAIL VARCHAR(255),
    IDADE VARCHAR(255),
    CIDADE VARCHAR(255),
    CPF VARCHAR(255)
);
```


### Configuração
- Clone o repositório.
- Instale os pacotes Python necessários.
- Configure a conexão MySQL no arquivo app_clients_db.py.

### Uso
- Execute o arquivo app_clients.py para iniciar a aplicação.
