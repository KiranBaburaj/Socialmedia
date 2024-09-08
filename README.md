# Socialmedia

# Django WebSocket and JWT Authentication Backend

## Overview

This backend is built using **Django** and **Django Channels** to provide API endpoints for user registration, authentication (JWT), real-time communication via WebSockets, and room creation. It is a part of a full-stack application with a React frontend.

## Technologies Used

- **Python**: Backend programming language.
- **Django**: Web framework for building the backend.
- **Django Rest Framework (DRF)**: For creating APIs.
- **Django Channels**: For WebSocket support and real-time communication.
- **JWT (JSON Web Tokens)**: For user authentication.
- **Redis**: Used as the channel layer for WebSocket handling.

## Features

- User Registration (via REST API)
- User Login (via REST API with JWT Authentication)
- WebSockets for real-time communication
- Room creation and management for WebSocket communication

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Redis (for handling WebSocket communication)

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd backend
