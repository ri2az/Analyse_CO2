import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Activer le style BD
plt.xkcd()

# ---------------------
# Données nettoyées
# ---------------------
data = {
    "distance_km": [19.1, 11.5, 50.0, 49.0, 108.8, 8.0, 102.5, 3.4, 97.3, 109.9,
                    81.4, 4.4, 65.9, 50.8, 19.9, 107.9, 85.5, 48.5, 130.9, 102.7, 34.6],
    "co2_kg":     [3.65, 2.3, 9.6, 9.41, 20.9, 1.54, 19.8, 0.58, 18.6, 21.1,
                   15.6, 0.77, 12.7, 9.79, 3.84, 20.7, 16.5, 9.41, 25.2, 19.8, 6.72]
}

df = pd.DataFrame(data)
df["co2_per_km"] = df["co2_kg"] / df["distance_km"]

# ---------------------
# Titre principal
# ---------------------
st.title("🌍 Analyse des données sur mon voyage à l'île Maurice en 2023")

# ---------------------
# Section 1 : Données brutes
# ---------------------
st.subheader("📋 Données enregistrées")
st.dataframe(df)

# ---------------------
# Section 2 : Statistiques
# ---------------------
st.subheader("📌 Résumé statistique")

# Slider pour choisir le prix du carbone
price_per_kg = st.slider("💶 Choisissez le prix du CO₂ (€/kg)", min_value=0.01, max_value=0.50, value=0.10, step=0.01)

# Calculs
total_distance = df["distance_km"].sum()
total_co2 = df["co2_kg"].sum()
mean_co2_per_km = total_co2 / total_distance
co2_cost_euro = total_co2 * price_per_kg
max_co2 = df["co2_kg"].max()
max_distance = df["distance_km"].max()

# Affichage
st.markdown(f"""
- 🛣️ **Distance totale parcourue** : `{total_distance:.1f}` km  
- 🌫️ **Émissions totales de CO₂** : `{total_co2:.2f}` kgCO₂e  
- ⚖️ **Moyenne CO₂ par km** : `{mean_co2_per_km:.2f}` kgCO₂e/km  
- 💶 **Coût carbone estimé** : `{co2_cost_euro:.2f}` € (à {price_per_kg:.2f} €/kg)  
- 📈 **Trajet le plus long** : `{max_distance}` km  
- 🔥 **Trajet le plus polluant** : `{max_co2}` kgCO₂e
""")

# ---------------------
# Section 3 : Graphiques
# ---------------------
st.subheader("📈 Visualisations des données")

# 1. Courbe distance vs CO2
fig1, ax1 = plt.subplots()
ax1.plot(df["distance_km"], df["co2_kg"], marker='o', linestyle='-', linewidth=2)
ax1.set_xlabel("Distance (km)")
ax1.set_ylabel("CO₂ (kg)")
ax1.set_title("Évolution des émissions selon la distance")
st.pyplot(fig1)

# 2. Histogramme des émissions
fig2, ax2 = plt.subplots()
ax2.hist(df["co2_kg"], bins=10)
ax2.set_xlabel("CO₂ (kg)")
ax2.set_ylabel("Nombre de trajets")
ax2.set_title("Distribution des émissions de CO₂")
st.pyplot(fig2)

# 3. CO₂ par km
fig3, ax3 = plt.subplots()
ax3.plot(df["co2_per_km"], marker='o')
ax3.set_ylabel("kgCO₂e/km")
ax3.set_xlabel("Trajet #")
ax3.set_title("Émissions de CO₂ par kilomètre")
st.pyplot(fig3)

# 4. Barres comparatives
fig4, ax4 = plt.subplots()
ax4.bar(range(len(df)), df["distance_km"], label="Distance (km)")
ax4.bar(range(len(df)), df["co2_kg"], label="CO₂ (kg)", alpha=0.7)
ax4.set_title("Comparaison Distance vs CO₂")
ax4.legend()
st.pyplot(fig4)

# ---------------------
# Footer
# ---------------------
st.markdown("---")
st.caption("Données analysées avec amour et un soupçon de CO₂ 🌴 – powered by Streamlit & xkcd style.")