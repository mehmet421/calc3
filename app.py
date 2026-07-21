import streamlit as st
from collections import Counter
class SmartCounter(Counter):
    def __mul__(self, scalar):
        return SmartCounter({k: v * scalar for k, v in self.items()})
        __rmul__ = __mul__
milk = Counter({"kcal": 34, "prot": 3.3})
yogurt = Counter({"kcal": 51, "prot": 9})
cheese = Counter({"kcal": 330, "prot": 22.5})
flakes = Counter({"kcal": 380, "prot": 8})
beans = Counter({"kcal": 310, "prot": 24})
egg = Counter({"kcal": 80, "prot": 12})
grud = Counter({"kcal": 140, "prot": 25})
porosh = Counter({"kcal": 379, "prot": 86.4})
cabb = Counter({"kcal": 15, "prot": 0.6})
m = milk = SmartCounter({"kcal": 34, "prot": 3.3})
y = yogurt = SmartCounter({"kcal": 51, "prot": 9})
ch = cheese = SmartCounter({"kcal": 330, "prot": 22.5})
f = flakes = SmartCounter({"kcal": 380, "prot": 8})
b = beans = SmartCounter({"kcal": 310, "prot": 24})
e = egg = SmartCounter({"kcal": 80, "prot": 12})
g = grud = SmartCounter({"kcal": 140, "prot": 25})
p = porosh = SmartCounter({"kcal": 379, "prot": 86.4})
ca = cabb = SmartCounter({"kcal": 15, "prot": 0.6})
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")
st.title("Calculator")

st.markdown("---")
