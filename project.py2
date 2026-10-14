import pandas as pd
import random
import os
import matplotlib.pyplot as plt

# ============================================================
# CAR SALES AND PRICE ANALYSIS
# 400 DATA RECORDS
# ============================================================

random.seed(100)

TOTAL_RECORDS = 400

# ============================================================
# 1. CAR DATA
# ============================================================

brands = [
    "Toyota", "Honda", "BMW", "Audi", "Ford",
    "Hyundai", "Mercedes", "Kia", "Tata", "Mahindra"
]

models = [
    "Sedan", "SUV", "Hatchback", "Coupe", "MPV"
]

fuel_types = [
    "Petrol", "Diesel", "CNG", "Electric"
]

cities = [
    "Pune", "Mumbai", "Nashik", "Nagpur",
    "Delhi", "Bengaluru", "Hyderabad", "Chennai"
]

data = []

for i in range(1, TOTAL_RECORDS + 1):

    data.append([
        i,
        random.choice(brands),
        f"{random.choice(models)} {random.randint(1, 9)}",
        random.randint(2015, 2026),
        random.randint(5000, 180000),
        random.choice(fuel_types),
        random.choice(cities),
        random.randint(250000, 4500000)
    ])

# ============================================================
# 2. DATAFRAME
# ============================================================

df = pd.DataFrame(
    data,
    columns=[
        "Car_ID",
        "Brand",
        "Model",
        "Year",
        "Kilometers_Driven",
        "Fuel_Type",
        "City",
        "Price_INR"
    ]
)

# ============================================================
# 3. BASIC ANALYSIS
# ============================================================

total_cars = len(df)

average_price = df["Price_INR"].mean()

minimum_price = df["Price_INR"].min()

maximum_price = df["Price_INR"].max()

average_km = df["Kilometers_Driven"].mean()

# ============================================================
# 4. BRAND SALES ANALYSIS
# ============================================================

brand_sales = (
    df["Brand"]
    .value_counts()
    .reset_index()
)

brand_sales.columns = [
    "Brand",
    "Sales_Count"
]

# ============================================================
# 5. BRAND PRICE ANALYSIS
# ============================================================

brand_price = (
    df
    .groupby("Brand")["Price_INR"]
    .mean()
    .reset_index()
)

brand_price.columns = [
    "Brand",
    "Average_Price_INR"
]

# ============================================================
# 6. FUEL TYPE ANALYSIS
# ============================================================

fuel_analysis = (
    df
    .groupby("Fuel_Type")
    .agg(
        Sales_Count=("Car_ID", "count"),
        Average_Price_INR=("Price_INR", "mean")
    )
    .reset_index()
)

# ============================================================
# 7. YEAR-WISE SALES
# ============================================================

year_sales = (
    df
    .groupby("Year")
    .size()
    .reset_index(name="Sales_Count")
)

# ============================================================
# 8. CITY-WISE SALES
# ============================================================

city_sales = (
    df["City"]
    .value_counts()
    .reset_index()
)

city_sales.columns = [
    "City",
    "Sales_Count"
]

# ============================================================
# 9. SUMMARY
# ============================================================

summary = pd.DataFrame({

    "Metric": [
        "Total Cars",
        "Average Price",
        "Minimum Price",
        "Maximum Price",
        "Average Kilometers",
        "Most Sold Brand"
    ],

    "Value": [
        total_cars,
        round(average_price, 2),
        minimum_price,
        maximum_price,
        round(average_km, 2),
        brand_sales.iloc[0]["Brand"]
    ]
})

# ============================================================
# 10. CREATE CHART FOLDER
# ============================================================

os.makedirs(
    "car_charts",
    exist_ok=True
)

# ============================================================
# 11. BRAND SALES CHART
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    brand_sales["Brand"],
    brand_sales["Sales_Count"]
)

plt.title("Car Sales by Brand")

plt.xlabel("Brand")

plt.ylabel("Number of Cars")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "car_charts/car_sales_by_brand.png"
)

plt.close()

# ============================================================
# 12. AVERAGE PRICE CHART
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    brand_price["Brand"],
    brand_price["Average_Price_INR"]
)

plt.title("Average Car Price by Brand")

plt.xlabel("Brand")

plt.ylabel("Average Price")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "car_charts/average_price_by_brand.png"
)

plt.close()

# ============================================================
# 13. YEAR-WISE SALES CHART
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    year_sales["Year"].astype(str),
    year_sales["Sales_Count"]
)

plt.title("Car Sales by Year")

plt.xlabel("Year")

plt.ylabel("Sales Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "car_charts/car_sales_by_year.png"
)

plt.close()

# ============================================================
# 14. FUEL TYPE CHART
# ============================================================

plt.figure(figsize=(7, 5))

plt.bar(
    fuel_analysis["Fuel_Type"],
    fuel_analysis["Sales_Count"]
)

plt.title("Sales by Fuel Type")

plt.xlabel("Fuel Type")

plt.ylabel("Sales Count")

plt.tight_layout()

plt.savefig(
    "car_charts/sales_by_fuel_type.png"
)

plt.close()

# ============================================================
# 15. CREATE EXCEL FILE
# ============================================================

excel_file = "Car_Sales_Price_Analysis_400.xlsx"

with pd.ExcelWriter(
    excel_file,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Car_Data_400",
        index=False
    )

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    brand_sales.to_excel(
        writer,
        sheet_name="Brand_Sales",
        index=False
    )

    brand_price.to_excel(
        writer,
        sheet_name="Brand_Price",
        index=False
    )

    fuel_analysis.to_excel(
        writer,
        sheet_name="Fuel_Analysis",
        index=False
    )

    year_sales.to_excel(
        writer,
        sheet_name="Year_Sales",
        index=False
    )

    city_sales.to_excel(
        writer,
        sheet_name="City_Sales",
        index=False
    )

# ============================================================
# 16. FINAL OUTPUT
# ============================================================

print("=" * 60)

print("       CAR SALES AND PRICE ANALYSIS")

print("=" * 60)

print()

print("Total Cars        :", total_cars)

print("Average Price     :", round(average_price, 2))

print("Minimum Price     :", minimum_price)

print("Maximum Price     :", maximum_price)

print("Average Kilometers:", round(average_km, 2))

print(
    "Most Sold Brand   :",
    brand_sales.iloc[0]["Brand"]
)

print()

print("Excel file created successfully!")

print(
    "File:",
    excel_file
)

print()

print(
    "Charts saved in 'car_charts' folder."
)

print()

print("PROJECT COMPLETED SUCCESSFULLY!")

print("=" * 60)