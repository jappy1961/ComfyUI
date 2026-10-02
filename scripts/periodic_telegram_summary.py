#!/usr/bin/env python3
import os
import sys
import subprocess
import json
import urllib.request

BOT_TOKEN = "8756944347:AAH3WWzHOJopBlpEBxJtcfdfmn9305Dipgs"
CHAT_ID = "8343724201"
BASE_MODELS_DIR = "/home/blackhawk/ComfyUI/models"

MODELS = [
    ("diffusion_models", "ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors"),
    ("text_encoders", "gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors"),
    ("vae", "ltx-2.5-video-vae-bf16.safetensors"),
    ("vae", "ltx-2.5-audio-vae-bf16.safetensors"),
    ("latent_upscale_models", "ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors"),
    ("latent_upscale_models", "ltx-2.3-spatial-upscaler-x1.5-1.0.safetensors"),
    ("loras", "ltx-2-19b-lora-camera-control-static.safetensors"),
    ("loras", "ltxv-098-ic-lora-detailer-comfyui.safetensors"),
    ("diffusion_models", "MelBandRoformer_fp16.safetensors")
]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error sending Telegram summary: {e}", file=sys.stderr)
        return None

def get_summary():
    ready_count = 0
    details = []
    
    for folder, name in MODELS:
        path = os.path.join(BASE_MODELS_DIR, folder, name)
        if os.path.exists(path) and os.path.getsize(path) > 1024 * 1024:
            size_mb = os.path.getsize(path) / (1024**2)
            ready_count += 1
            details.append(f"🟢 `{name}` ({size_mb:.1f} MB)")
        else:
            details.append(f"⏳ `{name}` (Pendiente / Descargando)")
            
    # System info
    df = subprocess.getoutput("df -h / | tail -n 1").split()
    disk_used = df[2] if len(df) > 2 else "N/A"
    disk_avail = df[3] if len(df) > 3 else "N/A"
    disk_pct = df[4] if len(df) > 4 else "N/A"
    
    msg = (
        f"📊 *[REPORTE DE AVANCE 30 MIN - DELL WORKSTATION]*\n\n"
        f"🤖 *Estado de Descarga LTX 2.5:* {ready_count}/{len(MODELS)} modelos listos\n"
        f"💾 *Disco SSD:* {disk_used} usados / {disk_avail} libres ({disk_pct})\n\n"
        f"*Detalle por Modelo:*\n" + "\n".join(details) + "\n\n"
        f"✨ _Próximo resumen consolidado en 30 minutos._"
    )
    return msg

if __name__ == "__main__":
    summary_text = get_summary()
    print(summary_text)
    send_telegram(summary_text)
