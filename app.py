import streamlit as st
import time

# --- Configuration de la page ---
st.set_page_config(page_title="Joyeux Anniversaire 🌹", page_icon="🌹", layout="centered")

SURNOM = "La fine rose de mon esprit"

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
    .conte {
        background-color: #ffe5ec;
        border-radius: 15px;
        padding: 25px;
        font-size: 1.1em;
        line-height: 1.6em;
        color: #4a0d1f;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Gestion des étapes avec la Session State ---
if "etape" not in st.session_state:
    st.session_state.etape = 1
if "page_conte" not in st.session_state:
    st.session_state.page_conte = 0

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
    q2 = st.selectbox("2. Quel combattant UFC est adoré ici ?",
                       ("Conor McGregor", "Islam Makhachev", "Jon Jones", "Khabib Nurmagomedov"))

    if st.button("Valider les réponses"):
        if q1.lower() == "blanc" and "makhachev" in q2.lower():
            st.session_state.etape = 3
            st.session_state.page_conte = 0
            st.rerun()
        else:
            st.error("Mmmh... Ce ne sont pas les bonnes réponses ! Réfléchis bien mon cœur. 🧐")

# ==========================================
# ÉTAPE 3 : Le livre - la fleur et l'abeille
# ==========================================
elif st.session_state.etape == 3:
    st.title("📖 Un conte pour toi...")

    pages_du_livre = [
        "Il était une fois, dans un jardin oublié du temps, une fleur si splendide "
        "que même le soleil ralentissait sa course pour la contempler un peu plus longtemps. "
        "Elle poussait seule, fière et lumineuse, sans savoir à quel point elle illuminait "
        "tout ce qui l'entourait.",

        "Un jour, une petite abeille, épuisée d'avoir cherché sans relâche à travers "
        "mille jardins, se posa enfin sur ses pétales. Elle n'avait jamais rien vu d'aussi "
        "beau, d'aussi vrai, d'aussi apaisant que cette fleur-là.",

        "L'abeille revint le lendemain. Puis le jour suivant. Puis tous les jours qui "
        "suivirent. Elle ne butinait plus par nécessité, mais par envie — parce qu'être "
        "près de cette fleur rendait chaque journée plus douce, plus légère, plus lumineuse.",

        "La fleur, elle, avait fini par comprendre que cette petite abeille n'était pas "
        "une visiteuse parmi d'autres. C'était celle qui revenait toujours, celle qui prenait "
        "soin d'elle sans jamais rien abîmer, celle qui la faisait se sentir unique parmi "
        "tous les jardins du monde.",

        "Et depuis ce jour, la fleur et l'abeille ont continué leur histoire, jardin après "
        "jardin, saison après saison — parce que certaines rencontres ne sont pas un hasard, "
        "mais une promesse silencieuse que la vie tenait depuis le début. 🌹🐝",
    ]

    idx = st.session_state.page_conte
    total_pages = len(pages_du_livre)

    st.markdown(f"<div class='conte'>{pages_du_livre[idx]}</div>", unsafe_allow_html=True)
    st.caption(f"Page {idx + 1} / {total_pages}")

    col1, col2 = st.columns(2)
    with col1:
        if idx > 0:
            if st.button("⬅️ Page précédente"):
                st.session_state.page_conte -= 1
                st.rerun()
    with col2:
        if idx < total_pages - 1:
            if st.button("Page suivante ➡️"):
                st.session_state.page_conte += 1
                st.rerun()
        else:
            if st.button("Fermer le livre 🌹"):
                st.session_state.etape = 4
                st.rerun()

# ==========================================
# ÉTAPE 4 : Le clin d'œil romantique
# ==========================================
elif st.session_state.etape == 4:
    st.title("💍 Une petite question...")
    st.write(
        "Alors comme ça, l'abeille et la fleur ne se quittent plus... "
        "Dans ce cas j'ai une question importante à te poser :"
    )
    st.markdown("### Veux-tu continuer cette histoire avec moi, encore et encore ? 🌹")

    col1, col2 = st.columns(2)
    with col1:
        oui = st.button("Oui, évidemment ! 💖")
    with col2:
        non = st.button("Non")

    if oui:
        st.session_state.etape = 5
        st.rerun()
    elif non:
        st.warning("Tu es sûr(e) ? Essaie encore... je ne renonce pas si facilement 😏")

# ==========================================
# ÉTAPE 5 : La vidéo finale
# ==========================================
elif st.session_state.etape == 5:
    st.balloons()
    st.title(f"🌹 Joyeux Anniversaire, {SURNOM} ! 🌹")

    st.markdown(f"""
    ### Mon cœur,

    Si tu lis ce message, c'est que tu as passé toutes les étapes avec succès.
    Cette petite application a été codée rien que pour toi, pour te prouver à quel point
    tu es unique et importante à mes yeux.

    Je te souhaite le plus merveilleux des anniversaires, rempli de bonheur, de sourires
    et de tout l'amour que tu mérites.

    *Je t'aime fort.* ❤️
    """)

    st.subheader("🎬 Un dernier mot en vidéo")

    # --- Emplacement réservé pour la vidéo finale ---
    # Remplace ceci par l'une des deux options ci-dessous quand ta vidéo sera prête :
    #
    # 1) Fichier vidéo local :
    #    st.video("chemin/vers/ta_video.mp4")
    #
    # 2) Lien YouTube / Drive :
    #    st.video("https://www.youtube.com/watch?v=XXXXXXXXXXX")

    st.info("🎥 Espace réservé : la vidéo sera ajoutée ici dès qu'elle sera prête.")
