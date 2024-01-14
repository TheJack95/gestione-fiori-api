# Usa un'immagine di base con Python
FROM python:3.10

# Imposta l'ambiente di produzione per Django
ENV DJANGO_SETTINGS_MODULE=gestionefiori.settings.production

# Imposta la variabile d'ambiente PYTHONUNBUFFERED in modo che Python output sia inviato direttamente sulla console senza buffering
ENV PYTHONUNBUFFERED 1

# Crea una directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt nella directory del container
COPY requirements.txt /app/

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice sorgente del progetto nella directory del container
COPY . /app/

# Esponi la porta su cui il server Django sarà in ascolto
EXPOSE 8000

# Esempio di comando per eseguire le migrazioni e avviare il server Django
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]