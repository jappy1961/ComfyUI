# <span style="color:#00ff88; font-weight:bold;">🎨 PROYECTO MAESTRO: COMFYUI STUDIO (CONTROL, ARTEFACTOS Y GIT)</span>

**Fecha de generación:** 2026-10-01  
**Autor:** Antigravity Workstation (Nodo Dell Xeon / X26)  
**Proyecto:** `ComfyUI_Studio` (`~/X26/ComfyUI_Studio`)  

---

## 📌 1. Visión y Propósito del Proyecto

El proyecto **ComfyUI Studio** se crea como el centro neurálgico de desarrollo, iteración y control de **ComfyUI** dentro del ecosistema Trinidad X26.

A diferencia de la carpeta `/home/blackhawk/ComfyUI` (que opera como el motor de ejecución nativo del sistema), esta carpeta `~/X26/ComfyUI_Studio` es un **repositorio independiente de Git y workspace dedicado** para:

1. **Gestión de Iteraciones con Git:** Cada flujo de trabajo (`.json`), script de automatización, prompt o modificación técnica se guarda con commits de Git explícitos y trazables.
2. **Registro de Artefactos y Notas (`docs/`):** Almacenamiento ordenado de todos los documentos, walkthroughs, especificaciones y bitácoras de experimentos bajo el estándar `YYYYMMDD_NOMBRE.md`.
3. **Repositorio de Workflows (`workflows/`):** Control de versiones para diagramas y esquemas de generación (Flux, SDXL, Sana, AnimateDiff, IP-Adapter, etc.).
4. **Orquestación y API (`scripts/`):** Scripts automatizados para interactuar con la API REST y WebSockets de ComfyUI (puerto `8188`), ejecutar renders en lote y monitorear el uso de VRAM de la GPU NVIDIA RTX A6000.
5. **Consolidación Tetrafuerza:** Integración con Obsidian Vault (`~/Documents/Obsidian Vault/Antigravity/Bitacoras/`) y sincronización multi-nodo con GitHub (`jappy1961/comfyui-studio`).

---

## 🛠️ 2. Arquitectura del Repositorio

```
~/X26/ComfyUI_Studio/
├── README.md                                    # Guía general de arquitectura
├── .gitignore                                   # Control de bulto y archivos temporales
├── docs/                                        # Documentos y reportes (YYYYMMDD_*.md)
│   └── 20261001_INICIO_PROYECTO_COMFYUI_STUDIO.md # Este documento de inicio
├── workflows/                                   # Diagramas JSON exportados e iteraciones
├── scripts/                                     # Automatización de control API y servidor
│   ├── start_comfy.sh                           # Lanzador del motor ComfyUI (:8188)
│   └── comfy_api_client.py                      # Cliente Python API para envíos remotos
└── outputs/                                     # Muestras y evidencias visuales registradas
```

---

## ⚡ 3. Protocolo de Trabajo e Iteraciones

Para cada sesión o iteración de trabajo con ComfyUI:

1. **Definición de Iteración:** Se genera una nota o plan en `docs/YYYYMMDD_DESCRIPCION.md`.
2. **Ejecución y Modificación:** Se prueban los workflows o scripts.
3. **Registro de Artefactos:** Los workflows JSON se guardan en `workflows/` y los logs relevantes en `docs/`.
4. **Commit & Push (Tetrafuerza):** Se ejecuta el comando global de Tetrafuerza para asentar los cambios:
   ```bash
   bash ~/X26/SysAdmin/Scripts/tetrafuerza.sh "feat(comfy): mensaje de la iteración" "ComfyUI_Studio" "$CONVERSATION_ID"
   ```

---
*Copia de resguardo registrada en el proyecto ComfyUI_Studio y lista para el primer commit de Git.*
