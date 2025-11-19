# 1. Base Image: Começa com uma imagem oficial slim do Python 3
FROM python:3.9-slim

# 2. Working Directory: Define onde o código ficará dentro do container
WORKDIR /app

# 3. Copy Code: Copia o seu script Python para o container
COPY check_status.py /app/

# 4. Entrypoint: Comando para rodar a aplicação quando o container iniciar
CMD ["python3", "check_status.py"]