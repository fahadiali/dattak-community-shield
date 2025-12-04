# Installation Client

## 1. Installer
```bash
pip3 install fastapi uvicorn pydantic python-multipart jinja2 requests
```

## 2. Configurer
Dans `site_a/app.py`:
```python
SITE_ID = "Nom_Client"
CENTRAL_SERVER = "http://serveur-dattak:5001"
```

## 3. Démarrer
```bash
cd site_a && python3 app.py
```

## Intégration Site Existant
```python
from shield.protection import create_shield, ShieldMiddleware

shield = create_shield("Nom_Client", "http://serveur-dattak:5001")
app.add_middleware(ShieldMiddleware, shield=shield)
```

