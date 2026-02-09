#!/bin/bash

BACKUP_DIR="/backups"
mkdir -p $BACKUP_DIR

echo "Porneste serviciul de backup automat..."

while true; do
    DATE=$(date +"%Y-%m-%d_%H-%M-%S")
    FILENAME="$BACKUP_DIR/db_backup_$DATE.sql"

    echo "Incepe salvarea bazei de date..."
    
    export PGPASSWORD=$DB_PASSWORD
    pg_dump -h db -U $DB_USER $DB_NAME > $FILENAME

    if [ $? -eq 0 ]; then
        echo "Backup reusit!!!: $FILENAME"
    else
        echo "Eroare la backup!"
    fi

    find $BACKUP_DIR -type f -mmin +5 -name "*.sql" -delete

    echo "SLEEP 60 de secunde..."
    sleep 60
done