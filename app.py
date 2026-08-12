import streamlit as st

st.set_page_config(
    page_title="FitBalance",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
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

.hero .byline {
    font-size:15px;
    font-weight:700;
    color:#5eead4;
    letter-spacing:.3px;
    margin-bottom:14px;
    text-transform:uppercase;
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
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">
    <h1>🏋️ FitBalance</h1>
    <div class="byline">Coached by Yazan</div>

    <p>
        Coach Yazan's personal fitness dashboard — clear numbers, balanced
        macros, and real food ideas that fit your goals.
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
        <div class="metric-title">Goal</div>
        <div class="metric-value" style="font-size:20px;">
            {goal}
        </div>
        <div class="metric-small">{gender}</div>
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
# TEEN SAFETY
# ============================================================

if age < 18:

    st.markdown("""
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
        "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80",
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
        "image": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=800&q=80",
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
        "image": "https://images.unsplash.com/photo-1519162808019-7de1683fa2ad?w=800&q=80",
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

        food_list = "".join(
            f"<li>{item}</li>"
            for item in food["foods"]
        )

        st.markdown(
            f"""
            <div class="food-card">

                <img src="{food["image"]}">

                <h3>{food["title"]}</h3>

                <ul class="food-list">
                    {food_list}
                </ul>

            </div>
            """,
            unsafe_allow_html=True
        )


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
    "image": "https://images.unsplash.com/photo-1517673400267-0251440c45dc?w=800&q=80",
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
    "image": "https://images.unsplash.com/photo-1543353071-873f17a7a088?w=800&q=80",
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
    "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=800&q=80",
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

    ingredients = "".join(
        f"<li>{item}</li>"
        for item in meal["ingredients"]
    )

    with col:

        st.markdown(
            f"""
            <div class="meal-card">

                <img src="{meal["image"]}">

                <div class="meal-content">

                    <div class="meal-title">
                        {meal["title"]}
                    </div>

                    <h3>
                        {meal["name"]}
                    </h3>

                    <p class="meal-description">
                        {meal["description"]}
                    </p>

                    <div class="meal-info">

                        <b>🛒 Ingredients</b>

                        <ul>
                            {ingredients}
                        </ul>

                        <b>💡 Why?</b><br>

                        {meal["note"]}

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# DAILY MEAL STRUCTURE
# ============================================================

st.markdown(
    '<div class="section-title">📅 Simple Daily Structure</div>',
    unsafe_allow_html=True
)

structure = st.columns(4)

daily = [
    ("🌅 Breakfast", "Protein + carbs + fruit"),
    ("☀️ Lunch", "Protein + carbs + vegetables"),
    ("🍎 Snack", "Fruit + yogurt / nuts"),
    ("🌙 Dinner", "Protein + vegetables + carbs")
]

for col, (title, text) in zip(structure, daily):

    with col:

        st.markdown(
            f"""
            <div class="card">

                <div class="metric-title">
                    {title}
                </div>

                <div style="
                    color:white;
                    font-weight:700;
                    font-size:16px;
                ">
                    {text}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "FitBalance provides educational estimates. Individual nutritional "
    "needs vary, and BMI is only a screening measure."
)
