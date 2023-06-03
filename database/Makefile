IMG_NAME = postgres-image
CONTAINER_NAME = practice-01-postgres

app:
	@make build
	@make run
build:
	sudo docker build -t $(IMG_NAME) .
run:
	sudo docker run --name $(CONTAINER_NAME) -p 5432:5432 -d $(IMG_NAME)
install:
	sudo snap install docker