#!/bin/bash
# Script para iniciar ComfyUI en segundo plano o modo interactivo
# Ubicación de ComfyUI: /home/blackhawk/ComfyUI

COMFY_DIR="/home/blackhawk/ComfyUI"
LOG_FILE="$COMFY_DIR/comfyui.log"

export PYTHONUNBUFFERED=1

echo "[$(date)] Iniciando ComfyUI Server en http://127.0.0.1:8188 ..."

if [ "$1" == "--background" ] || [ "$1" == "-b" ]; then
    nohup "$COMFY_DIR/venv/bin/python3" "$COMFY_DIR/main.py" --port 8188 > "$LOG_FILE" 2>&1 &
    PID=$!
    echo "[$(date)] ComfyUI corriendo en segundo plano con PID: $PID"
    echo "Log: $LOG_FILE"
else
    exec "$COMFY_DIR/venv/bin/python3" "$COMFY_DIR/main.py" --port 8188
fi
