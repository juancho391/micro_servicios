Microservices Application (Users, Products, Cart)

This is my first microservices project, still in progress. The application consists of three services: Users, Products, and Cart. Each service is containerized using Docker and orchestrated with Docker Compose. The goal of this project is to learn and practice microservices architecture, Docker, and Docker Compose.

This project simulates a basic e-commerce system where:

Users can register and authenticate.
Products can be listed and added to the cart.
The Cart service interacts with both the Users and Products services, allowing authenticated users to add products to their cart.
The services communicate through HTTP requests and are isolated in separate containers.

Services

Users Service: Handles user registration and authentication (JWT tokens).
Products Service: Manages the product catalog, allowing users to view available products.
Cart Service: Allows users to add products to their cart. It requires the authentication token provided by the Users Service.
Technologies

Backend: Python, Django Rest Framework, JWT
Databases: SQLite (will migrate to PostgreSQL or MySQL)
Containers: Docker, Docker Compose

Project Structure

├── services/
│   ├── users/        # Users service
│   ├── products/     # Products service
│   └── cart/         # Cart service
├── docker-compose.yml
└── README.md
Setup

To get started with this project, you need to have Docker and Docker Compose installed.

Steps:
Clone this repository:
git clone https://github.com/yourusername/microservices-ecommerce.git
cd microservices-ecommerce
Build and run the services using Docker Compose:
docker-compose up --build
The services should now be running. You can interact with them via their respective endpoints.

you can visit this url : "api/schema/swagger-ui/" to check the API documentation.
