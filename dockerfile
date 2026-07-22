FROM python:3.11-slim

# System packages needed for PDF handling and common imaging libs
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential git libglib2.0-0 libsm6 libxext6 libxrender1 libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync
 
COPY . .

CMD ["uv", "run", "python", "app.py"]