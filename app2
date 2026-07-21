import streamlit as st
from collections import Counter

class SmartCounter(Counter):
    def __mul__(self, scalar):
        return SmartCounter({k: v * scalar for k, v in self.items()})
    
    # Needs to be indented at the class level so m * m_val and m_val * m both work
    __rmul__ = __mul__

# Ingredients database (per 1 unit / 100g)
m = milk = SmartCounter({"kcal": 34, "prot": 3.3})
y = yogurt = SmartCounter({"kcal": 51, "prot": 9.0})
ch = cheese = SmartCounter({"kcal": 330, "prot": 22.5})
f = flakes = SmartCounter({"kcal": 380, "prot": 8.0})
b = beans = SmartCounter({"kcal": 310, "prot": 24.0})
e = egg = SmartCounter({"kcal": 80, "prot": 12.0})
g = grud = SmartCounter({"kcal": 140, "prot": 25.0})
p = porosh = SmartCounter({"kcal": 379, "prot": 86.4})
ca = cabb = SmartCounter({"kcal": 15, "prot": 0.6})

st.set_page_config(page_title="Macro Calculator", page_icon="🧮", layout="centered")
st.title("Macro Calculator")
st.markdown("---")

# User Inputs
m_val = st.number_input("Milk quantity", value=0.0, step=0.1, key="m")
y_val = st.number_input("Yogurt quantity", value=0.0, step=0.1, key="y")
ch_val = st.number_input("Cheese quantity", value=0.0, step=0.1, key="ch")
f_val = st.number_input("Flakes quantity", value=0.0, step=0.1, key="f")
b_val = st.number_input("Beans quantity", value=0.0, step=0.1, key="b")
g_val = st.number_input("Grud quantity", value=0.0, step=0.1, key="g")
p_val = st.number_input("Poroshok quantity", value=0.0, step=0.1, key="p")
c_val = st.number_input("Cabbages quantity", value=0.0, step=0.1, key="c")

# Calculate individual totals
item_totals = {
    "Milk": m * m_val,
    "Yogurt": y * y_val,
    "Cheese": ch * ch_val,
    "Flakes": f * f_val,
    "Beans": b * b_val,
    "Grud": g * g_val,
    "Poroshok": p * p_val,
    "Cabbage": ca * c_val,
}

# Fix: Start sum with an empty SmartCounter() instead of integer 0
total = sum(item_totals.values(), SmartCounter())

# Display Results
st.markdown("---")
st.header("Total Nutrition")
col1, col2 = st.columns(2)
col1.metric("Calories", f"{total['kcal']:.1f} kcal")
col2.metric("Protein", f"{total['prot']:.1f} g")

with st.expander("Show breakdown"):
    for item_name, values in item_totals.items():
        if values["kcal"] > 0 or values["prot"] > 0:
            st.write(f"- **{item_name}:** {values['kcal']:.1f} kcal | {values['prot']:.1f}g protein")
