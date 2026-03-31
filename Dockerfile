# 1. Image de base Python
FROM python:3.11-slim

# 2. On définit le répertoire de travail interne au serveur
WORKDIR /app

# 3. On copie le fichier requirements depuis le dossier backend local
COPY backend/requirements.txt .

# 4. Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie tout le contenu du dossier backend local vers le serveur
COPY backend/ .

# 6. Lancement de l'application
# (main:app car main.py sera maintenant à la racine de /app sur le serveur)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]