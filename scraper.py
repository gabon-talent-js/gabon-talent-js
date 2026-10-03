import os
from supabase import create_client

url = "https://dsjtbpcerjxpbxuxiuf.supabase.co"
key = os.environ.get("SUPABASE_KEY") or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRzanRicGNlcmp4cGJieHV4aXVmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTEwMzAzODYsImV4cCI6MjEwNjYwNjM4Nn0.stSO21CCayobN_KaFucZqVrQjXwVVFyvSv0q5n5Yz6s"

supabase = create_client(url, key)

# Le robot va scanner ici plus tard avec BeautifulSoup / Apify
offres = [
  {"title":"Développeur Full-Stack JS","company":"Gabon Talent OS","city":"Libreville","salary":"800k-1.2M","source":"LinkedIn","source_url":"https://www.linkedin.com/jobs/","email_rh":"recrutement@gabontalent.ga","description":"Construction de l'OS. React/Supabase. Opportunité CTO.","tag":"NOUVEAU"},
  {"title":"Comptable Pétrole & Gaz","company":"Assala Energy","city":"Port-Gentil","salary":"650k","source":"Facebook","source_url":"https://www.facebook.com/groups/emploi.gabon","email_rh":"rh@assalaenergy.ga","description":"Scan auto depuis groupe Facebook Emploi Gabon. Sage 100 exigé.","tag":"CDI"},
  {"title":"Community Manager","company":"Agence 241","city":"Libreville","salary":"300k","source":"Instagram","source_url":"https://www.instagram.com/","email_rh":"contact@agence241.ga","description":"Scan auto depuis Instagram. Gestion TikTok/Insta.","tag":"URGENT"}
]

supabase.table("jobs").delete().neq("id", 0).execute()
supabase.table("jobs").insert(offres).execute()
print("SUCCESS - 3 offres injectées")
