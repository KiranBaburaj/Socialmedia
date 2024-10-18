# Social Media Backend

## Overview

This repository is the backend for a social media platform built using **Django** and **Django REST Framework**. It provides API endpoints for user authentication, profile management, room creation, and WebSocket-based real-time communication.

## Technologies Used :

- **Django**: Web framework for backend.
- **Django REST Framework**: For building RESTful APIs.
- **Django Channels**: For handling WebSockets.
- **JWT**: For secure authentication.
- **Redis**: For WebSocket message handling.

## Features

- User Registration and Authentication (JWT-based)
- Room Creation
- Real-time WebSocket Messaging
- API Endpoints for User and Profile Management

## Prerequisites

- **Python 3.x**
- **Redis**: Required for WebSocket messaging.
- **PostgreSQL** (or any other database of your choice).

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KiranBaburaj/Socialmedia.git
   cd Socialmedia





2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root and set variables such as:
   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=your_database_url
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start Redis server** (ensure Redis is installed):
   ```bash
   redis-server
   ```

7. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

## Running Tests

To run the tests:
```bash
python manage.py test
```

## Deployment

To deploy the application, you can use platforms like **Heroku**, **AWS**, or **DigitalOcean**. Make sure to configure the environment variables and Redis on the deployment server.


