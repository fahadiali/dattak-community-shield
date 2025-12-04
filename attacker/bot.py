"""
Bot d'attaque minimaliste - Scénarios de test
"""
import requests
import sys
from colorama import Fore, init

init(autoreset=True)

ATTACKS = {
    "honeypot": {
        "name": "Honeypot",
        "data": {"name": "Test", "email": "test@test.com", "message": "Hello", "honeypot": "bot", "website": "spam.com"}
    },
    "sql1": {
        "name": "SQL Injection 1",
        "data": {"name": "' OR '1'='1", "email": "test@test.com", "message": "Test", "honeypot": "", "website": ""}
    },
    "sql2": {
        "name": "SQL Injection 2",
        "data": {"name": "admin'--", "email": "test@test.com", "message": "Test", "honeypot": "", "website": ""}
    },
    "xss1": {
        "name": "XSS 1",
        "data": {"name": "Test", "email": "test@test.com", "message": "<script>alert('XSS')</script>", "honeypot": "", "website": ""}
    },
    "xss2": {
        "name": "XSS 2",
        "data": {"name": "Test", "email": "test@test.com", "message": "javascript:alert('XSS')", "honeypot": "", "website": ""}
    }
}


def attack(target_url, scenario=None):
    """Lancer une attaque"""
    url = f"{target_url.rstrip('/')}/contact"
    
    if scenario and scenario in ATTACKS:
        # Scénario spécifique
        attack_data = ATTACKS[scenario]
        print(f"{Fore.CYAN}[{attack_data['name']}] {Fore.WHITE}Envoi...")
        try:
            r = requests.post(url, data=attack_data['data'], timeout=5)
            if r.status_code == 403:
                print(f"{Fore.RED}❌ BLOQUÉ ({r.status_code})")
            else:
                print(f"{Fore.GREEN}✅ RÉUSSI ({r.status_code})")
        except Exception as e:
            print(f"{Fore.RED}Erreur: {e}")
    else:
        # Tous les scénarios
        print(f"{Fore.YELLOW}=== Test de tous les scénarios ===\n")
        for key, attack_data in ATTACKS.items():
            print(f"{Fore.CYAN}[{attack_data['name']}] {Fore.WHITE}Envoi...", end=" ")
            try:
                r = requests.post(url, data=attack_data['data'], timeout=5)
                if r.status_code == 403:
                    print(f"{Fore.RED}❌ BLOQUÉ")
                else:
                    print(f"{Fore.GREEN}✅ RÉUSSI")
            except Exception as e:
                print(f"{Fore.RED}Erreur")
        print(f"\n{Fore.YELLOW}=== Fin des tests ===")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Usage: python3 bot.py <url> [scenario]")
        print(f"{Fore.CYAN}Scénarios: honeypot, sql1, sql2, xss1, xss2")
        print(f"{Fore.CYAN}Exemple: python3 bot.py http://localhost:8001")
        print(f"{Fore.CYAN}Exemple: python3 bot.py http://localhost:8001 honeypot")
        sys.exit(1)
    
    target = sys.argv[1]
    scenario = sys.argv[2] if len(sys.argv) > 2 else None
    attack(target, scenario)
