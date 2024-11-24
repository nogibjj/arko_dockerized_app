# Install dependencies
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

# Format code using black
format:	
	black app.py tests/*.py

# Lint code using ruff
lint:
	ruff check app.py tests/*.py

# Build the Docker image
build:
	docker build -t arko0/calculator_app:latest -f .devcontainer/Dockerfile .

# Run the Docker container
run:
	docker run -d -p 5000:5000 --name calculator_app_container arko0/calculator_app:latest

# Stop and remove the Docker container
stop:
	@docker stop calculator_app_container 2>/dev/null || true
	@docker rm calculator_app_container 2>/dev/null || true

# Push the Docker image to Docker Hub
push:
	docker push arko0/calculator_app:latest

# Deploy the application (stop existing container, build and run a new one)
deploy: stop build run
	@echo "Application is running at http://localhost:5000"

# Run tests
test:
	python tests/test_calculator.py
