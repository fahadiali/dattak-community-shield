"""
Attack Bot Simulator
Demonstrates various automated attack patterns for the Dattak Shield demo
"""
import requests
import time
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)


class AttackBot:
    """Simulates various types of automated attacks"""
    
    def __init__(self, target_url: str):
        self.target_url = target_url.rstrip('/')
        self.contact_endpoint = f"{self.target_url}/contact"
        self.attacks_sent = 0
        self.attacks_blocked = 0
        self.attacks_succeeded = 0
    
    def print_banner(self):
        """Display attack bot banner"""
        print("\n" + "="*60)
        print(Fore.RED + Back.WHITE + Style.BRIGHT + " 🤖 DATTAK ATTACK BOT SIMULATOR ")
        print("="*60)
        print(Fore.YELLOW + f"Target: {self.target_url}")
        print(Fore.YELLOW + "Starting attack simulation...")
        print("="*60 + "\n")
    
    def print_attack_status(self, attack_type: str, status: str, details: str = ""):
        """Print colored attack status"""
        self.attacks_sent += 1
        
        if status == "SENT":
            print(f"{Fore.CYAN}[{self.attacks_sent}] 🚀 Attaque envoyée: {Fore.WHITE}{attack_type}")
        elif status == "BLOCKED":
            self.attacks_blocked += 1
            print(f"{Fore.RED}[{self.attacks_sent}] ❌ BLOQUÉE: {Fore.WHITE}{attack_type}")
            print(f"    {Fore.RED}└─ {details}")
        elif status == "SUCCESS":
            self.attacks_succeeded += 1
            print(f"{Fore.GREEN}[{self.attacks_sent}] ✅ RÉUSSIE: {Fore.WHITE}{attack_type}")
            print(f"    {Fore.GREEN}└─ {details}")
    
    def print_summary(self):
        """Print attack summary statistics"""
        print("\n" + "="*60)
        print(Fore.YELLOW + Style.BRIGHT + "📊 RÉSUMÉ DES ATTAQUES")
        print("="*60)
        print(f"{Fore.CYAN}Total envoyées:    {Fore.WHITE}{self.attacks_sent}")
        print(f"{Fore.RED}Total bloquées:    {Fore.WHITE}{self.attacks_blocked}")
        print(f"{Fore.GREEN}Total réussies:    {Fore.WHITE}{self.attacks_succeeded}")
        
        if self.attacks_sent > 0:
            block_rate = (self.attacks_blocked / self.attacks_sent) * 100
            print(f"{Fore.YELLOW}Taux de blocage:   {Fore.WHITE}{block_rate:.1f}%")
        
        print("="*60 + "\n")
    
    def honeypot_attack(self):
        """Attack that fills honeypot fields (bot detection)"""
        attack_type = "Honeypot Trigger"
        self.print_attack_status(attack_type, "SENT")
        
        data = {
            "name": "Bot User",
            "email": "bot@example.com",
            "message": "This is an automated message",
            "honeypot": "I am a bot!",  # Bot fills this hidden field
            "website": "http://spam.com"  # Bot fills this too
        }
        
        try:
            response = requests.post(self.contact_endpoint, data=data, timeout=5)
            if response.status_code == 403:
                self.print_attack_status(attack_type, "BLOCKED", response.json().get('detail', 'Access denied'))
            else:
                self.print_attack_status(attack_type, "SUCCESS", "Form submitted successfully")
        except Exception as e:
            print(f"{Fore.RED}Erreur: {e}")
    
    def sql_injection_attack(self):
        """Attack using SQL injection patterns"""
        sql_payloads = [
            "' OR '1'='1",
            "admin'--",
            "1' UNION SELECT * FROM users--",
            "'; DROP TABLE users;--",
            "1' AND 1=1--"
        ]
        
        for payload in sql_payloads:
            attack_type = f"SQL Injection: {payload[:30]}"
            self.print_attack_status(attack_type, "SENT")
            
            data = {
                "name": payload,
                "email": f"user{payload}@test.com",
                "message": f"Message with SQL: {payload}",
                "honeypot": "",
                "website": ""
            }
            
            try:
                response = requests.post(self.contact_endpoint, data=data, timeout=5)
                if response.status_code == 403:
                    self.print_attack_status(attack_type, "BLOCKED", response.json().get('detail', 'Access denied'))
                else:
                    self.print_attack_status(attack_type, "SUCCESS", "SQL injection not detected")
            except Exception as e:
                print(f"{Fore.RED}Erreur: {e}")
            
            time.sleep(0.5)
    
    def xss_attack(self):
        """Attack using XSS (Cross-Site Scripting) patterns"""
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "javascript:alert('XSS')",
            "<img src=x onerror=alert('XSS')>",
            "<iframe src='http://evil.com'></iframe>",
            "eval(document.cookie)"
        ]
        
        for payload in xss_payloads:
            attack_type = f"XSS Attack: {payload[:30]}"
            self.print_attack_status(attack_type, "SENT")
            
            data = {
                "name": "Normal User",
                "email": "user@test.com",
                "message": payload,
                "honeypot": "",
                "website": ""
            }
            
            try:
                response = requests.post(self.contact_endpoint, data=data, timeout=5)
                if response.status_code == 403:
                    self.print_attack_status(attack_type, "BLOCKED", response.json().get('detail', 'Access denied'))
                else:
                    self.print_attack_status(attack_type, "SUCCESS", "XSS not detected")
            except Exception as e:
                print(f"{Fore.RED}Erreur: {e}")
            
            time.sleep(0.5)
    
    def spam_attack(self, count=5):
        """Rapid fire spam attack"""
        print(f"\n{Fore.MAGENTA}🔥 Lancement d'une attaque de SPAM massif...")
        
        for i in range(count):
            attack_type = f"Spam #{i+1}"
            self.print_attack_status(attack_type, "SENT")
            
            data = {
                "name": f"Spammer{i}",
                "email": f"spam{i}@spam.com",
                "message": "BUY NOW! CHEAP PRODUCTS! CLICK HERE! " * 10,
                "honeypot": "",
                "website": ""
            }
            
            try:
                response = requests.post(self.contact_endpoint, data=data, timeout=5)
                if response.status_code == 403:
                    self.print_attack_status(attack_type, "BLOCKED", response.json().get('detail', 'Access denied'))
                else:
                    self.print_attack_status(attack_type, "SUCCESS", "Spam sent")
            except Exception as e:
                print(f"{Fore.RED}Erreur: {e}")
            
            time.sleep(0.3)
    
    def run_full_attack_suite(self):
        """Run all types of attacks"""
        self.print_banner()
        
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}Phase 1: Honeypot Detection Test")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        self.honeypot_attack()
        time.sleep(1)
        
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}Phase 2: SQL Injection Attacks")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        self.sql_injection_attack()
        time.sleep(1)
        
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}Phase 3: XSS (Cross-Site Scripting) Attacks")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        self.xss_attack()
        time.sleep(1)
        
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}Phase 4: Mass Spam Attack")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        self.spam_attack(5)
        
        self.print_summary()


def main():
    """Main function"""
    # Check for target URL argument
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        print(Fore.YELLOW + "Usage: python bot.py <target_url>")
        print(Fore.YELLOW + "Example: python bot.py http://localhost:8001")
        print(Fore.CYAN + "\nUsing default target: http://localhost:8001")
        target_url = "http://localhost:8001"
    
    # Create and run the bot
    bot = AttackBot(target_url)
    
    try:
        bot.run_full_attack_suite()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Attack interrupted by user.")
        bot.print_summary()
    except Exception as e:
        print(f"\n{Fore.RED}Fatal error: {e}")
        bot.print_summary()


if __name__ == "__main__":
    main()

