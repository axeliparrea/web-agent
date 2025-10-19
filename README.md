# Web Agent: LinkedIn + Indeed Bots (Windows)

Guía completa para instalar, configurar y ejecutar ambos bots desde Windows PowerShell.

## Requisitos

- Windows 10/11
- Python 3.10 o 3.11 instalado
- Google Chrome o Chromium instalado

## Instalación rápida

1) Abre PowerShell en la carpeta del repo:

```
cd C:\Users\axeli\web-agent
```

2) Crea y activa un entorno virtual (recomendado):

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Instala dependencias por proyecto:

- Indeed:
```
pip install -r indeed_bot/requirements.txt
```

- LinkedIn:
```
pip install -r Auto_job_applier_linkedIn/requirements.txt
```

Notas:
- Si el sistema está detrás de proxy/inspección SSL, podría ser necesario configurar certificados para `pip`.
- Evita usar Python de MSYS2 en este repo; usa el del `.venv` anterior.

## Configuración

### Indeed (`indeed_bot/config.yaml`)

Campos clave:
- `search.base_url`: pega aquí la URL de resultados de Indeed después de aplicar filtros en el sitio. Evita URLs con `vjk=`.
- `search.start` y `search.end`: paginación (cada página avanza de 10 en 10).
- `camoufox.user_data_dir`: carpeta local para el perfil del navegador.
- `camoufox.language`: código de idioma/país para el dominio (fr, us, mx, es, etc.).

También puedes sobrescribir por variables de entorno en un archivo `.env` en la raíz:

```
INDEED_LANGUAGE=mx
INDEED_BASE_URL=https://mx.indeed.com/trabajo?q=desarrollador+de+software&l=Monterrey%2C+N.+L.&radius=100
INDEED_START=0
INDEED_END=50
INDEED_USER_DATA_DIR=user_data_dir
```

### LinkedIn (`Auto_job_applier_linkedIn/config/*`)

Revisa los archivos en `config/` para: búsqueda, preguntas, credenciales y ajustes. Ajusta según tu flujo.

## Ejecución

Desde la raíz del repo (con el `.venv` activado):

- Indeed:
```
python main indeed
```

- LinkedIn:
```
python main linkedin
```

Primer uso: si el bot abre el navegador pidiendo login, inicia sesión manualmente y cierra esa ventana; vuelve a ejecutar el comando.

## Solución de problemas

### Error: No module named 'yaml'
Instala PyYAML (ya está listado en `indeed_bot/requirements.txt`). Si persiste, ejecuta:
```
pip install PyYAML
```

### Error: No module named 'camoufox' o instalación falla compilando numpy/cmake
En algunos entornos Windows, `pip` intenta compilar dependencias (numpy/lxml) y falla con errores de certificados o toolchains.

Prueba estas alternativas, en este orden:
1. Asegúrate de que el `.venv` está activado y `pip` actualizado:
```
python -m pip install --upgrade pip setuptools wheel
```
2. Instala ruedas precompiladas antes de camoufox:
```
pip install "numpy==1.26.4" "lxml==5.3.0"
pip install camoufox
```
3. Si hay error SSL (CERTIFICATE_VERIFY_FAILED), revisa tu proxy/certificados del sistema. Como último recurso temporal:
```
pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install camoufox
```

### Playwright/Browser no abre o bloqueos en Cloudflare
- Asegúrate de tener Chrome/Chromium instalado.
- Si aparece un challenge, haz clic manualmente la primera vez y vuelve a ejecutar.

## Estructura
- `main` y `main.py`: punto de entrada unificado.
- `indeed_bot/`: bot de Indeed (+ `config.yaml`).
- `Auto_job_applier_linkedIn/`: bot de LinkedIn (+ configs).

## Notas
- Este repo automatiza interacción con sitios de terceros. Úsalo bajo tu responsabilidad y respetando términos de uso.