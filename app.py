import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Calculateur d'Intérêt",
    page_icon="💰",
    layout="centered"
)

# Texte en haut à gauche
st.markdown(
    "<h5 style='text-align: left; color: gray;'>Programme créé par Caden</h5>",
    unsafe_allow_html=True
)

# Titre principal
st.title("💰 Calculateur d'Intérêt")

# Création des onglets
tab1, tab2 = st.tabs(["Intérêt Simple", "Intérêt Composé"])

# =========================
# ONGLET INTÉRÊT SIMPLE
# =========================
with tab1:

    st.header("Calculateur d'Intérêt Simple")

    st.write("Entrez les valeurs ci-dessous :")

    capital_simple = st.number_input(
        "Capital Initial ($)",
        min_value=0.0,
        value=1000.0,
        step=1.0,
        key="simple_capital"
    )

    taux_simple = st.number_input(
        "Taux d'intérêt (%)",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="simple_taux"
    )

    temps_simple = st.number_input(
        "Temps (années)",
        min_value=0.0,
        value=3.0,
        step=1.0,
        key="simple_temps"
    )

    if st.button("Calculer l'intérêt simple"):

        interet_simple = capital_simple * (taux_simple / 100) * temps_simple
        total_simple = capital_simple + interet_simple

        st.success("Calcul terminé !")

        st.subheader("Résultats")

        st.write(f"Intérêt gagné : ${interet_simple:.2f}")
        st.write(f"Montant total : ${total_simple:.2f}")

        st.latex(r"I = P \times r \times t")

# =========================
# ONGLET INTÉRÊT COMPOSÉ
# =========================
with tab2:

    st.header("Calculateur d'Intérêt Composé")

    st.write("Entrez les valeurs ci-dessous :")

    capital_compose = st.number_input(
        "Capital Initial ($)",
        min_value=0.0,
        value=1000.0,
        step=1.0,
        key="compose_capital"
    )

    taux_compose = st.number_input(
        "Taux d'intérêt annuel (%)",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="compose_taux"
    )

    temps_compose = st.number_input(
        "Temps (années)",
        min_value=0.0,
        value=3.0,
        step=1.0,
        key="compose_temps"
    )

    frequence = st.number_input(
        "Nombre de compositions par année",
        min_value=1,
        value=1,
        step=1,
        key="compose_frequence"
    )

    if st.button("Calculer l'intérêt composé"):

        montant_compose = capital_compose * (
            1 + (taux_compose / 100) / frequence
        ) ** (frequence * temps_compose)

        interet_compose = montant_compose - capital_compose

        st.success("Calcul terminé !")

        st.subheader("Résultats")

        st.write(f"Intérêt gagné : ${interet_compose:.2f}")
        st.write(f"Montant total : ${montant_compose:.2f}")

        st.latex(r"A = P(1+\frac{r}{n})^{nt}")