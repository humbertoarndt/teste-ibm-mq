# Define o nome da pasta
MQDATA_DIR = mqdata

# Tarefa padrão
all: create_mqdata docker_up

# Tarefa para criar a pasta mqdata
create_mqdata:
	@echo "Criando a pasta '$(MQDATA_DIR)'..."
	mkdir -p $(MQDATA_DIR)
	@echo "Definindo permissões 777 para a pasta '$(MQDATA_DIR)'..."
	chmod -R 777 $(MQDATA_DIR)
	@echo "Pasta '$(MQDATA_DIR)' criada e permissões definidas."

# Tarefa para subir o docker-compose
docker_up:
	@echo "Subindo o Docker Compose..."
	docker-compose up -d

# Tarefa para limpar
clean:
	@echo "Removendo a pasta '$(MQDATA_DIR)'..."
	sudo rm -rf $(MQDATA_DIR)
	@echo "Pasta '$(MQDATA_DIR)' removida."
	@echo "Parando e removendo os containers do Docker Compose..."
	docker-compose down
