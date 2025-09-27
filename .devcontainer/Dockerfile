FROM python:3.10-bookworm

RUN apt-get update && apt-get install -y curl && \
    sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- -y && \
    echo 'eval "$(starship init bash)"' >> ~/.bashrc

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

