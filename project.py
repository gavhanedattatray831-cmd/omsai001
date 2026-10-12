import pandas as pd
import random
import os
import matplotlib.pyplot as plt

# ============================================================
# LIBRARY MANAGEMENT AND ANALYSIS
# 300 DATA RECORDS
# ============================================================

random.seed(100)

TOTAL_RECORDS = 300

# ============================================================
# 1. BOOKS DATA
# ============================================================

book_names = [
    "Python Basics",
    "Data Science with Python",
    "Database Management",
    "Computer Networks",
    "Operating System",
    "Machine Learning",
    "Web Development",
    "C Programming",
    "Java Programming",
    "Artificial Intelligence"
]

categories = [
    "Programming",
    "Database",
    "Networking",
    "Computer",
    "AI",
    "Web"
]

authors = [
    "Mark Lutz",
    "Jake VanderPlas",
    "Raghu Ramakrishnan",
    "Andrew Tanenbaum",
    "Galvin",
    "Tom Mitchell",
    "Jon Duckett",
    "Dennis Ritchie",
    "Herbert Schildt",
    "Stuart Russell"
]

books = []

for i in range(1, TOTAL_RECORDS + 1):

    books.append([
        100 + i,
        random.choice(book_names),
        random.choice(categories),
        random.choice(authors),
        random.randint(2020, 2025),
        random.randint(1, 10)
    ])

books_df = pd.DataFrame(
    books,
    columns=[
        "Book_ID",
        "Book_Name",
        "Category",
        "Author",
        "Year",
        "Copies"
    ]
)

# ============================================================
# 2. STUDENTS DATA
# ============================================================

first_names = [
    "Rahul", "Amit", "Om", "Rohit", "Akash",
    "Sahil", "Aditya", "Vishal", "Pratik", "Kunal",
    "Sneha", "Pooja", "Priya", "Neha", "Riya"
]

last_names = [
    "Patil", "Shinde", "Jadhav", "Pawar",
    "Deshmukh", "More", "Gavhane", "Kadam",
    "Bhosale", "Chavan"
]

departments = [
    "Computer",
    "IT",
    "Mechanical",
    "Civil",
    "Electronics",
    "Commerce"
]

students = []

for i in range(1, TOTAL_RECORDS + 1):

    name = random.choice(first_names) + " " + random.choice(last_names)

    students.append([
        1000 + i,
        name,
        random.choice(departments),
        random.randint(18, 25),
        "student" + str(i) + "@gmail.com"
    ])

students_df = pd.DataFrame(
    students,
    columns=[
        "Student_ID",
        "Student_Name",
        "Department",
        "Age",
        "Email"
    ]
)

# ============================================================
# 3. ISSUE / RETURN / FINE DATA
# ============================================================

issue_data = []

for i in range(1, TOTAL_RECORDS + 1):

    issue_date = pd.Timestamp("2026-01-01") + pd.Timedelta(
        days=random.randint(0, 250)
    )

    return_date = issue_date + pd.Timedelta(
        days=random.randint(3, 20)
    )

    due_date = issue_date + pd.Timedelta(days=14)

    days_late = max(
        0,
        (return_date - due_date).days
    )

    fine = days_late * 5

    if days_late > 0:
        status = "Late"
    else:
        status = "Returned"

    issue_data.append([
        i,
        random.randint(101, 400),
        random.randint(1001, 1300),
        issue_date.date(),
        due_date.date(),
        return_date.date(),
        days_late,
        fine,
        status
    ])

issue_df = pd.DataFrame(
    issue_data,
    columns=[
        "Issue_ID",
        "Book_ID",
        "Student_ID",
        "Issue_Date",
        "Due_Date",
        "Return_Date",
        "Days_Late",
        "Fine",
        "Status"
    ]
)

# ============================================================
# 4. BASIC ANALYSIS
# ============================================================

total_books = len(books_df)

total_students = len(students_df)

total_issues = len(issue_df)

total_copies = books_df["Copies"].sum()

total_fine = issue_df["Fine"].sum()

average_fine = issue_df["Fine"].mean()

late_returns = len(
    issue_df[issue_df["Status"] == "Late"]
)

returned_books = len(
    issue_df[issue_df["Status"] == "Returned"]
)

most_common_category = (
    books_df["Category"]
    .value_counts()
    .idxmax()
)

most_common_department = (
    students_df["Department"]
    .value_counts()
    .idxmax()
)

# ============================================================
# 5. CATEGORY ANALYSIS
# ============================================================

category_analysis = (
    books_df
    .groupby("Category")
    .agg(
        Total_Books=("Book_ID", "count"),
        Total_Copies=("Copies", "sum")
    )
    .reset_index()
)

# ============================================================
# 6. DEPARTMENT ANALYSIS
# ============================================================

department_analysis = (
    students_df
    .groupby("Department")
    .agg(
        Total_Students=("Student_ID", "count")
    )
    .reset_index()
)

# ============================================================
# 7. STATUS ANALYSIS
# ============================================================

status_analysis = (
    issue_df
    .groupby("Status")
    .agg(
        Total_Records=("Issue_ID", "count"),
        Total_Fine=("Fine", "sum")
    )
    .reset_index()
)

# ============================================================
# 8. AUTHOR ANALYSIS
# ============================================================

author_analysis = (
    books_df["Author"]
    .value_counts()
    .reset_index()
)

author_analysis.columns = [
    "Author",
    "Book_Count"
]

# ============================================================
# 9. SUMMARY
# ============================================================

summary = pd.DataFrame({
    "Metric": [
        "Total Books",
        "Total Students",
        "Total Issues",
        "Total Copies",
        "Total Fine",
        "Average Fine",
        "Late Returns",
        "Returned Books",
        "Most Common Category",
        "Most Common Department"
    ],

    "Value": [
        total_books,
        total_students,
        total_issues,
        total_copies,
        total_fine,
        round(average_fine, 2),
        late_returns,
        returned_books,
        most_common_category,
        most_common_department
    ]
})

# ============================================================
# 10. CREATE CHART FOLDER
# ============================================================

os.makedirs("library_charts", exist_ok=True)

# ============================================================
# 11. CATEGORY CHART
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    category_analysis["Category"],
    category_analysis["Total_Books"]
)

plt.title("Books by Category")
plt.xlabel("Category")
plt.ylabel("Number of Books")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "library_charts/books_by_category.png"
)

plt.close()

# ============================================================
# 12. DEPARTMENT CHART
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    department_analysis["Department"],
    department_analysis["Total_Students"]
)

plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "library_charts/students_by_department.png"
)

plt.close()

# ============================================================
# 13. FINE CHART
# ============================================================

plt.figure(figsize=(7, 5))

plt.bar(
    status_analysis["Status"],
    status_analysis["Total_Fine"]
)

plt.title("Fine Analysis")
plt.xlabel("Status")
plt.ylabel("Total Fine")

plt.tight_layout()

plt.savefig(
    "library_charts/fine_analysis.png"
)

plt.close()

# ============================================================
# 14. AUTHOR CHART
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    author_analysis["Author"],
    author_analysis["Book_Count"]
)

plt.title("Books by Author")
plt.xlabel("Author")
plt.ylabel("Number of Books")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "library_charts/books_by_author.png"
)

plt.close()

# ============================================================
# 15. CREATE EXCEL FILE
# ============================================================

excel_file = "Library_Management_Analysis_300.xlsx"

with pd.ExcelWriter(
    excel_file,
    engine="openpyxl"
) as writer:

    books_df.to_excel(
        writer,
        sheet_name="Books_300",
        index=False
    )

    students_df.to_excel(
        writer,
        sheet_name="Students_300",
        index=False
    )

    issue_df.to_excel(
        writer,
        sheet_name="Issue_Return_Fine",
        index=False
    )

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    category_analysis.to_excel(
        writer,
        sheet_name="Category_Analysis",
        index=False
    )

    department_analysis.to_excel(
        writer,
        sheet_name="Department_Analysis",
        index=False
    )

    status_analysis.to_excel(
        writer,
        sheet_name="Status_Analysis",
        index=False
    )

    author_analysis.to_excel(
        writer,
        sheet_name="Author_Analysis",
        index=False
    )

# ============================================================
# 16. FINAL OUTPUT
# ============================================================

print("=" * 60)

print("       LIBRARY MANAGEMENT AND ANALYSIS")

print("=" * 60)

print()

print("Total Books       :", total_books)

print("Total Students    :", total_students)

print("Total Issues      :", total_issues)

print("Total Copies      :", total_copies)

print("Total Fine        :", total_fine)

print("Average Fine      :", round(average_fine, 2))

print("Late Returns      :", late_returns)

print("Returned Books    :", returned_books)

print("Most Common Category   :", most_common_category)

print("Most Common Department  :", most_common_department)

print()

print("Excel file created successfully!")

print("File :", excel_file)

print()

print("Charts saved in 'library_charts' folder.")

print()

print("PROJECT COMPLETED SUCCESSFULLY!")

print("=" * 60)