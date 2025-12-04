# Dattak Community Shield

Protection collaborative contre les cyberattaques pour les PME.

## Installation

```bash
# Installer les dépendances
cd central_server && pip3 install -r requirements.txt
cd ../site_a && pip3 install -r requirements.txt
cd ../site_b && pip3 install -r requirements.txt
cd ../attacker && pip3 install -r requirements.txt
```

## Démarrage

**Terminal 1 - Serveur Central:**
```bash
cd central_server && python3 app.py
```

**Terminal 2 - Site A:**
```bash
cd site_a && python3 app.py
```

**Terminal 3 - Site B:**
```bash
cd site_b && python3 app.py
```

**Terminal 4 - Tests:**
```bash
# Tous les scénarios
cd attacker && python3 bot.py http://localhost:8001

# Scénario spécifique
python3 bot.py http://localhost:8001 honeypot
python3 bot.py http://localhost:8001 sql1
python3 bot.py http://localhost:8001 sql2
python3 bot.py http://localhost:8001 xss1
python3 bot.py http://localhost:8001 xss2
```

## URLs

- Serveur Central: http://localhost:5001
- Site A: http://localhost:8001
- Site B: http://localhost:8002
- Dashboards: http://localhost:8001/dashboard | http://localhost:8002/dashboard

## Concept

Quand Site A est attaqué, Site B est automatiquement protégé grâce au partage d'intelligence des menaces.
