
Configuración dependencias servidor Ubuntu 24.04

# ==================================
# ACTUALIZAR SISTEMA
# ==================================

sudo apt update
sudo apt upgrade -y


# ==================================
# INSTALAR DEPENDENCIAS DEL SISTEMA
# ==================================

sudo apt install -y \
git \
python3 \
python3-venv \
python3-pip \
python3-dev \
build-essential \
pkg-config \
default-libmysqlclient-dev \
nodejs \
npm \
ufw \
docker.io \
docker-compose-v2


# ==================================
# INICIAR DOCKER
# ==================================

sudo systemctl enable docker
sudo systemctl start docker

# opcional: ejecutar docker sin sudo
sudo usermod -aG docker $USER


# ==================================
# COMPROBAR INSTALACIÓN
# ==================================

python3 --version
pip3 --version
git --version
node --version
npm --version
docker --version
docker compose version


# ==================================
# CLONAR PROYECTO
# ==================================

cd /opt/proyectos

git clone URL_REPO_PRIVADO

cd django-agrivall


# ==================================
# LEVANTAR MYSQL (Y OTROS SERVICIOS)
# ==================================
(Primero pas amos el .env para las variables de creación de la BDD)
docker compose up -d


# ==================================
# CREAR Y ACTIVAR ENTORNO VIRTUAL
# ==================================

python3 -m venv env
source env/bin/activate


# ==================================
# INSTALAR DEPENDENCIAS PYTHON
# ==================================

pip install --upgrade pip
pip install -r requirements.txt


# ==================================
# INSTALAR FRONTEND
# ==================================

npm install


# ==================================
# PREPARAR DJANGO
# ==================================

python manage.py migrate
python manage.py collectstatic


# ==================================
# ABRIR PUERTO DE PRUEBA
# ==================================

sudo ufw allow OpenSSH
sudo ufw allow 8000/tcp
sudo ufw enable


# ==================================
# ARRANCAR DJANGO
# ==================================

python manage.py runserver 0.0.0.0:8000
