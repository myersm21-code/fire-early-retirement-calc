import streamlit as st

# 1. Page Configuration (SEO Optimized for FIRE & Finance)
st.set_page_config(
    page_title="FIRE Reality Check | Early Retirement Calculator",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "A professional-grade utility for the FIRE community to calculate their 'Freedom Number'."
    }
)

# 2. CUSTOM CSS (Wealth & Stability Facelift)
st.markdown("""
    <style>
    .main { background-color: #f0f4f2; }
    .stNumberInput div div input { border-radius: 10px; border: 2px solid #1b5e20; }
    .stButton button { 
        width: 100%; 
        border-radius: 25px; 
        background-color: #1b5e20; 
        color: white; 
        font-weight: bold; 
        height: 3.5em;
        transition: 0.3s;
    }
    .stButton button:hover { background-color: #0d3b13; border: none; }
    .fire-box { 
        padding: 30px; 
        border-radius: 15px; 
        background-color: white; 
        border: 2px solid #1b5e20; 
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar & Anonymous Tip Jar
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/safe.png", width=120)
    st.markdown("### THE NICHE DECODER")
    st.write("Decoding the math behind early retirement.")
    st.divider()
    st.link_button("☕ Support the Decoder", "https://buymeacoffee.com/the_niche_decoder")
    st.divider()
    st.caption("v1.0 - FIRE Series")

# 4. Main Interface
st.title("🔥 FIRE Reality Check")
st.markdown("### When can you actually walk away?")

# Input Section
col1, col2 = st.columns(2)

with col1:
    annual_expenses = st.number_input("Annual Living Expenses ($)", min_value=1000, value=60000, step=1000)
    current_savings = st.number_input("Current Portfolio Size ($)", min_value=0, value=100000, step=5000)

with col2:
    withdrawal_rate = st.slider("Safe Withdrawal Rate (%)", 2.0, 6.0, 4.0, 0.1, help="4% is the industry standard (Trinity Study).")
    annual_contributions = st.number_input("Annual Savings Contribution ($)", min_value=0, value=20000, step=1000)

# 5. Calculation Logic
# The 'Freedom Number' (Expenses / SWR)
freedom_number = annual_expenses / (withdrawal_rate / 100)
gap = max(0.0, freedom_number - current_savings)

# Simplified compound interest to estimate years to FIRE (assuming 7% market return)
years_to_fire = 0
projected_portfolio = current_savings
if gap > 0:
    while projected_portfolio < freedom_number and years_to_fire < 50:
        projected_portfolio = (projected_portfolio * 1.07) + annual_contributions
        years_to_fire += 1

# 6. Results
if st.button("📈 CALCULATE FREEDOM DATE"):
    st.divider()
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Freedom Number", f"${freedom_number:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Years to FIRE", f"~{years_to_fire}")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        progress = (current_savings / freedom_number) * 100 if freedom_number > 0 else 100
        st.metric("Progress", f"{progress:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    
    # Verdict Logic
    if progress >= 100:
        verdict = "🎉 YOU ARE FIRE"
        color = "#1b5e20"
        advice = "Your portfolio can officially support your lifestyle. You are working for fun now."
    elif years_to_fire <= 10:
        verdict = "🚀 ON THE FAST TRACK"
        color = "#2e7d32"
        advice = f"You are less than a decade away. Stay the course and avoid lifestyle creep."
    else:
        verdict = "🐢 THE LONG GAME"
        color = "#555"
        advice = "You have a solid start. Consider increasing contributions or lowering expenses to accelerate the timeline."

    st.markdown(f"""
    <div class="fire-box">
        <h2 style="color: {color};">{verdict}</h2>
        <p style="font-size: 18px; color: #555;">{advice}</p>
        <p style="font-size: 14px; color: #888;">Assumes 7% real market return. Actual results may vary based on inflation and market volatility.</p>
    </div>
    """, unsafe_allow_html=True)

# 7. Final Attribution
st.divider()
st.caption("Developed by The Niche Decoder Factory. Anonymous & Math-Driven.")
