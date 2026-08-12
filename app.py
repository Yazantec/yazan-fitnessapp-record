import streamlit as st
import textwrap

st.set_page_config(
    page_title="FitBalance",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# STYLE
# ============================================================

st.markdown(textwrap.dedent("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(34,197,94,.15), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(59,130,246,.15), transparent 30%),
        linear-gradient(135deg,#07111f 0%,#0b1728 50%,#071a16 100%);
    color:#f8fafc;
    font-family:'Inter',sans-serif;
}

.block-container {
    max-width:1250px;
    padding-top:2rem;
    padding-bottom:3rem;
}

.hero {
    padding:42px;
    border-radius:28px;
    margin-bottom:30px;
    background:linear-gradient(
        135deg,
        rgba(16,185,129,.25),
        rgba(37,99,235,.20)
    );
    border:1px solid rgba(255,255,255,.12);
    box-shadow:0 20px 60px rgba(0,0,0,.30);
}

.hero h1 {
    font-size:48px !important;
    font-weight:800 !important;
    margin-bottom:8px;
}

.hero p {
    font-size:17px;
    color:#cbd5e1;
    max-width:850px;
}

.card {
    background:rgba(255,255,255,.065);
    border:1px solid rgba(255,255,255,.10);
    border-radius:22px;
    padding:22px;
    box-shadow:0 12px 35px rgba(0,0,0,.20);
}

.metric-title {
    color:#94a3b8;
    font-size:14px;
    margin-bottom:8px;
}

.metric-value {
    font-size:30px;
    font-weight:800;
    color:white;
}

.metric-small {
    color:#94a3b8;
    font-size:13px;
    margin-top:4px;
}

.section-title {
    font-size:27px;
    font-weight:800;
    margin-top:35px;
    margin-bottom:18px;
}

.tip {
    background:rgba(34,197,94,.08);
    border-left:4px solid #22c55e;
    border-radius:12px;
    padding:16px;
    margin-bottom:12px;
}

.warning {
    background:rgba(245,158,11,.10);
    border-left:4px solid #f59e0b;
    border-radius:12px;
    padding:18px;
    margin:20px 0;
}

.food-card {
    background:rgba(255,255,255,.065);
    border:1px solid rgba(255,255,255,.10);
    border-radius:20px;
    padding:12px;
    height:100%;
    margin-bottom:15px;
}

.food-card img {
    width:100%;
    height:190px;
    object-fit:cover;
    border-radius:15px;
}

.food-card h3 {
    margin-top:14px;
    color:white;
}

.food-card p {
    color:#cbd5e1;
}

.food-list {
    color:#cbd5e1;
    line-height:1.8;
}

.meal-card {
    background:linear-gradient(
        145deg,
        rgba(255,255,255,.075),
        rgba(255,255,255,.035)
    );
    border:1px solid rgba(255,255,255,.11);
    border-radius:24px;
    overflow:hidden;
    height:100%;
    box-shadow:0 15px 40px rgba(0,0,0,.22);
}

.meal-card img {
    width:100%;
    height:240px;
    object-fit:cover;
}

.meal-content {
    padding:20px;
}

.meal-title {
    font-size:23px;
    font-weight:800;
    color:white;
    margin-bottom:8px;
}

.meal-description {
    color:#cbd5e1;
    line-height:1.6;
}

.meal-info {
    margin-top:15px;
    padding:12px;
    background:rgba(255,255,255,.05);
    border-radius:13px;
    color:#dbeafe;
}

.stButton > button {
    width:100%;
    border-radius:12px;
    font-weight:700;
}

section[data-testid="stSidebar"] {
    background:rgba(5,15,25,.95);
}

</style>
"""), unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown(textwrap.dedent("""
<div class="hero">
    <h1>🏋️ FitBalance</h1>

    <p>
        Your personal fitness dashboard for understanding BMI,
        estimating daily energy needs, building balanced macros,
        and discovering simple healthy food and meal ideas.
    </p>
</div>
"""), unsafe_allow_html=True)


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

if gender == "Male":
    bmr = (
        10 * weight
        + 6.25 * height
        - 5 * age
        + 5
    )
else:
    bmr = (
        10 * weight
        + 6.25 * height
        - 5 * age
        - 161
    )


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

    carbs = max(
        remaining_calories / 4,
        0
    )

else:

    protein = weight * 1.2
    fat = (tdee * .30) / 9

    carbs = max(
        (tdee - protein * 4 - fat * 9) / 4,
        0
    )


protein = round(protein)
carbs = round(carbs)
fat = round(fat)


# ============================================================
# BMI
# ============================================================

if age < 18:
    bmi_category = "Use age-specific growth charts."

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
    st.markdown(textwrap.dedent(f"""
    <div class="card">
        <div class="metric-title">BMI</div>
        <div class="metric-value">{bmi:.1f}</div>
        <div class="metric-small">{bmi_category}</div>
    </div>
    """), unsafe_allow_html=True)

with c2:
    st.markdown(textwrap.dedent(f"""
    <div class="card">
        <div class="metric-title">BMR</div>
        <div class="metric-value">{bmr:.0f}</div>
        <div class="metric-small">Estimated kcal/day at rest</div>
    </div>
    """), unsafe_allow_html=True)

with c3:
    st.markdown(textwrap.dedent(f"""
    <div class="card">
        <div class="metric-title">Daily Energy</div>
        <div class="metric-value">{tdee:.0f}</div>
        <div class="metric-small">Estimated kcal/day</div>
    </div>
    """), unsafe_allow_html=True)

with c4:
    st.markdown(textwrap.dedent(f"""
    <div class="card">
        <div class="metric-title">Goal</div>
        <div class="metric-value" style="font-size:20px;">
            {goal}
        </div>
        <div class="metric-small">{gender}</div>
    </div>
    """), unsafe_allow_html=True)


# ============================================================
# MACROS
# ============================================================

st.markdown(
    '<div class="section-title">🥗 Daily Macro Estimate</div>',
    unsafe_allow_html=True
)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(textwrap.dedent(f"""
    <div class="card">
        <div class="metric-title">🥩 Protein</div>
        <div class="metric-value">{protein} g</div>
        <div class="metric-small">{protein * 4} kcal</div>
    </div>
    """), unsafe_allow_html=True)

with m2:
    st.markdown(textwrap.dedent(f"""
    <div class="card">
        <div class="metric-title">🍚 Carbohydrates</div>
        <div class="metric-value">{carbs} g</div>
        <div class="metric-small">{carbs * 4} kcal</div>
    </div>
    """), unsafe_allow_html=True)

with m3:
    st.markdown(textwrap.dedent(f"""
    <div class="card">
        <div class="metric-title">🥑 Healthy Fats</div>
        <div class="metric-value">{fat} g</div>
        <div class="metric-small">{fat * 9} kcal</div>
    </div>
    """), unsafe_allow_html=True)


# ============================================================
# TEEN SAFETY
# ============================================================

if age < 18:

    st.markdown(textwrap.dedent("""
    <div class="warning">

        <b>⚠️ Important</b>

        <br><br>

        For teenagers, calorie and BMI calculations are only rough
        educational estimates. Growing bodies have changing nutritional
        needs, so this app should not be used to restrict calories or
        create a weight-loss diet.

        <br><br>

        Focus on balanced meals, regular activity, sleep and overall
        wellbeing. If you have concerns about nutrition or growth,
        speak with a parent/guardian and a qualified healthcare professional.

    </div>
    """), unsafe_allow_html=True)


# ============================================================
# LONG TERM TIPS
# ============================================================

st.markdown(
    '<div class="section-title">🌱 Long-Term Improvement</div>',
    unsafe_allow_html=True
)

tips = [
    (
        "🥗 Build balanced meals",
        "Combine protein, vegetables or fruit, carbohydrates and healthy fats throughout the day."
    ),

    (
        "💪 Stay active",
        "Focus on gradually improving strength, fitness and movement instead of chasing quick results."
    ),

    (
        "😴 Sleep well",
        "Consistent sleep supports recovery, concentration, mood and physical performance."
    ),

    (
        "💧 Stay hydrated",
        "Water is a simple everyday choice, especially during exercise and hot weather."
    ),

    (
        "📈 Think long term",
        "Small habits repeated consistently are more sustainable than extreme changes."
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
# FOOD SOURCES
# ============================================================

st.markdown(
    '<div class="section-title">🥗 Healthy Food Sources</div>',
    unsafe_allow_html=True
)

food_sources = [

    {
        "title": "🥩 Protein",
        "image": "https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/2147491336/images/6b57555-118-c5b6-a407-d0edc587d3e_How_Much_Protein_Women_Need_to_Build_Muscle.jpg",
        "foods": [
            "Chicken breast",
            "Eggs",
            "Fish",
            "Greek yogurt",
            "Lentils",
            "Beans"
        ]
    },

    {
        "title": "🍚 Carbohydrates",
        "image": "https://cdn.salla.sa/vwaxy/TOzIvJkMHc7rmGkzOYQrLWUKmWZyDLG8wArXWMvE.png",
        "foods": [
            "Oats",
            "Rice",
            "Potatoes",
            "Whole grains",
            "Whole-grain bread",
            "Fruit"
        ]
    },

    {
        "title": "🥑 Healthy Fats",
        "image": "https://static.wixstatic.com/media/b8b90e_069601d4669b48528460378624151f1f~mv2.png/v1/fill/w_980%2Ch_980%2Cal_c%2Cq_90%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/b8b90e_069601d4669b48528460378624151f1f~mv2.png",
        "foods": [
            "Avocado",
            "Almonds",
            "Walnuts",
            "Seeds",
            "Olive oil",
            "Tahini"
        ]
    }
]

food_cols = st.columns(3)

for col, food in zip(food_cols, food_sources):

    with col:
        with st.container(border=True):
            st.image(food["image"], use_container_width=True)
            st.markdown(f"### {food['title']}")

            for item in food["foods"]:
                st.markdown(f"✓ {item}")


# ============================================================
# HEALTHY MEALS
# ============================================================

st.markdown(
    '<div class="section-title">🍽️ Healthy Meal Ideas</div>',
    unsafe_allow_html=True
)

st.write(
    "Simple meal ideas built around a mix of protein, carbohydrates, "
    "healthy fats and fruit/vegetables."
)


# ============================================================
# BREAKFAST
# ============================================================

breakfast = {
    "title": "🌅 Healthy Breakfast",
    "name": "Oatmeal + Eggs + Fruit",
    "image": "https://media.suvalgyk.lt/suvalgyk_recipes/avizine-kose-su-vaisiais-ir-virtais-kiausiniais-a22d14d2.png",
    "description": (
        "A simple breakfast combining oats, eggs and fruit. "
        "It gives you carbohydrates, protein, fiber and useful micronutrients."
    ),
    "ingredients": [
        "Oats",
        "2 eggs",
        "Banana or berries",
        "Milk or Greek yogurt",
        "Cinnamon"
    ],
    "note": "Balanced combination of protein + carbs + fruit."
}


# ============================================================
# LUNCH
# ============================================================

lunch = {
    "title": "☀️ Healthy Lunch",
    "name": "Chicken Rice Power Bowl",
    "image": "https://snapcalorie-webflow-website.s3.us-east-2.amazonaws.com/media/food_pics_v2/medium/chicken_and_rice_bowl.jpg",
    "description": (
        "A colorful bowl with chicken, rice and vegetables. "
        "You can customize the vegetables and add avocado or olive oil."
    ),
    "ingredients": [
        "Chicken breast",
        "Rice",
        "Broccoli",
        "Carrots",
        "Tomatoes",
        "Avocado"
    ],
    "note": "Great combination of protein + carbohydrates + vegetables."
}


# ============================================================
# DINNER
# ============================================================

dinner = {
    "title": "🌙 Healthy Dinner",
    "name": "Salmon + Potatoes + Vegetables",
    "image": "https://www.fitfoodway.co.uk/media/produse/salmon-file-with-boiled-potatoes-broccoli-and-cherry-tomatoes.jpg",
    "description": (
        "A balanced dinner featuring salmon, potatoes and vegetables. "
        "Salmon provides protein and healthy fats while potatoes provide carbohydrates."
    ),
    "ingredients": [
        "Salmon",
        "Potatoes",
        "Broccoli",
        "Cherry tomatoes",
        "Lemon",
        "Herbs"
    ],
    "note": "Protein + healthy fats + carbohydrates + vegetables."
}


meals = [breakfast, lunch, dinner]

meal_cols = st.columns(3)

for col, meal in zip(meal_cols, meals):

    with col:
        with st.container(border=True):
            st.image(meal["image"], use_container_width=True)
            st.markdown(f"### {meal['title']}")
            st.markdown(f"#### {meal['name']}")
            st.write(meal["description"])

            st.markdown("**🛒 Ingredients**")
            for item in meal["ingredients"]:
                st.markdown(f"✓ {item}")

            st.markdown("**💡 Why?**")
            st.write(meal["note"])


# ============================================================
# DAILY MEAL STRUCTURE
# ============================================================

st.markdown("## 📅 Simple Daily Structure")

structure = st.columns(4)

daily = [
    ("🌅 Breakfast", "Protein + carbs + fruit"),
    ("☀️ Lunch", "Protein + carbs + vegetables"),
    ("🍎 Snack", "Fruit + yogurt / nuts"),
    ("🌙 Dinner", "Protein + vegetables + carbs")
]

for col, (title, text) in zip(structure, daily):
    with col:
        with st.container(border=True):
            st.markdown(f"### {title}")
            st.markdown(f"**{text}**")


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "FitBalance provides educational estimates. Individual nutritional "
    "needs vary, and BMI is only a screening measure."
)
