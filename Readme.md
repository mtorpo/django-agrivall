
Configuración dependencias servidor Ubuntu 24.04

# ==================================
# Proyecto Web Agrivall - DAW
## Ecommerce, blogs y reserva online casa rural
# ==================================

### Puesta en marcha de la web


Configuración dependencias servidor Ubuntu 24.04

### 1. ACTUALIZAR SISTEMA
sudo apt update
sudo apt upgrade -y


### 2. INSTALAR DEPENDENCIAS DEL SISTEMA
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



### 3. INICIAR DOCKER
sudo systemctl enable docker
sudo systemctl start docker

# opcional
sudo usermod -aG docker $USER


### 4. COMPROBAR INSTALACIÓN
python3 --version
pip3 --version
git --version
node --version
npm --version
docker --version
docker compose version


### 5. CLONAR PROYECTO
cd /opt/proyectos

git clone URL_REPO_PRIVADO

cd django-agrivall


### 6. LEVANTAR MYSQL (Y OTROS SERVICIOS)
(Primero pas amos el .env para las variables de creación de la BDD)
docker compose up -d


### 7. CREAR Y ACTIVAR ENTORNO VIRTUAL
python3 -m venv env
source env/bin/activate


### 8. INSTALAR DEPENDENCIAS PYTHON
pip install --upgrade pip
pip install -r requirements.txt


### 9. INSTALAR FRONTEND
npm install


### 10. PREPARAR DJANGO
python manage.py migrate
python manage.py collectstatic


### 11. ABRIR PUERTO DE PRUEBA
sudo ufw allow OpenSSH
sudo ufw allow 8000/tcp
sudo ufw enable


### 12. ARRANCAR DJANGO
python manage.py runserver 0.0.0.0:8000
