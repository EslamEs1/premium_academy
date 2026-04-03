#!/usr/bin/env bash
set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────────
#  SNA Academy — Quick Deploy / Update Script
#  Run on the server after pulling new code:
#    sudo bash deploy/deploy.sh
# ──────────────────────────────────────────────────────────────────────────────

APP_DIR="/var/www/premium_academy"

echo "[deploy] Pulling latest code..."
sudo -u snaacademy git -C ${APP_DIR} pull origin main

echo "[deploy] Installing/updating Python dependencies..."
${APP_DIR}/venv/bin/pip install -r ${APP_DIR}/requirements.txt

echo "[deploy] Running migrations..."
${APP_DIR}/venv/bin/python ${APP_DIR}/manage.py migrate --settings=config.settings

echo "[deploy] Collecting static files..."
${APP_DIR}/venv/bin/python ${APP_DIR}/manage.py collectstatic --noinput --settings=config.settings

echo "[deploy] Restarting Gunicorn..."
systemctl restart gunicorn

echo "[deploy] Reloading Nginx..."
nginx -t && systemctl reload nginx

echo "[deploy] Done!"
