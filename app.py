import streamlit as st
import requests

st.title("📍 Ma Position en Direct")

# Champ pour entrer le mot de passe secret
password = st.text_input("Mot de passe requis pour voir la position :", type="password")

# Définissez votre mot de passe secret ici
SECRET_CODE = "mon_mot_de_passe_secret"

if password == SECRET_CODE:
    st.success("Accès autorisé !")
    
    # Bouton pour actualiser la position
    if st.button("Récupérer ma position IP"):
        try:
            r = requests.get("https://ipinfo.io/json", timeout=5)
            if r.ok:
                d = r.json()
                st.write(f"**Ville :** {d.get('city')}")
                st.write(f"**Région :** {d.get('region')}")
                st.write(f"**Pays :** {d.get('country')}")
                st.write(f"**Coordonnées (IP) :** {d.get('loc')}")
                
                # Affichage sur une carte interactive Streamlit
                lat, lon = map(float, d.get('loc').split(','))
                st.map({"lat": [lat], "lon": [lon]})
        except Exception as e:
            st.error(f"Erreur : {e}")

elif password:
    st.error("Mot de passe incorrect.")
