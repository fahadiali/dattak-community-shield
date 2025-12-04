"""
Site A - Protected PME Website
Demonstrates Dattak Community Shield protection
"""
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sys
import os

# Add parent directory to path to import shield
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from shield.protection import create_shield, ShieldMiddleware

app = FastAPI(title="Site A - PME Demo")
templates = Jinja2Templates(directory="templates")

# Initialize Dattak Shield
SITE_ID = "Site_A"
CENTRAL_SERVER = "http://localhost:5001"
shield = create_shield(SITE_ID, CENTRAL_SERVER)

# Add shield middleware
app.add_middleware(ShieldMiddleware, shield=shield)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with contact form"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "site_name": "Site A - Cabinet d'Avocats Dupont"
    })


@app.post("/contact")
async def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
    honeypot: str = Form(""),  # Honeypot field
    website: str = Form("")    # Another honeypot field
):
    """Handle contact form submission with protection"""
    client_ip = request.client.host
    
    # Prepare form data for analysis
    form_data = {
        "name": name,
        "email": email,
        "message": message,
        "honeypot": honeypot,
        "website": website
    }
    
    # Analyze the request
    is_threat, reason = shield.analyze_request(form_data)
    
    if is_threat:
        # Block this IP
        shield.block_ip(client_ip, reason)
        print(f"[SITE A] Attack blocked from {client_ip}: {reason}")
        raise HTTPException(
            status_code=403,
            detail=f"Access denied. Threat detected: {reason}"
        )
    
    # If we get here, the form is legitimate
    print(f"[SITE A] Legitimate form submission from {client_ip}")
    return JSONResponse({
        "status": "success",
        "message": "Merci! Votre message a été envoyé avec succès."
    })


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Protection dashboard showing statistics"""
    stats = shield.get_stats()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "site_name": "Site A - Cabinet d'Avocats Dupont",
        "stats": stats
    })


@app.get("/api/stats")
async def get_stats():
    """API endpoint to get current statistics"""
    return shield.get_stats()


if __name__ == "__main__":
    import uvicorn
    print(f"Starting {SITE_ID} on port 8001...")
    print(f"Home: http://localhost:8001")
    print(f"Dashboard: http://localhost:8001/dashboard")
    uvicorn.run(app, host="0.0.0.0", port=8001)

