# ⚡ Quick Start - Dattak Community Shield

## 🚀 Démarrage Rapide (10 minutes)

### Étape 1: Installation (2 minutes)

```bash
cd /Users/admin/Documents/Epitech/DATTAK
./install_all.sh
```

Attendez que toutes les dépendances soient installées.

---

### Étape 2: Lancer les Serveurs (2 minutes)

**Ouvrir 4 terminaux séparés**

#### Terminal 1 - Serveur Central
```bash
cd /Users/admin/Documents/Epitech/DATTAK
./start_central.sh
```
✅ Attendez: "Uvicorn running on http://0.0.0.0:5000"

#### Terminal 2 - Site A
```bash
cd /Users/admin/Documents/Epitech/DATTAK
./start_site_a.sh
```
✅ Attendez: "Uvicorn running on http://0.0.0.0:8001"

#### Terminal 3 - Site B
```bash
cd /Users/admin/Documents/Epitech/DATTAK
./start_site_b.sh
```
✅ Attendez: "Uvicorn running on http://0.0.0.0:8002"

#### Terminal 4 - Gardez ouvert pour les attaques

---

### Étape 3: Ouvrir les Pages Web (1 minute)

Dans votre navigateur, ouvrir ces 4 onglets:

1. 🏢 **Site A**: http://localhost:8001
2. 📊 **Dashboard A**: http://localhost:8001/dashboard
3. 🏢 **Site B**: http://localhost:8002
4. 📊 **Dashboard B**: http://localhost:8002/dashboard

---

### Étape 4: Lancer la Démo (5 minutes)

#### 🎬 Démo Rapide

**1. Attaquer Site A** (Terminal 4):
```bash
cd /Users/admin/Documents/Epitech/DATTAK
./attack_site_a.sh
```

👁️ **Observer**:
- Terminal: Attaques BLOQUÉES en rouge ❌
- Dashboard A: Nombre d'attaques bloquées augmente

**2. Vérifier Site B** (Dashboard B):
- Rafraîchir: http://localhost:8002/dashboard
- 🎯 **VOIR**: "Protection Communautaire" a augmenté!
- Site B est protégé SANS avoir été attaqué!

**3. Prouver la protection** (Terminal 4):
```bash
./attack_site_b.sh
```

👁️ **Observer**:
- Les attaques sont IMMÉDIATEMENT bloquées
- Site B était déjà vacciné!

---

## 🎯 Le "Wow Effect"

> **"Site B a été protégé par l'attaque subie par Site A"**
> 
> C'est l'immunité collective cyber!

---

## 📖 Pour Plus de Détails

- **Présentation complète**: Lire `DEMO_GUIDE.md`
- **Documentation technique**: Lire `README.md`
- **Tests et validation**: Lire `TESTING_CHECKLIST.md`
- **Vue d'ensemble**: Lire `PROJECT_SUMMARY.md`

---

## 🔧 Commandes Utiles

### Arrêter tous les serveurs
Dans chaque terminal: `Ctrl + C`

### Réinitialiser pour une nouvelle démo
```bash
cd central_server
echo '{"blacklist": []}' > threats.json
```
Puis relancer tous les serveurs.

### Vérifier qu'un port est libre
```bash
lsof -ti:5000  # Remplacer 5000 par le port à vérifier
```

### Tuer un processus sur un port
```bash
lsof -ti:5000 | xargs kill -9
```

---

## ✅ Checklist Avant Démo

- [ ] Python 3.8+ installé
- [ ] Dépendances installées (`./install_all.sh`)
- [ ] 4 terminaux ouverts
- [ ] Serveurs démarrés (central, site_a, site_b)
- [ ] 4 onglets navigateur ouverts
- [ ] Terminal 4 prêt pour attaques
- [ ] `DEMO_GUIDE.md` lu et compris

---

## 🎤 Pitch Court (30 secondes)

> "Dattak Community Shield protège les PME contre les cyberattaques avec une innovation: l'immunité collective.
> 
> Quand une entreprise est attaquée, toutes les autres du réseau sont automatiquement protégées.
> 
> Zero configuration. Intégré à l'assurance. Protection collaborative.
> 
> Regardez la démo..."

---

## 🚨 Dépannage Express

**Erreur de port déjà utilisé:**
```bash
# Tuer le processus sur le port (ex: 5000)
lsof -ti:5000 | xargs kill -9
```

**Module non trouvé:**
```bash
# Réinstaller les dépendances
./install_all.sh
```

**Dashboard ne se met pas à jour:**
- Appuyer sur F5 (rafraîchir)
- Vérifier que le serveur central est lancé

---

## ⏱️ Timeline

- **Installation**: 2 minutes
- **Démarrage**: 2 minutes
- **Préparation navigateur**: 1 minute
- **Démo**: 5 minutes
- **TOTAL**: 10 minutes

---

**Prêt pour la démo à 16h30! 🚀**

