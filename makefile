install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:	
	black app.py tests/*.py

lint:
	ruff check app.py tests/*.py

build:
	docker build -t calculator_app -f .devcontainer/Dockerfile .

run:
	docker run -d -p 5000:5000 --name calculator_app_container calculator_app

stop:
	@docker stop calculator_app_container 2>/dev/null || true
	@docker rm calculator_app_container 2>/dev/null || true

deploy: stop build run
	@echo "Application is running at http://localhost:5000"

test:
	python tests/test_calculator.py
