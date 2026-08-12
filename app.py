import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="FitBalance",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(34,197,94,0.15), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(59,130,246,0.15), transparent 30%),
        linear-gradient(135deg, #07111f 0%, #0b1728 50%, #071a16 100%);
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hero */
.hero {
    padding: 42px;
    border-radius: 28px;
    margin-bottom: 30px;
    background:
        linear-gradient(
            135deg,
            rgba(16,185,129,0.25),
            rgba(37,99,235,0.20)
        );
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 20px 60px rgba(0,0,0,0.30);
}

.hero h1 {
    font-size: 48px !important;
    font-weight: 800 !important;
    margin-bottom: 8px;
}

.hero p {
    font-size: 17px;
    color: #cbd5e1;
    max-width: 800px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.065);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.20);
}

.metric-title {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
    color: white;
}

.metric-small {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 4px;
}

/* Section titles */
.section-title {
    font-size: 26px;
    font-weight: 800;
    margin-top: 32px;
    margin-bottom: 18px;
}

/* Tips */
.tip {
    background: rgba(34,197,94,0.08);
    border-left: 4px solid #22c55e;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
}

.warning {
    background: rgba(245,158,11,0.10);
    border-left: 4px solid #f59e0b;
    border-radius: 12px;
    padding: 18px;
    margin: 20px 0;
}

/* Food cards */
.food-card {
    background: rgba(255,255,255,0.065);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 20px;
    padding: 12px;
    height: 100%;
}

.food-card img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 15px;
}

.food-card h3 {
    margin-top: 14px;
    color: white;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    font-weight: 700;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(5,15,25,0.95);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================
st.markdown("""
<div class="hero">
    <h1>🏋️ FitBalance</h1>
    <p>
        Your personal fitness dashboard for understanding BMI,
        estimating daily calorie needs, and building a balanced
        nutrition plan around protein, carbohydrates and healthy fats.
    </p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:

    st.header("📋 Your Details")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=13,
        max_value=100,
        value=18,
        step=1
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=230.0,
        value=170.0,
        step=0.5
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=250.0,
        value=70.0,
        step=0.5
    )

    activity = st.selectbox(
        "Activity Level",
        [
            "Sedentary",
            "Lightly Active",
            "Moderately Active",
            "Very Active",
            "Athlete"
        ]
    )

    goal = st.selectbox(
        "Main Goal",
        [
            "General Wellness",
            "Maintain Weight",
            "Build Muscle",
            "Improve Fitness"
        ]
    )

    calculate = st.button(
        "🚀 Calculate My Results",
        type="primary"
    )


# ============================================================
# CALCULATIONS
# ============================================================

height_m = height / 100

bmi = weight / (height_m ** 2)


# Mifflin-St Jeor equation
if gender == "Male":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161


activity_multiplier = {
    "Sedentary": 1.20,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
    "Athlete": 1.90
}

tdee = bmr * activity_multiplier[activity]


# ============================================================
# MACROS
# ============================================================

if age >= 18:

    if goal == "Build Muscle":
        protein = weight * 1.6
    else:
        protein = weight * 1.4

    fat = weight * 0.8

    remaining_calories = tdee - (
        protein * 4 +
        fat * 9
    )

    carbs = max(remaining_calories / 4, 0)

else:

    # Educational estimate only for minors.
    protein = weight * 1.2
    fat = (tdee * 0.30) / 9
    carbs = max(
        (tdee - protein * 4 - fat * 9) / 4,
        0
    )


protein = round(protein)
fat = round(fat)
carbs = round(carbs)


# ============================================================
# BMI CATEGORY
# ============================================================

if age < 18:

    bmi_category = "Teen BMI requires age- and sex-specific growth charts."

elif bmi < 18.5:

    bmi_category = "Below adult reference range."

elif bmi < 25:

    bmi_category = "Within adult reference range."

elif bmi < 30:

    bmi_category = "Above adult reference range."

else:

    bmi_category = "Higher adult reference range."


# ============================================================
# RESULTS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Your Results</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">BMI</div>
        <div class="metric-value">{bmi:.1f}</div>
        <div class="metric-small">{bmi_category}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">BMR</div>
        <div class="metric-value">{bmr:.0f}</div>
        <div class="metric-small">Estimated kcal/day at rest</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">Daily Energy</div>
        <div class="metric-value">{tdee:.0f}</div>
        <div class="metric-small">Estimated kcal/day</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">Gender</div>
        <div class="metric-value">{gender}</div>
        <div class="metric-small">{goal}</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MACROS
# ============================================================

st.markdown(
    '<div class="section-title">🥗 Daily Macro Estimate</div>',
    unsafe_allow_html=True
)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">🥩 Protein</div>
        <div class="metric-value">{protein} g</div>
        <div class="metric-small">{protein * 4} kcal</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">🍚 Carbohydrates</div>
        <div class="metric-value">{carbs} g</div>
        <div class="metric-small">{carbs * 4} kcal</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">🥑 Healthy Fats</div>
        <div class="metric-value">{fat} g</div>
        <div class="metric-small">{fat * 9} kcal</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SAFETY FOR TEENS
# ============================================================

if age < 18:

    st.markdown("""
    <div class="warning">
        <b>⚠️ Important:</b><br><br>
        For teenagers, calorie and BMI calculations are only rough educational
        estimates. Growing bodies have changing nutritional needs, so this app
        should not be used to restrict calories or create a weight-loss diet.
        Focus on balanced meals, regular activity, sleep and overall wellbeing.
        If you are concerned about your weight or nutrition, speak with a parent/
        guardian and a qualified healthcare professional.
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# LONG TERM TIPS
# ============================================================

st.markdown(
    '<div class="section-title">🌱 Long-Term Improvement</div>',
    unsafe_allow_html=True
)

tips = [
    (
        "🥗 Eat balanced meals",
        "Try to include protein, vegetables or fruit, carbohydrates and healthy fats across your meals."
    ),
    (
        "💪 Train consistently",
        "Focus on gradually improving strength, fitness and movement instead of looking for instant results."
    ),
    (
        "😴 Prioritize sleep",
        "Good sleep supports recovery, concentration, mood and physical performance."
    ),
    (
        "💧 Stay hydrated",
        "Water is a simple everyday choice, especially when you're active or the weather is hot."
    ),
    (
        "📈 Be patient",
        "Fitness is a long-term process. Small habits repeated consistently are more sustainable than extreme changes."
    ),
]

for title, description in tips:

    st.markdown(
        f"""
        <div class="tip">
            <b>{title}</b><br>
            {description}
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOD SECTION
# ============================================================

st.markdown(
    '<div class="section-title">🍽️ Healthy Food Sources</div>',
    unsafe_allow_html=True
)

foods = [

    (
        "🥩 Protein",
        "Chicken • Eggs • Fish • Greek Yogurt • Lentils",
        "https://images.unsplash.com/photo-1604503468506-a8da13d82791?auto=format&fit=crop&w=1000&q=80"
    ),

    (
        "🍚 Carbohydrates",
        "Oats • Rice • Potatoes • Whole Grains • Fruit",
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=1000&q=80"
    ),

    (
        "🥑 Healthy Fats",
        "Avocado • Nuts • Seeds • Olive Oil • Tahini",
        "https://images.unsplash.com/photo-1606787366850-de6330128bfc?auto=format&fit=crop&w=1000&q=80"
    )
]

food_cols = st.columns(3)

for col, food in zip(food_cols, foods):

    title, description, image = food

    with col:

        st.markdown(
            f"""
            <div class="food-card">

                <img src="{image}">

                <h3>{title}</h3>

                <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "FitBalance provides estimates for educational purposes. "
    "Individual nutritional needs vary, and BMI is only a screening measure."
)
