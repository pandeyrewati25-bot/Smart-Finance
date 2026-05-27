# ==========================================================
# SMART SUSTAINABLE FINANCE PLANNER
# Premium Professional Finance Dashboard
# Streamlit + Plotly
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Smart Sustainable Finance Planner",
    page_icon="🌱",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* ======================================================
BACKGROUND
====================================================== */

.stApp {

    background:
    linear-gradient(
        rgba(4, 12, 20, 0.90),
        rgba(4, 12, 20, 0.92)
    ),

    url("https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?q=80&w=1974&auto=format&fit=crop");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;

    color: white;
}

/* ======================================================
TITLE
====================================================== */

h1 {

    color: #E8F5E9 !important;

    font-size: 48px !important;

    font-weight: bold !important;

    text-align: center;

    margin-bottom: 10px;
}

/* ======================================================
SECTION TITLE
====================================================== */

.section-title {

    background: linear-gradient(
        90deg,
        rgba(46,125,50,0.95),
        rgba(25,118,210,0.90)
    );

    padding: 14px 20px;

    border-radius: 14px;

    margin-top: 35px;

    margin-bottom: 20px;

    color: white;

    font-size: 28px;

    font-weight: bold;

    border-left: 6px solid #FFD54F;

    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
}

/* ======================================================
INFO BOX
====================================================== */

.info-box {

    background: rgba(255,255,255,0.06);

    padding: 18px;

    border-radius: 15px;

    margin-bottom: 20px;

    border: 1px solid rgba(255,255,255,0.08);
}

/* ======================================================
METRIC CARDS
====================================================== */

[data-testid="metric-container"] {

    background: rgba(14, 28, 52, 0.92);

    border-radius: 18px;

    padding: 22px;

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow: 0 6px 20px rgba(0,0,0,0.45);
}

/* ======================================================
METRIC TEXT
====================================================== */

[data-testid="stMetricLabel"] {

    color: white !important;

    font-size: 16px !important;
}

[data-testid="stMetricValue"] {

    color: #66BB6A !important;

    font-size: 30px !important;

    font-weight: bold !important;
}

/* ======================================================
INPUTS
====================================================== */

.stTextInput input,
.stNumberInput input {

    background-color: rgba(17, 34, 64, 0.95) !important;

    color: white !important;

    border-radius: 10px !important;

    border: 1px solid #2E7D32 !important;
}

/* ======================================================
LABELS
====================================================== */

label {

    color: white !important;

    font-weight: 600 !important;
}

/* ======================================================
BUTTON
====================================================== */

.stButton button {

    background: linear-gradient(
        90deg,
        #2E7D32,
        #66BB6A
    );

    color: white;

    font-weight: bold;

    border-radius: 12px;

    border: none;

    padding: 12px 28px;

    font-size: 16px;

    transition: 0.3s;
}

.stButton button:hover {

    background: linear-gradient(
        90deg,
        #FFD54F,
        #FFCA28
    );

    color: black;

    transform: scale(1.03);
}

/* ======================================================
CUSTOM TABLE DESIGN
====================================================== */

.custom-table {

    width: 100%;

    border-collapse: collapse;

    overflow: hidden;

    border-radius: 18px;

    background: rgba(10, 25, 47, 0.92);

    box-shadow: 0 6px 20px rgba(0,0,0,0.4);

    margin-top: 10px;
}

.custom-table thead {

    background: linear-gradient(
        90deg,
        #1B5E20,
        #1565C0
    );
}

.custom-table th {

    color: white;

    padding: 16px;

    text-align: left;

    font-size: 17px;
}

.custom-table td {

    padding: 15px;

    color: #ECEFF1;

    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.custom-table tr:hover {

    background-color: rgba(255,255,255,0.05);
}

/* ======================================================
PROGRESS BAR
====================================================== */

.stProgress > div > div > div > div {

    background-color: #66BB6A;
}

/* ======================================================
ALERT BOXES
====================================================== */

.stSuccess,
.stWarning,
.stError {

    border-radius: 12px;
}

/* ======================================================
PLOTLY LEGEND
====================================================== */

.js-plotly-plot .plotly .legend text {

    fill: white !important;
}

footer {

    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================

st.title("🌱 Smart Sustainable Finance Planner")

st.markdown("""
<div class="info-box">

### 💰 Middle Class Sustainable Finance Dashboard

✅ Budget Planning  
✅ Savings & SIP  
✅ Emergency Fund  
✅ Government Schemes  
✅ Sustainable Financial Growth  

</div>
""", unsafe_allow_html=True)

# ==========================================================
# BASIC INFORMATION
# ==========================================================

st.markdown(
    '<div class="section-title">👤 Basic Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Enter Your Name",
        "Rahul Sharma"
    )

    monthly_salary = st.number_input(
        "Monthly Salary (₹)",
        min_value=0,
        value=50000
    )

with col2:

    age = st.number_input(
        "Your Age",
        min_value=18,
        max_value=80,
        value=30
    )

    family_members = st.number_input(
        "Family Members",
        min_value=1,
        max_value=15,
        value=4
    )

# ==========================================================
# MONTHLY EXPENSES
# ==========================================================

st.markdown(
    '<div class="section-title">🏠 Monthly Expenses</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    rent = st.number_input("House Rent / EMI", value=12000)
    groceries = st.number_input("Groceries", value=7000)
    transport = st.number_input("Transport", value=3000)
    school_fees = st.number_input("School Fees", value=2000)

with col2:

    electricity = st.number_input("Electricity + Internet", value=2500)
    entertainment = st.number_input("Entertainment", value=3000)
    loan_emi = st.number_input("Loan EMI", value=0)
    other_expenses = st.number_input("Other Expenses", value=2000)

# ==========================================================
# SAVINGS & INSURANCE
# ==========================================================

st.markdown(
    '<div class="section-title">🏦 Savings & Insurance</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    emergency_fund = st.number_input(
        "Emergency Fund",
        value=10000
    )

    investments = st.number_input(
        "Current Investments",
        value=0
    )

with col2:

    health_insurance = st.selectbox(
        "Health Insurance",
        [
            "No Insurance",
            "Employer Insurance Only",
            "Basic Insurance",
            "Good Insurance"
        ]
    )

# ==========================================================
# BUTTON
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button("📊 Generate My Financial Plan")

# ==========================================================
# ANALYSIS
# ==========================================================

if analyze:

    total_expenses = (
        rent + groceries + transport +
        school_fees + electricity +
        entertainment + loan_emi +
        other_expenses
    )

    surplus = monthly_salary - total_expenses

    savings_rate = (
        surplus / monthly_salary * 100
        if monthly_salary > 0 else 0
    )

    target_emergency = total_expenses * 6

    # ======================================================
    # FINANCIAL ANALYSIS
    # ======================================================

    st.markdown(
        '<div class="section-title">📈 Financial Analysis</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Salary", f"₹{monthly_salary:,.0f}")
    c2.metric("Expenses", f"₹{total_expenses:,.0f}")
    c3.metric("Savings", f"₹{surplus:,.0f}")
    c4.metric("Savings %", f"{savings_rate:.1f}%")

    # ======================================================
    # SMART INSIGHTS
    # ======================================================

    st.markdown(
        '<div class="section-title">🧠 Smart Financial Insights</div>',
        unsafe_allow_html=True
    )

    if entertainment > 5000:
        st.warning("⚠️ Entertainment expenses high hain.")

    if groceries > 10000:
        st.warning("⚠️ Grocery spending reduce kar sakte hain.")

    if loan_emi > monthly_salary * 0.30:
        st.error("⚠️ EMI burden high hai.")

    if surplus > 0:

        st.success(
            f"""
            ✅ Aap har month approx ₹{surplus:,.0f}
            save kar sakte hain.

            Suggested Focus:
            • SIP Investment
            • PPF / NPS
            • Emergency Fund
            """
        )

    else:

        st.error("❌ Expenses income se zyada hain.")

    # ======================================================
    # EXPENSE DISTRIBUTION
    # ======================================================

    st.markdown(
        '<div class="section-title">📉 Expense Distribution</div>',
        unsafe_allow_html=True
    )

    labels = [
        "Rent", "Groceries", "Transport",
        "School", "Bills", "Entertainment",
        "Loan", "Other", "Savings"
    ]

    values = [
        rent, groceries, transport,
        school_fees, electricity,
        entertainment, loan_emi,
        other_expenses, max(surplus, 0)
    ]

    chart_df = pd.DataFrame({
        "Category": labels,
        "Amount": values
    })

    colors = [
        "#66BB6A",
        "#29B6F6",
        "#FFD54F",
        "#FF7043",
        "#AB47BC",
        "#26C6DA",
        "#EF5350",
        "#8D6E63",
        "#43A047"
    ]

    fig = px.pie(
        chart_df,
        names="Category",
        values="Amount",
        hole=0.45,
        color_discrete_sequence=colors
    )

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        insidetextorientation='radial',
        textfont=dict(
            color="white",
            size=14
        ),
        marker=dict(
            line=dict(
                color='white',
                width=2
            )
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            color="white",
            size=15
        ),
        legend=dict(
            font=dict(
                color="white",
                size=14
            )
        ),
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ======================================================
    # RECOMMENDED SAVINGS PLAN
    # ======================================================

    st.markdown(
        '<div class="section-title">💹 Recommended Savings Plan</div>',
        unsafe_allow_html=True
    )

    if surplus > 0:

        savings_df = pd.DataFrame({

            "Investment Type": [
                "Emergency Fund",
                "Mutual Fund SIP",
                "PPF",
                "Gold Savings",
                "Extra Savings"
            ],

            "Monthly Amount": [
                int(surplus * 0.30),
                int(surplus * 0.30),
                int(surplus * 0.20),
                int(surplus * 0.10),
                int(surplus * 0.10)
            ]
        })

        st.markdown(
            savings_df.to_html(
                classes='custom-table',
                index=False
            ),
            unsafe_allow_html=True
        )

    # ======================================================
    # GOVERNMENT SAVING SCHEMES
    # ======================================================

    st.markdown(
        '<div class="section-title">🏛️ Government Saving Schemes</div>',
        unsafe_allow_html=True
    )

    schemes_df = pd.DataFrame({

        "Scheme": [
            "PPF",
            "NPS",
            "Atal Pension Yojana",
            "PMJJBY",
            "PMSBY"
        ],

        "Benefits": [
            "Long-term tax free savings",
            "Retirement pension benefits",
            "Guaranteed pension scheme",
            "₹2 lakh life insurance",
            "₹2 lakh accident insurance"
        ]
    })

    st.markdown(
        schemes_df.to_html(
            classes='custom-table',
            index=False
        ),
        unsafe_allow_html=True
    )

    # ======================================================
    # EMERGENCY FUND STATUS
    # ======================================================

    st.markdown(
        '<div class="section-title">🛡️ Emergency Fund Status</div>',
        unsafe_allow_html=True
    )

    progress = min(
        emergency_fund / target_emergency,
        1.0
    )

    st.progress(progress)

    st.write(
        f"""
        ₹{emergency_fund:,.0f}
        saved out of
        ₹{target_emergency:,.0f}
        """
    )

    # ======================================================
    # FINAL ADVICE
    # ======================================================

    st.markdown(
        '<div class="section-title">📋 Final Advice</div>',
        unsafe_allow_html=True
    )

    advice = []

    if entertainment > 5000:
        advice.append("⚠️ Entertainment expenses reduce kariye.")

    if investments == 0:
        advice.append("✅ SIP investment start kariye.")

    if emergency_fund < target_emergency:
        advice.append("✅ Emergency fund build kariye.")

    if loan_emi > monthly_salary * 0.30:
        advice.append("⚠️ EMI burden kam kariye.")

    for item in advice:
        st.write(item)

    # ======================================================
    # FOOTER
    # ======================================================

    st.markdown("---")

    st.success(
        f"🎉 {name}, your sustainable finance report is ready!"
    )

    st.caption(
        "Made with ❤️ using Streamlit + Plotly"
    )