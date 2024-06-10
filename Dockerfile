# Use a base image mínima do Python
FROM python:3.9.5

# Defina variáveis de ambiente para o pyenv
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Instale dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    make \
    build-essential \
    libssl-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instale pyenv
RUN curl https://pyenv.run | bash

# Instale a versão do Python especificada no pyproject.toml
COPY pyproject.toml poetry.lock /app/
WORKDIR /app
RUN pyenv install $(grep -E '^python = ' pyproject.toml | cut -d'"' -f2) && \
    pyenv global $(grep -E '^python = ' pyproject.toml | cut -d'"' -f2)

# Instale o Poetry
RUN curl -sSL https://install.python-poetry.org | python -

# Adicione Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Instale dependências do projeto
RUN poetry install --no-root

# Copie o restante do código do projeto
COPY . /app

# Comando para iniciar o servidor
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
