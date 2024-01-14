# Usa l'immagine ufficiale di MySQL
FROM mysql:latest

# Imposta le variabili d'ambiente per il database
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=gestione-fiori

# Esponi la porta su cui il database sarà in ascolto
EXPOSE 3306

# Opzionale: copia uno script SQL per eseguire operazioni iniziali sul database, se necessario
# COPY ./script.sql /docker-entrypoint-initdb.d/

# Esempio di comando per avviare il container
CMD ["mysqld"]