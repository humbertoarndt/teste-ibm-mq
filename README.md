# IBM MQ Producer e Consumer

## Descrição
Este projeto é um estudo que implementa uma aplicação de exemplo para produzir e consumir mensagens usando IBM MQ em um container Docker.

## Estrutura do projeto
- `/app`: Contém os arquivos da aplicação.
- `/testes`: Contém os testes unitários para producer e consumer.
- `/docs`: Documentação adicional e anotações gerais usadas para estudo.

## Como rodar o projeto
### 1_ Baixe o projeto.
```sh
git clone https://github.com/humbertoarndt/teste-ibm-mq.git teste-ibm-mq
```

### 2_ Acesse o diretório criado.
```sh
cd teste-ibm-mq
```

### 3_ Use o Makefile para subir o container IBM MQ.
```sh
make
```

### 4_ Acesse o terminal do container criado.
```sh
docker exec -it ibm-mq-container /bin/bash
```

### 5_ Crie uma nova fila no IBM MQ.
```sh
echo "DEFINE QLOCAL('minha_fila')" | runmqsc QM1
```

### 6_ Cheque se a fila foi criada.
```sh
echo "DISPLAY QLOCAL('minha_fila')" | runmqsc QM1
```

### 7_ Instale as dependências do programa (pymqi).
```sh
pip install -r requirements.txt
```

### 8_ Execute o script python para enviar uma mensagem à fila.
```sh
python -m app.producer "Sua mensagem aqui"
```

### 9_ Execute o script python para consumir a primeira mensagem na fila.
```sh
python -m app.consumer
```

### 10_ Execute o comando make clean para remover o diretório `mqdata` e derrubar o container IBM MQ.
```sh
make clean
```