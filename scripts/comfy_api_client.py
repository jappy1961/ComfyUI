#!/usr/bin/env python3
"""
Cliente API para ComfyUI (Puerto 8188)
Permite verificar el estado del servidor, enviar workflows en formato JSON y consultar la cola de ejecución.
"""

import sys
import json
import urllib.request
import urllib.parse
import argparse

SERVER_URL = "http://127.0.0.1:8188"

def check_status():
    try:
        req = urllib.request.Request(f"{SERVER_URL}/system_stats")
        with urllib.request.urlopen(req, timeout=3) as res:
            data = json.loads(res.read().decode())
            print("🟢 ComfyUI Server ACTIVO y respondiendo en el puerto 8188.")
            print(json.dumps(data, indent=2))
            return True
    except Exception as e:
        print(f"🔴 ComfyUI Server NO está respondiendo en {SERVER_URL}: {e}")
        return False

def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(f"{SERVER_URL}/prompt", data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            response_data = json.loads(res.read().decode())
            print("🚀 Prompt enviado exitosamente a la cola de ComfyUI:")
            print(json.dumps(response_data, indent=2))
            return response_data
    except Exception as e:
        print(f"❌ Error al enviar prompt a ComfyUI: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ComfyUI API Client Helper")
    parser.add_argument("--check", action="store_true", help="Verifica la conexión con el servidor")
    parser.add_argument("--workflow", type=str, help="Ruta al archivo JSON del workflow a ejecutar")

    args = parser.parse_args()

    if args.check or len(sys.argv) == 1:
        check_status()
    elif args.workflow:
        with open(args.workflow, 'r', encoding='utf-8') as f:
            wf = json.load(f)
        queue_prompt(wf)
