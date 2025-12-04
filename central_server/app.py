"""
Dattak Central Server - Threat Intelligence Hub
Aggregates and distributes IP blacklists across the community
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import json
from datetime import datetime
import os

app = FastAPI(title="Dattak Central Threat Intelligence")

THREATS_FILE = "threats.json"


class ThreatReport(BaseModel):
    """Model for threat reports from local probes"""
    ip: str
    site_id: str
    reason: str
    timestamp: str = None


class BlacklistResponse(BaseModel):
    """Model for blacklist responses"""
    blacklist: List[Dict[str, str]]
    count: int


def load_threats() -> Dict:
    """Load threats from JSON file"""
    if not os.path.exists(THREATS_FILE):
        return {"blacklist": []}
    
    try:
        with open(THREATS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"blacklist": []}


def save_threats(data: Dict):
    """Save threats to JSON file"""
    with open(THREATS_FILE, 'w') as f:
        json.dump(data, f, indent=2)


@app.get("/")
async def root():
    """Root endpoint"""
    threats = load_threats()
    return {
        "service": "Dattak Central Threat Intelligence",
        "status": "operational",
        "total_threats": len(threats.get("blacklist", []))
    }


@app.post("/api/threats/report")
async def report_threat(report: ThreatReport):
    """
    Receive threat report from a local probe
    Adds the IP to the central blacklist if not already present
    """
    # Add timestamp if not provided
    if not report.timestamp:
        report.timestamp = datetime.now().isoformat()
    
    # Load current threats
    threats = load_threats()
    
    # Check if IP already in blacklist
    existing_ips = [entry.get("ip") for entry in threats.get("blacklist", [])]
    
    if report.ip not in existing_ips:
        # Add new threat
        threat_entry = {
            "ip": report.ip,
            "site_id": report.site_id,
            "reason": report.reason,
            "timestamp": report.timestamp
        }
        threats["blacklist"].append(threat_entry)
        save_threats(threats)
        
        print(f"[DATTAK CENTRAL] New threat reported: {report.ip} by {report.site_id} - {report.reason}")
        
        return {
            "status": "success",
            "message": "Threat reported and added to blacklist",
            "ip": report.ip,
            "total_threats": len(threats["blacklist"])
        }
    else:
        print(f"[DATTAK CENTRAL] Duplicate threat report: {report.ip} by {report.site_id}")
        return {
            "status": "duplicate",
            "message": "IP already in blacklist",
            "ip": report.ip,
            "total_threats": len(threats["blacklist"])
        }


@app.get("/api/threats/blacklist", response_model=BlacklistResponse)
async def get_blacklist():
    """
    Return the current blacklist of malicious IPs
    Used by local probes to sync their protection
    """
    threats = load_threats()
    blacklist = threats.get("blacklist", [])
    
    return {
        "blacklist": blacklist,
        "count": len(blacklist)
    }


@app.delete("/api/threats/clear")
async def clear_blacklist():
    """
    Clear the entire blacklist (for testing/demo purposes)
    """
    save_threats({"blacklist": []})
    print("[DATTAK CENTRAL] Blacklist cleared")
    return {"status": "success", "message": "Blacklist cleared"}


if __name__ == "__main__":
    import uvicorn
    print("Starting Dattak Central Threat Intelligence Server on port 5000...")
    uvicorn.run(app, host="0.0.0.0", port=5000)

