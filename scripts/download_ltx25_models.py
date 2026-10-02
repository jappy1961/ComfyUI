#!/usr/bin/env python3
import os
import sys
import time
from huggingface_hub import hf_hub_download

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

BASE_MODELS_DIR = "/home/blackhawk/ComfyUI/models"

HF_TOKEN = None
token_file = "/home/blackhawk/.cache/huggingface/token"
if os.path.exists(token_file):
    with open(token_file) as f:
        HF_TOKEN = f.read().strip()

MODELS = [
    {
        "primary_repo": "Lightricks/LTX-2.5",
        "fallback_repo": "johndoe48/ltx-2.5",
        "file": "diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors",
        "target_dir": "diffusion_models",
        "name": "ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors"
    },
    {
        "primary_repo": "Lightricks/LTX-2.5",
        "fallback_repo": "johndoe48/ltx-2.5",
        "file": "text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors",
        "target_dir": "text_encoders",
        "name": "gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors"
    },
    {
        "primary_repo": "Lightricks/LTX-2.5",
        "fallback_repo": "johndoe48/ltx-2.5",
        "file": "vae/ltx-2.5-video-vae-bf16.safetensors",
        "target_dir": "vae",
        "name": "ltx-2.5-video-vae-bf16.safetensors"
    },
    {
        "primary_repo": "Lightricks/LTX-2.5",
        "fallback_repo": "johndoe48/ltx-2.5",
        "file": "vae/ltx-2.5-audio-vae-bf16.safetensors",
        "target_dir": "vae",
        "name": "ltx-2.5-audio-vae-bf16.safetensors"
    },
    {
        "primary_repo": "Lightricks/LTX-2.5",
        "fallback_repo": "johndoe48/ltx-2.5",
        "file": "latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors",
        "target_dir": "latent_upscale_models",
        "name": "ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors"
    },
    {
        "primary_repo": "Lightricks/LTX-2.3",
        "fallback_repo": None,
        "file": "ltx-2.3-spatial-upscaler-x1.5-1.0.safetensors",
        "target_dir": "latent_upscale_models",
        "name": "ltx-2.3-spatial-upscaler-x1.5-1.0.safetensors"
    },
    {
        "primary_repo": "Lightricks/LTX-2-19b-LoRA-Camera-Control-Static",
        "fallback_repo": None,
        "file": "ltx-2-19b-lora-camera-control-static.safetensors",
        "target_dir": "loras",
        "name": "ltx-2-19b-lora-camera-control-static.safetensors"
    },
    {
        "primary_repo": "Lightricks/LTX-Video-ICLoRA-detailer-13b-0.9.8",
        "fallback_repo": None,
        "file": "ltxv-098-ic-lora-detailer-comfyui.safetensors",
        "target_dir": "loras",
        "name": "ltxv-098-ic-lora-detailer-comfyui.safetensors"
    },
    {
        "primary_repo": "Kijai/MelBandRoFormer_comfy",
        "fallback_repo": None,
        "file": "MelBandRoformer_fp16.safetensors",
        "target_dir": "diffusion_models",
        "name": "MelBandRoformer_fp16.safetensors"
    }
]

def main():
    print("🚀 [LTX-2.5 Downloader] Starting download manager (silent mode)...")
    total = len(MODELS)
    completed = 0
    
    for idx, item in enumerate(MODELS, start=1):
        target_folder = os.path.join(BASE_MODELS_DIR, item["target_dir"])
        os.makedirs(target_folder, exist_ok=True)
        final_path = os.path.join(target_folder, item["name"])
        
        if os.path.exists(final_path) and os.path.getsize(final_path) > 1024 * 1024:
            print(f"✅ [{idx}/{total}] Exists: {item['name']} ({os.path.getsize(final_path) / (1024**2):.1f} MB)")
            completed += 1
            continue
            
        print(f"⬇️ [{idx}/{total}] Downloading {item['name']}...")
        start_time = time.time()
        downloaded = None
        
        # Try primary repo with HF token
        try:
            downloaded = hf_hub_download(
                repo_id=item["primary_repo"],
                filename=item["file"],
                local_dir=target_folder,
                token=HF_TOKEN
            )
        except Exception as e_primary:
            print(f"⚠️ Primary repo {item['primary_repo']} failed: {e_primary}")
            if item.get("fallback_repo"):
                print(f"🔄 Trying fallback repo {item['fallback_repo']}...")
                try:
                    downloaded = hf_hub_download(
                        repo_id=item["fallback_repo"],
                        filename=item["file"],
                        local_dir=target_folder
                    )
                except Exception as e_fallback:
                    print(f"❌ Fallback repo failed: {e_fallback}")
                    
        if downloaded and os.path.exists(downloaded):
            if downloaded != final_path and os.path.isfile(downloaded):
                os.rename(downloaded, final_path)
            elapsed = time.time() - start_time
            size_mb = os.path.getsize(final_path) / (1024**2)
            print(f"🎉 [{idx}/{total}] Completed: {item['name']} ({size_mb:.1f} MB in {elapsed:.1f}s)")
            completed += 1

    print(f"📊 Completed {completed}/{total} models.")

if __name__ == "__main__":
    main()
