[![CICD](https://github.com/nogibjj/arko_dockerized_app/actions/workflows/CICD.yml/badge.svg)](https://github.com/nogibjj/arko_dockerized_app/actions/workflows/CICD.yml)
# Calculator App with Docker

This is a simple calculator web application built with Flask and Docker. The app provides basic arithmetic operations (addition, subtraction, multiplication, division) via a RESTful API. It is containerized using Docker for easy deployment and scalability.

## Features

- **Basic calculator functionality**: Add, subtract, multiply, and divide.
- **REST API**: Provides endpoints to perform calculations.
- **Dockerized**: The app is containerized with Docker for easy deployment and management.
- **CI/CD**: Uses GitHub Actions to automate building, testing, and pushing the Docker image to Docker Hub.

![image](https://github.com/user-attachments/assets/953778af-18e1-40a6-9e20-a1aefa031ea0)
![image](https://github.com/user-attachments/assets/c7199c70-d1c5-4847-a2e3-5ba316541152)
![image](https://github.com/user-attachments/assets/68ea8311-c649-48a3-b5d8-5f926b90388f)

## Docker Image Link
https://hub.docker.com/r/arko0/calculator_app

## Prerequisites

Before getting started, make sure you have the following installed:

- **Docker**: To build and run the containerized app.
- **Python 3.x**: To install dependencies and run tests.
- **Make**: For managing the build and deployment process.

## Installation and Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/calculator-app.git
   cd calculator-app
   ```
2. **Run locally**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
3. **Docker run**
   ```bash
   make deploy
   ```
