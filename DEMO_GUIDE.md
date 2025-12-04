# Guide de Démo - Dattak Community Shield

## Préparation (5 minutes avant la présentation)

### 1. Installation
```bash
./install_all.sh
```

### 2. Lancer tous les composants

**Terminal 1 - Serveur Central**
```bash
./start_central.sh
```
Attendre le message: "Uvicorn running on http://0.0.0.0:5000"

**Terminal 2 - Site A**
```bash
./start_site_a.sh
```
Attendre le message: "Uvicorn running on http://0.0.0.0:8001"

**Terminal 3 - Site B**
```bash
./start_site_b.sh
```
Attendre le message: "Uvicorn running on http://0.0.0.0:8002"

**Terminal 4 - Attente** (pour le bot)
Garder ce terminal ouvert pour lancer les attaques pendant la démo

### 3. Préparer les onglets du navigateur

Ouvrir ces 4 URLs dans des onglets :
1. http://localhost:8001 (Site A)
2. http://localhost:8001/dashboard (Dashboard A)
3. http://localhost:8002 (Site B)
4. http://localhost:8002/dashboard (Dashboard B)

---

## Script de Présentation (5 minutes)

### 🎬 Introduction (30 secondes)

**Parler** :
> "Bonjour ! Je vais vous présenter Dattak Community Shield : la première immunité collective cyber pour les PME, intégrée à leur assurance.
>
> Le problème : Les PME sont vulnérables aux attaques automatisées, mais les solutions existantes sont trop complexes.
>
> Notre solution : Un bouclier Zero-Config qui partage l'intelligence des menaces. Quand une entreprise est attaquée, toutes les autres sont automatiquement protégées."

**Montrer** : Les 4 onglets du navigateur ouverts

---

### 🛡️ Phase 1 : Présentation des Sites (30 secondes)

**Montrer Site A** : http://localhost:8001
> "Voici le site d'un cabinet d'avocats. Il a un simple formulaire de contact."

**Pointer** : Le badge vert "Protégé par Dattak Community Shield"

**Montrer Dashboard A** : http://localhost:8001/dashboard
> "Actuellement, aucune attaque. Protection à zéro."

**Montrer Site B** : http://localhost:8002
> "Voici un cabinet d'expertise comptable. Même protection."

**Montrer Dashboard B** : http://localhost:8002/dashboard
> "Également zéro attaque pour le moment."

---

### 🚨 Phase 2 : Attaque sur Site A (1 minute 30)

**Terminal 4** : Lancer l'attaque
```bash
./attack_site_a.sh
```

**Commenter pendant l'exécution** :
> "Je lance maintenant un bot d'attaque automatisé contre le Site A. Regardez..."

**Pointer dans le terminal** :
- Les attaques ENVOYÉES (en bleu 🚀)
- Les attaques BLOQUÉES (en rouge ❌)
- Les raisons du blocage : Honeypot, SQL Injection, XSS

**Lire le résumé** :
> "15 attaques envoyées, 15 bloquées. Taux de blocage : 100%."

**Rafraîchir Dashboard A** : http://localhost:8001/dashboard
> "Le dashboard du Site A montre maintenant les attaques bloquées. On voit les IPs malveillantes dans le journal."

---

### 🌐 Phase 3 : L'Effet Réseau - LE MOMENT CLÉ (2 minutes)

**Rafraîchir Dashboard B** : http://localhost:8002/dashboard

**POINTER avec emphase** :
> "Regardez le Site B ! Il n'a JAMAIS été attaqué directement. Pourtant...
>
> **Montrer** : Protection Communautaire : [X] IPs
>
> Le Site B a reçu automatiquement la liste des IPs malveillantes qui ont attaqué le Site A.
>
> C'est déjà vacciné contre ces menaces !"

**Prouver avec une attaque** : Terminal 4
```bash
./attack_site_b.sh
```

**Commenter** :
> "Je lance maintenant les MÊMES attaques contre le Site B..."

**Pointer** :
- Les attaques sont IMMÉDIATEMENT bloquées (403 Forbidden)
- Le bot ne peut même pas commencer

**Résumé** :
> "Site B a été protégé AVANT d'être attaqué, grâce à l'expérience du Site A.
>
> C'est l'immunité collective appliquée à la cybersécurité !"

---

### ✅ Phase 4 : Conclusion (1 minute)

**Récapituler les avantages** :

1. **Zero-Config** ✅
   > "Pas de configuration DNS, pas de firewall à paramétrer. On installe et ça protège."

2. **Protection Automatique** ✅
   > "Détection honeypot, SQL injection, XSS... Tout est automatique."

3. **Effet Réseau** ✅
   > "Une attaque bloquée chez un client protège TOUS les clients. Plus il y a d'assurés, plus la protection est forte."

4. **Intégré à l'Assurance** ✅
   > "L'utilisation du Shield améliore votre Cyber Score et peut réduire votre prime ou franchise."

**Différenciation** :
> "Contrairement à Cloudflare ou CrowdSec :
> - Pas d'abonnement à payer séparément
> - Pas de configuration technique
> - Protection pertinente : les menaces qui visent VOS clients, pas tout Internet"

**Call to Action** :
> "Dattak Community Shield : La cybersécurité collaborative pour les PME.
>
> Merci !"

---

## 🔧 En cas de problème pendant la démo

### Le bot ne se lance pas
```bash
cd attacker
pip3 install -r requirements.txt
python3 bot.py http://localhost:8001
```

### Les dashboards ne se rafraîchissent pas
- Appuyer sur F5 pour forcer le rafraîchissement
- Vérifier que le serveur central est bien démarré

### Un serveur ne démarre pas
- Vérifier que le port n'est pas déjà utilisé
- Tuer le processus : `lsof -ti:5000 | xargs kill -9` (remplacer 5000 par le bon port)

### Réinitialiser pour une nouvelle démo
1. Arrêter tous les serveurs (Ctrl+C dans chaque terminal)
2. Supprimer `central_server/threats.json`
3. Recréer le fichier : `echo '{"blacklist": []}' > central_server/threats.json`
4. Relancer tous les serveurs

---

## 📊 Statistiques Attendues

Après l'attaque sur Site A :
- **Site A** :
  - Attaques bloquées localement : 15
  - Total menaces : 15
  
- **Site B** (avant d'être attaqué) :
  - Protection communautaire : 15
  - Site B est protégé contre 15 IPs sans avoir été attaqué

---

## 🎯 Points Clés à Mentionner

1. **Pour les PME** : "Vous n'avez pas besoin d'un expert IT"
2. **Pour les assureurs** : "Réduction du risque sinistre, données en temps réel"
3. **Effet réseau** : "Plus on a de clients, plus la protection est forte"
4. **Business model** : "Intégré à l'assurance, pas un coût supplémentaire"

---

## 📝 Questions Fréquentes

**Q : Et si je veux bloquer manuellement une IP ?**
> "L'API centrale permet d'ajouter des IPs manuellement via POST /api/threats/report"

**Q : Qu'en est-il des faux positifs ?**
> "Les honeypots et patterns sont précis. Un utilisateur normal ne déclenchera jamais la protection."

**Q : Scalabilité ?**
> "Pour la production, on utilise une base de données distribuée et du cache. Le POC utilise du JSON pour la simplicité."

**Q : Vie privée / RGPD ?**
> "On ne stocke que les IPs malveillantes détectées, pas les données utilisateur. Conforme RGPD."

---

Bonne démo ! 🚀

