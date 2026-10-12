import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Smart Waste Management",
    page_icon="♻️",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("♻️ Smart Waste Management System")
st.subheader("Waste Collection Prediction using Machine Learning")

st.write(
    "A Machine Learning based system for monitoring "
    "waste levels and predicting collection time."
)

st.divider()

# =====================================================
# DATASET
# =====================================================

data = {
    "area": [
        1,1,1,1,1,
        2,2,2,2,2,
        3,3,3,3,3,
        4,4,4,4,4,
        5,5,5,5,5
    ],

    "bin_capacity": [
        100,100,100,100,100,
        120,120,120,120,120,
        80,80,80,80,80,
        150,150,150,150,150,
        100,100,100,100,100
    ],

    "waste_level": [
        30,45,60,75,90,
        25,40,55,70,95,
        20,35,50,65,85,
        30,50,65,80,95,
        25,45,60,75,90
    ],

    "hour": [
        8,9,10,11,12,
        8,9,10,11,12,
        8,9,10,11,12,
        8,9,10,11,12,
        8,9,10,11,12
    ],

    "day": [
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5
    ],

    "month": [
        9,9,9,9,9,
        9,9,9,9,9,
        9,9,9,9,9,
        9,9,9,9,9,
        9,9,9,9,9
    ],

    "dayofweek": [
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5
    ],

    "collection_time_hours": [
        10,8,6,4,2,
        11,9,7,5,2,
        12,10,7,5,3,
        11,8,6,4,2,
        10,8,6,4,2
    ]
}

df = pd.DataFrame(data)

# =====================================================
# MACHINE LEARNING MODEL
# =====================================================

features = [
    "area",
    "bin_capacity",
    "waste_level",
    "hour",
    "day",
    "month",
    "dayofweek"
]

X = df[features]
y = df["collection_time_hours"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("♻️ Project Menu")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Waste Analysis",
        "Collection Prediction",
        "Dataset"
    ]
)

# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.header("📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Records",
            len(df)
        )

    with col2:
        st.metric(
            "Average Waste",
            f"{df['waste_level'].mean():.1f}%"
        )

    with col3:
        st.metric(
            "Average Collection Time",
            f"{df['collection_time_hours'].mean():.1f} hrs"
        )

    with col4:
        st.metric(
            "Maximum Waste",
            f"{df['waste_level'].max()}%"
        )

    st.divider()

    st.subheader("📈 Waste Level Trend")

    chart = df[["waste_level"]].copy()
    chart.index = range(1, len(chart) + 1)

    st.line_chart(chart)

    st.subheader("🏙️ Area-wise Waste Level")

    area_waste = df.groupby("area")["waste_level"].mean()

    st.bar_chart(area_waste)

    st.subheader("🚛 Area-wise Collection Time")

    area_collection = (
        df.groupby("area")["collection_time_hours"]
        .mean()
    )

    st.bar_chart(area_collection)

# =====================================================
# WASTE ANALYSIS
# =====================================================

elif page == "Waste Analysis":

    st.header("🗑️ Waste Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Waste Level by Area")

        waste = df.groupby("area")["waste_level"].mean()

        st.bar_chart(waste)

    with col2:

        st.subheader("Bin Capacity by Area")

        capacity = df.groupby("area")["bin_capacity"].mean()

        st.bar_chart(capacity)

    st.divider()

    st.subheader("📊 Waste Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Minimum Waste",
        f"{df['waste_level'].min()}%"
    )

    c2.metric(
        "Average Waste",
        f"{df['waste_level'].mean():.1f}%"
    )

    c3.metric(
        "Maximum Waste",
        f"{df['waste_level'].max()}%"
    )

# =====================================================
# COLLECTION PREDICTION
# =====================================================

elif page == "Collection Prediction":

    st.header("🔮 Waste Collection Prediction")

    st.write(
        "Enter the current bin information "
        "to predict the estimated collection time."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "Area ID",
            min_value=1,
            max_value=20,
            value=1
        )

        bin_capacity = st.number_input(
            "Bin Capacity (%)",
            min_value=0.0,
            max_value=100.0,
            value=100.0
        )

        waste_level = st.number_input(
            "Current Waste Level (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

    with col2:

        hour = st.slider(
            "Current Hour",
            0,
            23,
            12
        )

        day = st.slider(
            "Day of Month",
            1,
            31,
            15
        )

        month = st.slider(
            "Month",
            1,
            12,
            9
        )

        dayofweek = st.slider(
            "Day of Week",
            0,
            6,
            1
        )

    st.divider()

    if st.button(
        "🔮 Predict Collection Time",
        use_container_width=True
    ):

        input_data = pd.DataFrame([[
            area,
            bin_capacity,
            waste_level,
            hour,
            day,
            month,
            dayofweek
        ]], columns=features)

        prediction = model.predict(input_data)[0]

        st.success(
            f"🚛 Estimated Collection Time: "
            f"{prediction:.2f} hours"
        )

        if prediction <= 3:

            st.error(
                "🔴 URGENT: Waste collection "
                "should be scheduled soon!"
            )

        elif prediction <= 6:

            st.warning(
                "🟠 Collection should be "
                "scheduled within a few hours."
            )

        else:

            st.info(
                "🟢 Immediate collection "
                "may not be required."
            )

# =====================================================
# DATASET
# =====================================================

elif page == "Dataset":

    st.header("📋 Waste Management Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    st.subheader("📊 Dataset Statistics")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Smart Waste Management and Collection Prediction | "
    "BSc Data Science Project"
)