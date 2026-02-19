# ==========================================================
# APPLICATION : Remplissage Silo Boues
# Auteur : AV (FMI Process)
# Date : 19/02/2025
#
# OBJECTIF :
# Permettre aux exploitants de savoir quand le silo de boues
# sera rempli. 
#
# UTILISATION :
# Outil destiné aux sites d’incinération.
# Développé avec Streamlit pour mise à disposition web
# via GitHub / Streamlit Cloud.
# ==========================================================

import streamlit as st
from datetime import datetime, timedelta

# ------------------------------------------
# FONCTION DE CALCUL DU TEMPS DE REMPLISSAGE
# ------------------------------------------
def calcul_remplissage(debit_entrant_t_h, debit_sortant_t_h):
    volume_m3 = 150
    densite_t_m3 = 0.9

    masse_totale = volume_m3 * densite_t_m3  # 135 tonnes
    debit_net = debit_entrant_t_h - debit_sortant_t_h

    if debit_net <= 0:
        return None, None

    temps_heures = masse_totale / debit_net
    return temps_heures, masse_totale

# ----------------------------------------------------------
# CONFIGURATION DE LA PAGE
# ----------------------------------------------------------

st.set_page_config(
    page_title="Calcul Temps Remplissage",
    page_icon="logo.png",
    layout="centered"
)
# ----------------------------------------------------------
# EN-TÊTE AVEC LOGO EN HAUT À GAUCHE
# ----------------------------------------------------------
col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.image("logo.png", width=120)

with col_title:
    st.markdown(
        "<span style='font-size:34px;'>**Temps de remplissage Silos Boues**</span>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<span style='font-size:14px;'>Application interne – FMI Process</span>",
        unsafe_allow_html=True
    )

st.markdown(
    """
    Outil d'aide au calcul du temps de remplissage des silos à boues.
    """
)

st.divider()

# ----------------------------------------------------------
# DONNEES UTILISATEURS
# ----------------------------------------------------------

debit_entrant = st.number_input(
    "Entrez le débit entrant (t/h) :",
    min_value=0.0,
    value=3.0,
    step=0.1)

debit_sortant = st.number_input(
    "Entrez le débit sortant (t/h) :",
    min_value=0.0,
    value=1.0,
    step=0.1)

# ----------------------------------------------------------
# CALCUL TEMPS RESTANT ET FIN DU REMPLISSAGE
# ----------------------------------------------------------

temps, masse = calcul_remplissage(debit_entrant, debit_sortant)

if temps is None:
    st.error("Le silo ne se remplira pas (débit net <= 0).")
else:
    # Date/heure actuelle
    debut = datetime.now()

    # Calcul de la fin
    fin = debut + timedelta(hours=temps)

    # Conversion en heures/minutes
    heures = int(temps)
    minutes = int((temps - heures) * 60)
    st.divider()

# ----------------------------------------------------------
# AFFICHAGE DES RESULTATS
# ---------------------------------------------------------- 

    st.subheader("Résultats")

    st.metric(
        label="Temps de remplissage estimé",
        value=f"{heures} h {minutes} min"
    )

    st.metric(
        label="Fin de remplissage estimée",
        value=f"{fin.strftime('%d/%m/%Y %H:%M')}"
    )
    







