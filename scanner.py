import requests
SUPABASE_URL = "https://dsjtbpcerjxpbxuxiuf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRzanRicGNlcmp4cGJoeHV4aXVmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MjExNDMsImV4cCI6MjA3NDk5NzQ0M30.xxxxx"

def ajouter(titre, entreprise, ville, desc):
    url = f"{SUPABASE_URL}/rest/v1/offres"
    headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}", "Content-Type": "application/json"}
    data = {"titre": titre, "entreprise": entreprise, "ville": ville, "description": desc, "source": "gabon-osint"}
    r = requests.post(url, headers=headers, json=data)
    print(r.status_code)

ajouter("Commercial Terrain Fixe+Com", "Canal+ Gabon", "Libreville", "Fixe + commission, WhatsApp CV")
ajouter("Caissière Glass", "Prix Import", "Libreville", "CDD 6 mois, experience caisse")
ajouter("Chauffeur Livreur", "Logistique Gabon", "Port-Gentil", "Permis B+C requis")
