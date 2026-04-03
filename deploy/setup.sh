#!/usr/bin/env bash
set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────────
#  SNA Academy — Ubuntu Server Setup Script
#  Run as:  sudo bash deploy/setup.sh
# ──────────────────────────────────────────────────────────────────────────────

DOMAIN="snaacademy.com"
APP_DIR="/var/www/premium_academy"
DB_NAME="snaacademy"
DB_USER="snaacademy_user"
STATIC_DIR="/var/www/snaacademy/static"
MEDIA_DIR="/var/www/snaacademy/media"

echo "============================================="
echo "  SNA Academy — Server Setup"
echo "============================================="

# ── 1. System packages ────────────────────────────────────────────────────────
echo ""
echo "[1/8] Installing system packages..."
apt update
apt install -y python3-pip python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl git ufw

# ── 2. PostgreSQL ─────────────────────────────────────────────────────────────
echo ""
echo "[2/8] Setting up PostgreSQL..."
read -sp "Enter password for database user '${DB_USER}': " DB_PASS
echo ""

sudo -u postgres psql -tc "SELECT 1 FROM pg_roles WHERE rolname='${DB_USER}'" | grep -q 1 || \
    sudo -u postgres psql -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASS}';"

sudo -u postgres psql -lqt | cut -d '|' -f 1 | grep -qw ${DB_NAME} || \
    sudo -u postgres psql -c "CREATE DATABASE ${DB_NAME} OWNER ${DB_USER};"

echo "   Database '${DB_NAME}' and user '${DB_USER}' ready."

# ── 3. Application user & directory ──────────────────────────────────────────
echo ""
echo "[3/8] Setting up application directory..."
id -u snaacademy &>/dev/null || useradd -m -s /bin/bash snaacademy

mkdir -p ${APP_DIR}
mkdir -p ${STATIC_DIR}
mkdir -p ${MEDIA_DIR}

chown -R snaacademy:snaacademy ${APP_DIR}
chown -R www-data:www-data ${STATIC_DIR}
chown -R www-data:www-data ${MEDIA_DIR}

echo "   Directory structure created."

# ── 4. Python virtualenv & dependencies ──────────────────────────────────────
echo ""
echo "[4/8] Installing Python dependencies..."
sudo -u snaacademy python3 -m venv ${APP_DIR}/venv
${APP_DIR}/venv/bin/pip install --upgrade pip
${APP_DIR}/venv/bin/pip install -r ${APP_DIR}/requirements.txt

echo "   Python dependencies installed."

# ── 5. .env file ─────────────────────────────────────────────────────────────
echo ""
echo "[5/8] Generating .env file..."
SECRET_KEY=$(${APP_DIR}/venv/bin/python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")

cat > ${APP_DIR}/.env << ENVFILE
DJANGO_SETTINGS_MODULE=config.settings
DEBUG=False
SECRET_KEY=${SECRET_KEY}
ALLOWED_HOSTS=${DOMAIN},www.${DOMAIN},localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=${DB_NAME}
DB_USER=${DB_USER}
DB_PASSWORD=${DB_PASS}
DB_HOST=localhost
DB_PORT=5432

GUNICORN_WORKERS=3
GUNICORN_BIND=127.0.0.1:8000

STATIC_ROOT=${STATIC_DIR}
MEDIA_ROOT=${MEDIA_DIR}

SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
ENVFILE

chown snaacademy:snaacademy ${APP_DIR}/.env
chmod 600 ${APP_DIR}/.env
echo "   .env created with generated SECRET_KEY."

# ── 6. Django management commands ────────────────────────────────────────────
echo ""
echo "[6/8] Running Django migrations & collecting static files..."
${APP_DIR}/venv/bin/python ${APP_DIR}/manage.py migrate --settings=config.settings
${APP_DIR}/venv/bin/python ${APP_DIR}/manage.py collectstatic --noinput --settings=config.settings

echo "   Migrations & static files done."

# ── 7. Gunicorn systemd service ──────────────────────────────────────────────
echo ""
echo "[7/8] Configuring Gunicorn service..."
cp ${APP_DIR}/deploy/gunicorn.socket /etc/systemd/system/gunicorn.socket
cp ${APP_DIR}/deploy/gunicorn.service /etc/systemd/system/gunicorn.service

systemctl daemon-reload
systemctl enable gunicorn.socket
systemctl start gunicorn.socket

echo "   Gunicorn socket activated."

# ── 8. Nginx ─────────────────────────────────────────────────────────────────
echo ""
echo "[8/8] Configuring Nginx..."
cp ${APP_DIR}/deploy/snaacademy_nginx.conf /etc/nginx/sites-available/snaacademy
ln -sf /etc/nginx/sites-available/snaacademy /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default

nginx -t && systemctl restart nginx

echo "   Nginx configured and restarted."

# ── Firewall ─────────────────────────────────────────────────────────────────
echo ""
echo "Configuring firewall..."
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable

echo ""
echo "============================================="
echo "  Setup Complete!"
echo "============================================="
echo ""
echo "  Site:       http://${DOMAIN}"
echo "  Admin:      http://${DOMAIN}/admin/"
echo "  App dir:    ${APP_DIR}"
echo "  Static:     ${STATIC_DIR}"
echo "  Media:      ${MEDIA_DIR}"
echo ""
echo "  Next steps:"
echo "    1. Add your domain DNS A record to this server's IP"
echo "    2. Set up SSL with:  sudo certbot --nginx -d ${DOMAIN} -d www.${DOMAIN}"
echo "    3. Create a superuser:"
echo "       sudo -u snaacademy ${APP_DIR}/venv/bin/python ${APP_DIR}/manage.py createsuperuser"
echo ""
echo "  Useful commands:"
echo "    sudo systemctl status gunicorn"
echo "    sudo systemctl restart gunicorn"
echo "    sudo journalctl -u gunicorn"
echo "    sudo systemctl status nginx"
echo "    sudo nginx -t && sudo systemctl reload nginx"
echo ""
