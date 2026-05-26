#!/bin/bash
set -e

echo "Bajando contenedores..."
docker compose down -v

echo "Borrando migraciones excepto __init__.py..."
find ./agrivall/migrations -type f -name "*.py" ! -name "__init__.py" -delete

echo "Borrando cache de Python..."
rm -rf ./agrivall/migrations/__pycache__

echo "Vaciando carpeta media..."
find ./media -type f -delete 2>/dev/null || true

echo "Arrancando contenedores..."
docker compose up -d

sleep 10

echo "Creando migraciones..."
python manage.py makemigrations

sleep 5

echo "Ejecutando migraciones..."
python manage.py migrate

sleep 5

echo "Ejecutando seed..."
python manage.py seed

sleep 5

echo "Creando superuser..."

export DJANGO_SUPERUSER_USERNAME=mtormos
export DJANGO_SUPERUSER_PASSWORD=mtormos
export DJANGO_SUPERUSER_EMAIL=mtormos@example.com

python manage.py createsuperuser --noinput || true

echo "Listo."