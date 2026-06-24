FROM python:3.11-slim

WORKDIR /app

RUN useradd -m agentuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le projet (y compris j18-VOCR (1).json car il n'est pas dans .gitignore)
COPY . .

RUN chown -R agentuser:agentuser /app
USER agentuser

EXPOSE 8000

# L'application va démarrer et lire les variables d'environnement du système conteneurisé
CMD ["python", "tests/test-agent.py"]