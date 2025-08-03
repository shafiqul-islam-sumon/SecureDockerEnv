# SecureDockerEnv

![GitHub stars](https://img.shields.io/github/stars/shafiqul-islam-sumon/SecureDockerEnv?style=social)
![GitHub forks](https://img.shields.io/github/forks/shafiqul-islam-sumon/SecureDockerEnv?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/shafiqul-islam-sumon/SecureDockerEnv)

## 🚀 Overview

**SecureDockerEnv** is a Python-based project for **securely managing environment variables in Docker**. It ensures that **sensitive credentials** are never embedded in Docker images while providing a **safe and efficient way to inject `.env` files at runtime**. This project follows **Docker security best practices** to **protect secrets, prevent accidental leaks, and enhance security in containerized applications**.

## ✨ Features

- **Secure management** of `.env` files in Docker.
- Prevents **sensitive credentials** from being embedded in images.
- Supports **Docker and Docker Compose** for flexible deployment.
- Implements **best security practices** for handling environment variables.

## 📥 Installation

To install and run SecureDockerEnv on your local machine:

1. Clone the repository:
   ```sh
   git clone https://github.com/shafiqul-islam-sumon/SecureDockerEnv.git
   cd SecureDockerEnv
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the project using Docker:
   ```sh
   docker build -t secure-docker-env .
   
   docker run --env-file .env secure-docker-env
   ```

## 🔒 Why You Should NOT Include `.env` Files in Docker Images (Security Risks)

- **Accidental Exposure in Shared Images**: `.env` files included in images can be accessed by anyone pulling the image.
- **Persistent Secrets in Image Layers**: Once embedded, secrets remain in previous layers even if deleted.
- **Static Secrets**: Hardcoded secrets require image rebuilding for updates.
- **Environment-Specific Configurations**: Embedding `.env` files makes it difficult to manage multiple environments.

## 🛠️ Secure Ways to Manage `.env` Files in Docker (Best Practices)

This project implements two secure approaches:

### 🐳 Using Docker (`--env-file`)

This method allows explicit control by dynamically passing the `.env` file at runtime.

#### **Step 1: Create a Secure `.env` File**
```sh
SLACK_BOT_TOKEN=your-slack-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
```

#### **Step 2: Write a Secure Dockerfile**
```dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y curl procps && \
    pip install -r requirements.txt

CMD ["python", "-u", "main.py"]
```

#### **Step 3: Exclude `.env` Using `.dockerignore`**
```plaintext
.env
```

#### **Step 4: Build and Run the Container**
```sh
docker build -t my-app .

docker run --env-file .env my-app
```

### 📦 Using Docker Compose (`env_file`)

This method simplifies environment management, especially for multi-container applications.

#### **Step 1: Create a `docker-compose.yml` File**
```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    env_file:
      - .env
```

#### **Step 2: Build and Run the Container**
```sh
# Build docker image
docker-compose build

# Run container
docker-compose up
```

## 📊 Docker (`--env-file`) vs. Docker Compose (`env_file`)

| Feature                 | Docker (`--env-file`)           | Docker Compose (`env_file`)                |
| ----------------------- | ------------------------------- | ------------------------------------------ |
| **Ease of Use**         | Requires manual `--env-file`    | Loads `.env` automatically                 |
| **Multiple Services**   | Best for single-container apps  | Ideal for multi-container apps             |
| **Explicit Control**    | Must pass `.env` each time      | Implicitly loads from `docker-compose.yml` |
| **Runtime Flexibility** | Allows dynamic `.env` selection | Requires modifying `docker-compose.yml`    |

## ✅ Best Practices

- Never include `.env` files in Docker images – Always use `.dockerignore`.
- Use `--env-file` for dynamic secret management – Useful for single-container deployments.
- **Use Docker Compose for multi-service environments** – Simplifies deployment.

## 🎯 Conclusion

By following these methods, **SecureDockerEnv** ensures `.env` files remain external to Docker images, enhancing security and flexibility. Choose `--env-file` for explicit control or Docker Compose for easier multi-container management.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch** (`feature-branch`).
3. **Commit your changes**.
4. **Push to GitHub** and create a **Pull Request**.

Feel free to submit issues and feature requests!

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 📚 References

For more details, check out:
- 🔗 [Protect Sensitive Information in Docker](https://shafiqulai.github.io/blogs/blog_1.html) (Full Blog Post)
- 🔗 [Docker Environment Variables Documentation](https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/)


