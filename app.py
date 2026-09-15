import streamlit as st
import time
import os

# --- Configuration de la page ---
st.set_page_config(page_title="Joyeux Anniversaire 🌹", page_icon="🌹", layout="centered")

SURNOM = "La fine rose de mon esprit"
ASSETS_DIR = "assets"  # Dossier contenant images, audios et vidéo

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
        animation: fadeInPage 0.9s ease-in-out;
    }
    .conte-titre {
        color: #d90429;
        font-style: italic;
        text-align: center;
        margin-bottom: 20px;
        animation: fadeInPage 1.2s ease-in-out;
    }
    @keyframes fadeInPage {
        0% { opacity: 0; transform: translateY(12px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# --- Gestion des étapes avec la Session State ---
if "etape" not in st.session_state:
    st.session_state.etape = 1
if "page_conte" not in st.session_state:
    st.session_state.page_conte = 0
if "branche" not in st.session_state:
    st.session_state.branche = None  # None, "oui" ou "non"

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
    st.title("📖 La légende de la fleur Zehra")

    # --- Dossier où déposer les fichiers d'illustration et de narration ---
    # Pour chaque page N, dépose (si tu veux) :
    #   assets/conte_page{N}.jpg          -> l'illustration de la page
    #   assets/conte_page{N}_audio.mp3    -> la narration audio de la page
    # Ils s'afficheront automatiquement dès qu'ils existent, sans retoucher le code.

    def afficher_page(texte, image_path=None, audio_path=None):
        """Affiche une page du conte avec, si disponibles, une image et une narration audio."""
        if image_path and os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        st.markdown(f"<div class='conte'>{texte}</div>", unsafe_allow_html=True)
        if audio_path and os.path.exists(audio_path):
            st.audio(audio_path)
        else:
            st.caption(f"🎙️ Espace réservé pour la narration audio de cette page (dépose le fichier ici : {audio_path})")

    # --- Pages communes du conte (avant la bifurcation) ---
    textes_du_livre = [
        "Dans une colonie d'abeilles, tous les jours on parlait de la légendaire fleur "
        "Zehra. C'était une fleur tellement splendide, tellement belle, que ses pétales "
        "rayonnaient : à travers eux, on pouvait voir la réfraction de la lumière et "
        "toutes ses couleurs se refléter. Elle possédait un nectar capable de nourrir "
        "une colonie pour toute une éternité, voire plusieurs colonies entières. Une "
        "abeille entendit cette histoire et décida de consacrer sa vie à trouver cette "
        "fleur, pour aider la sienne.",

        "Il se mit à la chercher pendant des jours, des nuits, des mois, des années. "
        "Sous la pluie, sous les tempêtes, sous la neige, à travers toutes les saisons "
        "qui l'attaquaient, il ne lâcha rien et resta déterminé. Un jour, posé sur une "
        "feuille pour se reposer, celle-ci se brisa et il tomba avec elle. Étourdi par "
        "la chute, il se releva la tête qui tournait. Puis, au loin, une image de plus "
        "en plus nette apparut : une énorme fleur qui n'avait pas encore éclos. "
        "L'abeille se précipita, tourna autour d'elle, puis décida d'en assurer la "
        "protection jusqu'à son éclosion, pour qu'aucun autre insecte ne s'en approche, "
        "et pour pouvoir prévenir sa colonie une fois la fleur ouverte.",

        "L'abeille chanta, écrivit des poèmes pour qu'elle s'ouvre, la supplia de le "
        "faire. Mais comme la fleur ne voyait rien, elle se refermait de plus en plus, "
        "par peur, par crainte, par manque de confiance, par méfiance. Elle croyait que "
        "tout n'était que mensonges, qu'il était un menteur venu lui faire du mal "
        "alors que pour l'abeille, même face à une simple fissure sur un pétale, il "
        "aurait brisé ses propres ailes pour la recoudre.",

        "Au loin, un insecte apparut, fonçant droit sur l'abeille et la fleur. Il "
        "tourna autour d'elle pour y entrer de force. L'abeille le vit et se précipita "
        "pour l'arrêter. Elle se battit pour la fleur ; l'insecte, coriace, ne se "
        "laissa pas faire et lui dit :\n\n"
        "*« Ohhh, toi, tu ne vois pas qu'elle ne s'ouvrira jamais à toi ? Il faut être "
        "brutal les fleurs n'aiment pas les insectes comme toi, ceux qui prennent "
        "soin d'elles. Elles veulent des insectes qui les brisent, qui les utilisent, "
        "qui ne les respectent pas ! Comprends ça ! »*",

        "L'abeille répondit :\n\n"
        "*« C'est possible. Mais pour moi, c'est elle qui me donnera à manger, qui me "
        "couvrira de ses pétales, qui prendra soin de ma colonie. Si j'agis comme toi, "
        "je l'aurai, certes, mais je la détruirai. Elle ne sera jamais libre. Une fleur "
        "qui ne te choisit pas te donne ce que tu veux seulement pour ne pas se faire "
        "mal, pour se protéger, faute de force. Ce n'est pas ce que je veux. Je veux "
        "une fleur qui brille, qui rayonne, qui pleure pour moi, avec moi, en ma "
        "présence qu'elle ne se cache plus. Nos visions sont différentes. Je suis "
        "prêt à perdre ma vie pour elle. »*\n\n"
        "Les deux insectes se battirent, et l'abeille piqua l'autre. Son propre "
        "abdomen se déchira ; les deux moururent et tombèrent au sol.",

        "Pendant quelque temps, la fleur n'entendit plus les bruits de l'abeille. Elle "
        "prit alors la décision de s'ouvrir. Ses pétales splendides s'ouvrirent peu à "
        "peu, le soleil brilla, et la légendaire fleur Zehra éclosa enfin. Aucun "
        "insecte ne vint. Elle se sentit indigne et se mit à pleurer. Au loin, un "
        "insecte entendit ses pleurs et vit la splendide fleur Zehra mais cet "
        "insecte ne connaissait ni la valeur, ni l'honneur, ni rien de tout cela, et "
        "il appela tous ses amis. La fleur, pleine de joie, s'apprêta à les accueillir "
        "alors qu'ils n'étaient là que pour la détruire. Ils lui arrachèrent les "
        "pétales, sa tige se brisa, ses couleurs pâlirent. La tête penchée vers le "
        "sol, elle vit l'abeille qui avait tourné pendant des mois autour d'elle, "
        "l'abdomen déchiré, et comprit enfin qu'il avait toujours été là pour la "
        "protéger.",
    ]

    # Construction des pages : chaque page va automatiquement chercher son image
    # et son audio dans le dossier assets/ (voir afficher_page ci-dessus).
    pages_du_livre = [
        {
            "texte": texte,
            "image": os.path.join(ASSETS_DIR, f"conte_page{i}.jpg"),
            "audio": os.path.join(ASSETS_DIR, f"conte_page{i}_audio.mp3"),
        }
        for i, texte in enumerate(textes_du_livre, start=1)
    ]

    # --- Les deux fins possibles ---
    fin_oui = (
        "Une larme sincère, remplie d'émotion, d'amour, de chagrin et de regret, tomba "
        "sur l'abeille. L'abeille se réveilla sans avoir compris ce qui s'était passé. "
        "Il recousit d'abord son abdomen ; quelques jours plus tard, il n'était plus "
        "tout à fait le même, mais il retrouva ses esprits et guérit. Une idée, "
        "pourtant, ne le quittait pas : la fleur Zehra. Car pour lui, cette fleur "
        "était gravée, cousue au plus profond de son ADN, de son esprit, de sa peau. "
        "Malgré ses douleurs, il retourna vers elle et la trouva brisée, cassée. "
        "L'abeille oublia aussitôt ses propres douleurs, attristé par cette situation, "
        "et se mit immédiatement au travail, espérant qu'elle guérisse. Chaque jour, "
        "avec ses petites pattes, il lui apporta des gouttes d'eau, répara sa tige et "
        "l'orienta vers le soleil. En faisant tout cela, une pensée le traversa : s'il "
        "parlait de son existence à sa colonie, les siens feraient exactement ce que "
        "ces insectes avaient fait. Il prit alors la décision de ne parler d'elle à "
        "personne. Peu à peu, la fleur reprit vie ; un air doux, un soleil chaud et "
        "apaisant pénétra ses pétales, et elle retrouva la vie. L'abeille, heureux, "
        "s'approcha de la fleur Zehra. La fleur, heureuse elle aussi, lui demanda "
        "pardon. L'abeille se tourna vers elle et lui dit qu'elle n'avait pas à "
        "s'excuser, car pour prouver son amour, il devait la protéger, quitte à "
        "mourir pour elle. L'abeille se posa sur la tête de la fleur et lui demanda de "
        "se refermer à jamais. La fleur et l'abeille vécurent ainsi, ensemble, pour "
        "l'éternité. 🌹🐝 **FIN**"
    )

    fin_non = (
        "La larme de la fleur tomba sur l'abeille, mais rien ne se produisit. Aucun "
        "souffle ne revint. L'abeille resta là, immobile, sous le regard de la fleur "
        "brisée. Zehra comprit alors que certaines blessures ne se referment jamais "
        "tout à fait, et que le silence qui suivit en disait plus long que tous les "
        "mots qu'elle n'avait jamais su offrir à temps.\n\n"
        "Elle continua de rayonner, mais différemment plus doucement, comme une "
        "lumière qui se souvient. Chaque printemps, une seule abeille venait se poser "
        "un instant sur ses pétales, sans jamais rester : un hommage silencieux à "
        "celui qui n'avait pas eu sa chance. Zehra ne referma plus jamais complètement "
        "ses pétales, comme si une part d'elle attendait encore. 🥀 **FIN**"
    )

    total_pages = len(pages_du_livre)
    idx = st.session_state.page_conte

    # --- Navigation dans les pages communes ---
    if st.session_state.branche is None and idx < total_pages:
        page = pages_du_livre[idx]
        afficher_page(page["texte"], page["image"], page["audio"])
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
                if st.button("Continuer... ➡️"):
                    st.session_state.page_conte += 1
                    st.rerun()

    # --- Le point de bifurcation ---
    elif st.session_state.branche is None and idx == total_pages:
        st.markdown(
            "<div class='conte-titre'>Une larme commence à se former sur les pétales "
            "de Zehra...</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='conte'>Comment veux-tu changer cette histoire ?<br><br>"
            "Veux-tu donner une seconde chance à l'abeille et à la fleur ?</div>",
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)
        with col1:
            oui_histoire = st.button("Oui, donne-leur une chance 🌹")
        with col2:
            non_histoire = st.button("Non")

        if oui_histoire:
            st.session_state.branche = "oui"
            st.rerun()
        elif non_histoire:
            st.session_state.branche = "non"
            st.rerun()

    # --- Affichage de la fin choisie ---
    else:
        if st.session_state.branche == "oui":
            texte_fin = fin_oui
            image_fin = os.path.join(ASSETS_DIR, "conte_fin_heureuse.jpg")
            audio_fin = os.path.join(ASSETS_DIR, "conte_fin_heureuse_audio.mp3")
        else:
            texte_fin = fin_non
            image_fin = os.path.join(ASSETS_DIR, "conte_fin_melancolique.jpg")
            audio_fin = os.path.join(ASSETS_DIR, "conte_fin_melancolique_audio.mp3")
        afficher_page(texte_fin, image_fin, audio_fin)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Revenir au choix"):
                st.session_state.branche = None
                st.rerun()
        with col2:
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

    video_path = os.path.join(ASSETS_DIR, "Seedance_20_Mini_64804.mp4")
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.info("🎥 Espace réservé : la vidéo sera ajoutée ici dès qu'elle sera prête.")
