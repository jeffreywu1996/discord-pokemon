APP_NAME := pokemon

build:
	docker build -t ${APP_NAME} .

run:
	docker run -it ${APP_NAME}
