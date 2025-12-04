# Dattak Community Shield - POC

**La première immunité collective cyber connectée à votre assurance**

## 🎯 Le Concept

Dattak Community Shield est un système de protection collaborative pour les PME. Lorsqu'une entreprise est attaquée, toutes les autres entreprises du réseau sont automatiquement protégées contre cette même menace. C'est l'immunité collective appliquée à la cybersécurité.

### Le Problème
- Les PME sont vulnérables aux attaques automatisées (bots, SQL injection, XSS)
- Les solutions existantes (WAF) sont trop complexes pour les PME sans expert IT
- Résultat : elles restent exposées jusqu'au sinistre

### La Solution
- **Zero-Config** : Installation simple, pas de configuration DNS ou firewall
- **Protection Collaborative** : Une attaque bloquée chez un client protège tous les autres
- **Intégré à l'Assurance** : Améliore le "Cyber Score" et réduit les primes

## 🏗️ Architecture

Le système comprend 4 composants :

1. **Serveur Central Dattak** (port 5000) - Hub d'intelligence des menaces
2. **Site A** (port 8001) - Cabinet d'Avocats Dupont (demo)
3. **Site B** (port 8002) - Expertise Comptable Martin (demo)
4. **Bot d'Attaque** - Simulateur d'attaques automatisées

### Technologies Utilisées
- **Backend** : FastAPI (Python 3.8+)
- **Protection** : Module Shield avec Honeypot, détection SQL/XSS
- **Interface** : HTML/CSS/JS (templates Jinja2)
- **Threat Intel** : Synchronisation automatique toutes les 30s

## 🚀 Installation Rapide

### Prérequis
```bash
Python 3.8+
pip
```

### Installation

1. **Installer les dépendances pour tous les composants** :

```bash
# Serveur Central
cd central_server
pip install -r requirements.txt
cd ..

# Site A
cd site_a
pip install -r requirements.txt
cd ..

# Site B
cd site_b
pip install -r requirements.txt
cd ..

# Bot d'Attaque
cd attacker
pip install -r requirements.txt
cd ..
```

## 🎬 Démarrage pour la Démo

**IMPORTANT** : Ouvrez 4 terminaux différents pour lancer chaque composant.

### Terminal 1 - Serveur Central Dattak
```bash
cd central_server
python app.py
```
Serveur disponible sur : http://localhost:5000

### Terminal 2 - Site A (Cabinet d'Avocats)
```bash
cd site_a
python app.py
```
- Site : http://localhost:8001
- Dashboard : http://localhost:8001/dashboard

### Terminal 3 - Site B (Expertise Comptable)
```bash
cd site_b
python app.py
```
- Site : http://localhost:8002
- Dashboard : http://localhost:8002/dashboard

### Terminal 4 - Bot d'Attaque
```bash
cd attacker
python bot.py http://localhost:8001
```

## 🎭 Scénario de Démo (5 minutes)

### Phase 1 : Montrer les Sites (30 secondes)

1. Ouvrir dans le navigateur :
   - Site A : http://localhost:8001
   - Site B : http://localhost:8002
   - Dashboard A : http://localhost:8001/dashboard
   - Dashboard B : http://localhost:8002/dashboard

2. Montrer que les deux sites sont protégés (badge "Protégé par Dattak Community Shield")

### Phase 2 : Attaque sur Site A (1 minute)

1. Lancer le bot contre Site A :
```bash
cd attacker
python bot.py http://localhost:8001
```

2. **Observer dans le terminal du bot** :
   - Les attaques envoyées (🚀)
   - Les attaques BLOQUÉES (❌) avec les raisons
   - Résumé : ~15 attaques bloquées

3. **Observer le Dashboard de Site A** :
   - Rafraîchir http://localhost:8001/dashboard
   - Voir le nombre d'attaques bloquées localement
   - Voir les IPs bannies dans le journal

### Phase 3 : L'Effet Réseau - Le "Wow Effect" (2 minutes)

**C'est le moment clé de la démo !**

1. **Ouvrir le Dashboard de Site B** : http://localhost:8002/dashboard

2. **Pointer du doigt** :
   - "Protection Communautaire" : Ce nombre a augmenté !
   - Site B n'a **jamais été attaqué** directement
   - Pourtant, il est déjà protégé contre les IPs qui ont attaqué Site A

3. **Prouver que la protection fonctionne** :
```bash
cd attacker
python bot.py http://localhost:8002
```

4. **Résultat** :
   - Les mêmes IPs d'attaque sont **immédiatement bloquées** sur Site B
   - Même sans avoir été attaquée directement, Site B était déjà vaccinée !

5. **Rafraîchir le Dashboard de Site B** :
   - Voir que le compteur "Protection Communautaire" montre les IPs reçues du réseau

### Phase 4 : Conclusion (1 minute)

**Message clé** :
> "Site B a été protégé par l'attaque subie par Site A. C'est l'immunité collective cyber."

**Avantages démontrés** :
1. ✅ **Zero-Config** : Aucune configuration complexe
2. ✅ **Protection Automatique** : Détection honeypot, SQL, XSS
3. ✅ **Effet Réseau** : Une attaque bloquée protège toute la communauté
4. ✅ **Visibilité** : Dashboard simple pour les PME

## 🛡️ Fonctionnalités du Shield

### Détection des Menaces

1. **Honeypot** : Champs cachés dans les formulaires
   - Si un bot les remplit → Blocage immédiat

2. **SQL Injection** : Détection de patterns malveillants
   - `' OR '1'='1`, `UNION SELECT`, `DROP TABLE`, etc.

3. **XSS (Cross-Site Scripting)** : Détection de scripts malveillants
   - `<script>`, `javascript:`, `onerror=`, etc.

4. **Threat Intelligence** : Synchronisation automatique
   - Les sites se synchronisent avec le serveur central toutes les 30 secondes
   - Partage instantané des IPs malveillantes

## 📊 Endpoints API

### Serveur Central (port 5000)

- `GET /` - Status du serveur
- `POST /api/threats/report` - Recevoir un signalement de menace
- `GET /api/threats/blacklist` - Récupérer la liste noire
- `DELETE /api/threats/clear` - Effacer la liste noire (demo)

### Sites A et B (ports 8001, 8002)

- `GET /` - Page d'accueil avec formulaire
- `POST /contact` - Soumission du formulaire (protégé)
- `GET /dashboard` - Tableau de bord de protection
- `GET /api/stats` - Statistiques de protection (JSON)

## 🧪 Tests Manuels

### Test 1 : Honeypot
```bash
curl -X POST http://localhost:8001/contact \
  -F "name=Test" \
  -F "email=test@test.com" \
  -F "message=Hello" \
  -F "honeypot=I am a bot"
```
**Résultat attendu** : 403 Forbidden - Honeypot triggered

### Test 2 : SQL Injection
```bash
curl -X POST http://localhost:8001/contact \
  -F "name=' OR '1'='1" \
  -F "email=test@test.com" \
  -F "message=Test" \
  -F "honeypot=" \
  -F "website="
```
**Résultat attendu** : 403 Forbidden - SQL Injection detected

### Test 3 : Requête Légitime
```bash
curl -X POST http://localhost:8001/contact \
  -F "name=Jean Dupont" \
  -F "email=jean@example.com" \
  -F "message=Bonjour, je souhaite un rendez-vous" \
  -F "honeypot=" \
  -F "website="
```
**Résultat attendu** : 200 OK - Message envoyé

## 🎨 Personnalisation

### Changer le serveur central
Dans `site_a/app.py` et `site_b/app.py` :
```python
CENTRAL_SERVER = "http://votre-serveur-dattak.com:5000"
```

### Ajouter des patterns de détection
Dans `shield/protection.py` :
```python
SQL_PATTERNS = [
    r"votre_pattern_regex",
    # ...
]
```

## 🔧 Dépannage

### Erreur "Could not sync with central server"
- Vérifier que le serveur central est démarré sur le port 5000
- Vérifier que `CENTRAL_SERVER` pointe vers la bonne URL

### Les attaques ne sont pas bloquées
- Vérifier que le middleware Shield est activé dans l'app
- Vérifier les logs du terminal pour voir les détections

### Dashboard ne montre pas les stats
- Rafraîchir la page (F5)
- Le dashboard se rafraîchit automatiquement toutes les 10 secondes

## 📝 Structure du Projet

```
DATTAK/
├── central_server/          # Serveur central d'intelligence
│   ├── app.py
│   ├── threats.json
│   └── requirements.txt
├── shield/                  # Module de protection réutilisable
│   ├── __init__.py
│   └── protection.py
├── site_a/                  # Site A - Cabinet d'Avocats
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   └── requirements.txt
├── site_b/                  # Site B - Expertise Comptable
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   └── requirements.txt
├── attacker/                # Bot d'attaque pour la demo
│   ├── bot.py
│   └── requirements.txt
└── README.md               # Ce fichier
```

## 🎯 Positionnement vs Concurrents

| Critère | Cloudflare / CrowdSec | Dattak Shield |
|---------|----------------------|---------------|
| **Complexité** | Configuration DNS, règles firewall | Zero-Config, Install & Forget |
| **Modèle économique** | Abonnement SaaS | Intégré à l'assurance |
| **Cible** | Menaces mondiales (bruit) | Menaces du portefeuille client (pertinent) |
| **Incitation** | Payer pour se protéger | Réduction de prime/franchise |
| **Expertise requise** | IT/DevOps | Aucune |

## 🚀 Prochaines Étapes (Production)

1. **Base de données** : Remplacer le JSON par PostgreSQL/MongoDB
2. **Authentification** : API keys pour les sites clients
3. **Machine Learning** : Détection avancée des patterns d'attaque
4. **Géolocalisation** : Bloquer les pays à risque
5. **Alertes** : Notifications email/SMS en temps réel
6. **Analytics** : Rapports mensuels pour les assurés

## 📧 Support

Pour toute question sur ce POC :
- Email : support@dattak.fr
- Documentation : https://docs.dattak.fr

---

**Dattak Community Shield** - L'immunité collective pour la cybersécurité des PME 🛡️

