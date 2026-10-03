import os, requests
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
def ajouter(titre, entreprise, ville, desc):
    url = f"{SUPABASE_URL}/rest/v1/offres"
    headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}", "Content-Type": "application/json"}
    data = {"titre": titre, "entreprise": entreprise, "ville": ville, "description": desc, "source": "gabon-osint"}
    r = requests.post(url, headers=headers, json=data)
    print(f"{titre} -> {r.status_code}")
ajouter("Commercial Terrain Fixe+Com", "Canal+ Gabon", "Libreville", "Fixe + commission")
ajouter("Caissière Glass", "Prix Import", "Libreville", "CDD 6 mois caisse")
ajouter("Chauffeur Livreur", "Logistique Gabon", "Port-Gentil", "Permis B+C")
print("ROBOT TERMINE !")
