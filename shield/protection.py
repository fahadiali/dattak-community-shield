"""
Dattak Shield Protection Module
Provides honeypot detection, threat analysis, and community protection
"""
import re
import time
import threading
import requests
from typing import Dict, List, Set, Optional
from datetime import datetime
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


# Detection patterns for SQL Injection
SQL_PATTERNS = [
    r"(\bUNION\b.*\bSELECT\b)",
    r"(\bOR\b\s+\d+\s*=\s*\d+)",
    r"(\bOR\b\s+['\"].*['\"])",
    r"(--|#|/\*|\*/)",
    r"(\bDROP\b.*\bTABLE\b)",
    r"(\bINSERT\b.*\bINTO\b)",
    r"(\bDELETE\b.*\bFROM\b)",
    r"(\bUPDATE\b.*\bSET\b)",
    r"(;.*\bSELECT\b)",
    r"(\bEXEC\b.*\()",
    r"(\bEXECUTE\b.*\()",
    r"(xp_cmdshell)",
]

# Detection patterns for XSS
XSS_PATTERNS = [
    r"<script[^>]*>.*?</script>",
    r"<script[^>]*>",
    r"javascript:",
    r"onerror\s*=",
    r"onload\s*=",
    r"onclick\s*=",
    r"<iframe[^>]*>",
    r"eval\s*\(",
    r"alert\s*\(",
    r"document\.cookie",
]


class DattakShield:
    """
    Main shield class that provides protection against automated attacks
    """
    
    def __init__(self, site_id: str, central_server_url: str = "http://localhost:5000"):
        self.site_id = site_id
        self.central_server_url = central_server_url
        self.local_blacklist: Set[str] = set()
        self.community_blacklist: Set[str] = set()
        self.blocked_attacks: List[Dict] = []
        self.community_protections = 0
        
        # Compile regex patterns for better performance
        self.sql_regex = [re.compile(pattern, re.IGNORECASE) for pattern in SQL_PATTERNS]
        self.xss_regex = [re.compile(pattern, re.IGNORECASE) for pattern in XSS_PATTERNS]
        
        # Start background sync thread
        self.sync_thread = threading.Thread(target=self._sync_loop, daemon=True)
        self.sync_thread.start()
        
        print(f"[SHIELD {self.site_id}] Protection activated. Central server: {self.central_server_url}")
    
    def _sync_loop(self):
        """Background thread that periodically syncs with central server"""
        while True:
            try:
                self._sync_with_central()
                time.sleep(30)  # Sync every 30 seconds
            except Exception as e:
                print(f"[SHIELD {self.site_id}] Sync error: {e}")
                time.sleep(30)
    
    def _sync_with_central(self):
        """Pull latest blacklist from central server"""
        try:
            response = requests.get(
                f"{self.central_server_url}/api/threats/blacklist",
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                old_count = len(self.community_blacklist)
                self.community_blacklist = {entry["ip"] for entry in data.get("blacklist", [])}
                new_count = len(self.community_blacklist)
                
                if new_count > old_count:
                    diff = new_count - old_count
                    self.community_protections += diff
                    print(f"[SHIELD {self.site_id}] Synced: {new_count} IPs in community blacklist (+{diff} new)")
        except Exception as e:
            print(f"[SHIELD {self.site_id}] Could not sync with central server: {e}")
    
    def _report_threat(self, ip: str, reason: str):
        """Report a detected threat to the central server"""
        try:
            response = requests.post(
                f"{self.central_server_url}/api/threats/report",
                json={
                    "ip": ip,
                    "site_id": self.site_id,
                    "reason": reason,
                    "timestamp": datetime.now().isoformat()
                },
                timeout=5
            )
            if response.status_code == 200:
                print(f"[SHIELD {self.site_id}] Threat reported to Dattak: {ip} - {reason}")
                return True
        except Exception as e:
            print(f"[SHIELD {self.site_id}] Could not report threat: {e}")
        return False
    
    def check_honeypot(self, form_data: Dict) -> bool:
        """
        Check if honeypot field was filled
        Returns True if honeypot was triggered (bot detected)
        """
        # Common honeypot field names
        honeypot_fields = ["honeypot", "bot_field", "email_confirm", "website", "url"]
        
        for field in honeypot_fields:
            if field in form_data and form_data[field]:
                return True
        return False
    
    def check_sql_injection(self, text: str) -> Optional[str]:
        """
        Check if text contains SQL injection patterns
        Returns the matched pattern if found, None otherwise
        """
        for pattern in self.sql_regex:
            match = pattern.search(text)
            if match:
                return match.group(0)
        return None
    
    def check_xss(self, text: str) -> Optional[str]:
        """
        Check if text contains XSS patterns
        Returns the matched pattern if found, None otherwise
        """
        for pattern in self.xss_regex:
            match = pattern.search(text)
            if match:
                return match.group(0)
        return None
    
    def analyze_request(self, form_data: Dict) -> tuple[bool, Optional[str]]:
        """
        Analyze form data for threats
        Returns (is_threat, reason)
        """
        # Check honeypot first
        if self.check_honeypot(form_data):
            return True, "Honeypot triggered - Bot detected"
        
        # Check all form fields for SQL injection and XSS
        for field_name, field_value in form_data.items():
            if not isinstance(field_value, str):
                continue
            
            # Check SQL injection
            sql_match = self.check_sql_injection(field_value)
            if sql_match:
                return True, f"SQL Injection detected: {sql_match[:50]}"
            
            # Check XSS
            xss_match = self.check_xss(field_value)
            if xss_match:
                return True, f"XSS attempt detected: {xss_match[:50]}"
        
        return False, None
    
    def is_blocked(self, ip: str) -> tuple[bool, Optional[str]]:
        """
        Check if an IP is blocked
        Returns (is_blocked, source) where source is 'local' or 'community'
        """
        if ip in self.local_blacklist:
            return True, "local"
        if ip in self.community_blacklist:
            return True, "community"
        return False, None
    
    def block_ip(self, ip: str, reason: str):
        """
        Block an IP and report it to central server
        """
        if ip not in self.local_blacklist:
            self.local_blacklist.add(ip)
            self.blocked_attacks.append({
                "ip": ip,
                "reason": reason,
                "timestamp": datetime.now().isoformat(),
                "site_id": self.site_id
            })
            print(f"[SHIELD {self.site_id}] Blocked IP: {ip} - {reason}")
            
            # Report to central server
            self._report_threat(ip, reason)
    
    def get_stats(self) -> Dict:
        """Get protection statistics"""
        return {
            "site_id": self.site_id,
            "local_blocks": len(self.local_blacklist),
            "community_protections": len(self.community_blacklist),
            "total_attacks_blocked": len(self.blocked_attacks),
            "recent_attacks": self.blocked_attacks[-10:] if self.blocked_attacks else []
        }


class ShieldMiddleware(BaseHTTPMiddleware):
    """
    FastAPI middleware that applies Dattak Shield protection
    """
    
    def __init__(self, app, shield: DattakShield):
        super().__init__(app)
        self.shield = shield
    
    async def dispatch(self, request: Request, call_next):
        # Get client IP
        client_ip = request.client.host
        
        # Check if IP is blocked
        is_blocked, source = self.shield.is_blocked(client_ip)
        if is_blocked:
            print(f"[SHIELD {self.shield.site_id}] Blocked request from {client_ip} (source: {source})")
            return HTTPException(
                status_code=403,
                detail=f"Access denied. IP blocked by Dattak Community Shield ({source} protection)."
            )
        
        # Process the request
        response = await call_next(request)
        return response


def create_shield(site_id: str, central_server_url: str = "http://localhost:5000") -> DattakShield:
    """
    Factory function to create a shield instance
    """
    return DattakShield(site_id, central_server_url)

