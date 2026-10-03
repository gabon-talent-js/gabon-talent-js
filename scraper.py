import os
from supabase import create_client

# NE TOUCHE PAS CETTE PARTIE - Connexion auto
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# C'EST ICI QUE LE ROBOT METTRA LES OFFRES DE FACEBOOK/LINKEDIN PLUS TARD
# Pour l'instant, on met 3 offres de test
offres_a_scanner = [
  {
    "title": "Assistant RH (Scan Facebook)",
    "company": "Airtel Gabon",
    "city": "Libreville",
    "salary": "400k FCFA",
    "source": "Facebook",
    "source_url": "https://www.facebook.com/groups/emploi.gabon",
    "email_rh": "rh@airtel.ga",
    "description": "Offre détectée dans le groupe Facebook 'Emploi Gabon'. Le robot l'a mise ici automatiquement.",
    "tag": "NOUVEAU"
  },
  {
    "title": "Commercial Terrain (Scan LinkedIn)",
    "company": "CanalBox",
    "city": "Libreville",
    "salary": "350k + commissions",
    "source": "LinkedIn",
    "source_url": "https://www.linkedin.com/jobs/",
    "email_rh": "recrutement@canalbox.ga",
    "description": "Offre détectée sur LinkedIn Gabon. CDI. Bac+2 exigé.",
    "tag": "CDI"
  }
]

# Le robot efface les anciennes et met les nouvelles
supabase.table("jobs").delete().neq("id", 0).execute()
supabase.table("jobs").insert(offres_a_scanner).execute()
print("ROBOT OK - Offres poussées")
