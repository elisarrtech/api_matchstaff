# chatboterr
# Chatbot Matchstaff

Pequeño chatbot en Python (Flask) para recolectar datos de candidatos en tu sitio de reclutamiento.

## 🧾 Estructura
- `backend/`: API en Flask
- `frontend/`: HTML + JS + CSS

## 🚀 Despliegue backend (Render.com)
1. Crea servicio "Web Service" -> conecta tu repo.
2. Build command: `pip install -r backend/requirements.txt`
3. Start command: `gunicorn app:app --chdir backend -b 0.0.0.0:$PORT`
4. Configura puerto `$PORT`.
5. Copia la URL pública y ponla en `frontend/index.html`.

## 🚀 Despliegue frontend (GitHub Pages)
1. Selecciona la rama `main` y carpeta `/frontend` en settings de Pages.
2. Tu sitio estará en `https://<tuusuario>.github.io/<repo>/`.

## 📌 Uso
- Web: incrusta `<iframe>` o botón que abra `index.html`.
- Redes sociales: comparte URL de Pages.

## 📩 Mejoras
- Guardar respuestas en base de datos o Google Sheets.
- Enviarlas por correo.
- Validaciones, estado de progreso.
- Diseño responsive/mobile.
