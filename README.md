# 🎨 ComfyUI Studio — Centro de Control, Iteraciones y Artefactos

**Proyecto:** `ComfyUI_Studio`  
**Ubicación:** `~/X26/ComfyUI_Studio`  
**Instalación Core ComfyUI:** `/home/blackhawk/ComfyUI` (Puerto 8188)  
**Fecha de Inicio:** 2026-10-01  

---

## 🎯 Propósito del Proyecto

Este espacio está dedicado exclusivamente a **controlar, iterar, documentar y versionar todas las interacciones con ComfyUI**.

### 🌟 Capacidades Integradas:
1. **Control de Versiones (Git):** Cada iteración, prueba de prompt, workflow `.json` o mejora de scripts se registra en un commit de Git.
2. **Artefactos y Documentación (`docs/`):** Todos los planes, notas de investigación y reportes técnicos siguen el estándar de nomenclatura `YYYYMMDD_NOMBRE.md`.
3. **Biblioteca de Workflows (`workflows/`):** Almacén central de diagramas y flujos de trabajo reutilizables en formato JSON.
4. **Automatización vía API (`scripts/`):** Scripts en Python y Bash para enviar tareas, consultar estados e interactuar con ComfyUI en el puerto 8188 sin necesidad de intervención manual.
5. **Protocolo Tetrafuerza:** Integración completa con Obsidian, Engrams de conocimiento e historial de commits en GitHub (`jappy1961/comfyui-studio`).

---

## 📁 Estructura del Repositorio

```
~/X26/ComfyUI_Studio/
├── README.md                      # Documento principal del proyecto
├── .gitignore                     # Exclusiones de Git (outputs pesados, temp, venv)
├── docs/                          # Notas, planes, walkthroughs y reportes (YYYYMMDD_*.md)
│   └── 20261001_INICIO_PROYECTO_COMFYUI_STUDIO.md
├── workflows/                     # Flujos de trabajo JSON organizados por versión e iteración
├── scripts/                       # Scripts de automatización y control API
│   ├── start_comfy.sh             # Script para iniciar el servidor nativo en port 8188
│   └── comfy_api_client.py        # Cliente API de Python para enviar prompts y monitorear
└── outputs/                       # Muestras de renders y evidencias visuales por iteración
```

---

## ⚡ Comandos Rápidos

* **Iniciar ComfyUI:**
  ```bash
  ./scripts/start_comfy.sh
  ```
* **Verificar API de ComfyUI:**
  ```bash
  python3 scripts/comfy_api_client.py --check
  ```
* **Guardar e Iterar con Tetrafuerza:**
  ```bash
  bash ~/X26/SysAdmin/Scripts/tetrafuerza.sh "mensaje del commit" "ComfyUI_Studio" "$CONVERSATION_ID"
  ```
