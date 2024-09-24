# IBM-MQ

## Modo de uso

### Criar Fila
Crie o diretório onde o container será iniciado, e garanta suas permissões:
```sh
mkdir mqdata
chmod -R 777 ./mqdata
```

Suba o container.
```sh
docker-compose up -d
```

Cheque se o container está pronto para uso.
```sh
docker ps
```

Uma mensagem como esta deve ser exibida:
```
CONTAINER ID   IMAGE              COMMAND            CREATED          STATUS          PORTS                                                                                            NAMES
e357b2ba61ee   ibmcom/mq:latest   "runmqdevserver"   10 minutes ago   Up 10 minutes   0.0.0.0:1414->1414/tcp, :::1414->1414/tcp, 0.0.0.0:9443->9443/tcp, :::9443->9443/tcp, 9157/tcp   ibm-mq-container
```

Acesse o terminal bash dentro do container.
```sh
docker exec -it ibm-mq-container /bin/bash
```

Os seguintes comando são usados para criar, listar e deletar filas.
```sh
echo "DEFINE QLOCAL('QM1')" | runmqsc QM1
echo "DISPLAY QUEUE('QM1')" | runmqsc QM1
echo "DELETE QLOCAL('QM1')" | runmqsc QM1
```