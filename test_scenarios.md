# Scénarios de Test

## Tous les scénarios
```bash
cd attacker && python3 bot.py http://localhost:8001
```

## Scénarios individuels

### 1. Honeypot
```bash
python3 bot.py http://localhost:8001 honeypot
```

### 2. SQL Injection 1
```bash
python3 bot.py http://localhost:8001 sql1
```

### 3. SQL Injection 2
```bash
python3 bot.py http://localhost:8001 sql2
```

### 4. XSS 1
```bash
python3 bot.py http://localhost:8001 xss1
```

### 5. XSS 2
```bash
python3 bot.py http://localhost:8001 xss2
```

## Test Site B (protection communautaire)
```bash
python3 bot.py http://localhost:8002
```

