# Flask Docker App

This is a simple Flask web application that is Dockerized. It runs a basic web server that returns "Hello, World!" when accessed.

## Prerequisites

- Docker
- Git
- Kubernetes (for orchestration demo)

## How to Build the Docker Image

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-docker-app.git
    cd flask-docker-app
    ```

2. Build the Docker image:

    ```bash
    docker build -t flask-app .
    ```

3. Run the Docker container:

    ```bash
    docker run -p 5000:5000 flask-app
    ```

    You can access the app at [http://localhost:5000](http://localhost:5000).

## Kubernetes Setup (Optional)

1. Apply the deployment and service YAMLs to Kubernetes:

    ```bash
    kubectl apply -f kubernetes/deployment.yaml
    kubectl apply -f kubernetes/service.yaml
    ```

2. Access the app through the exposed service.

## License

This project is licensed under the MIT License.
