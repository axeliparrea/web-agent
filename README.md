# Run Indeed Bot (Guía ultra corta)

Este repo tiene dos bots (LinkedIn e Indeed). Para correr Indeed con el menor número de pasos:

## 1) Instalar dependencias mínimas

Desde la raíz del repo:

```
pip install -r indeed_bot/requirements.txt
pip install python-dotenv
```

Requisito del sistema: tener Chromium o Google Chrome instalado.

## 2) Configurar una sola vez

Edita el `.env` en la raíz y define tu búsqueda (ejemplo para MX):

```
INDEED_LANGUAGE=mx
INDEED_BASE_URL=https://mx.indeed.com/trabajo?q=desarrollador+de+software&l=Monterrey%2C+N.+L.&radius=100
INDEED_START=0
INDEED_END=50
```

Consejo: saca `INDEED_BASE_URL` copiando la URL de resultados después de aplicar filtros en la UI de Indeed (evita URLs con `vjk=`).

## 3) Ejecutar

Desde la raíz del repo:

```
python main indeed
```

Primer run: si te pide login, inicia sesión en la ventana del navegador, cierra esa ventana y vuelve a correr el comando.

---
Opcional: Para LinkedIn, configura `Auto_job_applier_linkedIn/config/` y ejecuta `python main linkedin`.