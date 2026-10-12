import random
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


TOTAL_RECORDS = 300


def build_library_data(total_records: int = TOTAL_RECORDS, seed: int = 100):
    """Create synthetic books, students, and issue/return datasets."""
    random.seed(seed)

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
        "Artificial Intelligence",
    ]

    categories = [
        "Programming",
        "Database",
        "Networking",
        "Computer",
        "AI",
        "Web",
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
        "Stuart Russell",
    ]

    first_names = [
        "Rahul", "Amit", "Om", "Rohit", "Akash",
        "Sahil", "Aditya", "Vishal", "Pratik", "Kunal",
        "Sneha", "Pooja", "Priya", "Neha", "Riya",
    ]

    last_names = [
        "Patil", "Shinde", "Jadhav", "Pawar",
        "Deshmukh", "More", "Gavhane", "Kadam",
        "Bhosale", "Chavan",
    ]

    departments = [
        "Computer",
        "IT",
        "Mechanical",
        "Civil",
        "Electronics",
        "Commerce",
    ]

    books = []
    for i in range(1, total_records + 1):
        books.append([
            100 + i,
            random.choice(book_names),
            random.choice(categories),
            random.choice(authors),
            random.randint(2020, 2025),
            random.randint(1, 10),
        ])

    books_df = pd.DataFrame(
        books,
        columns=["Book_ID", "Book_Name", "Category", "Author", "Year", "Copies"],
    )

    students = []
    for i in range(1, total_records + 1):
        name = random.choice(first_names) + " " + random.choice(last_names)
        students.append([
            1000 + i,
            name,
            random.choice(departments),
            random.randint(18, 25),
            f"student{i}@gmail.com",
        ])

    students_df = pd.DataFrame(
        students,
        columns=["Student_ID", "Student_Name", "Department", "Age", "Email"],
    )

    issue_data = []
    for i in range(1, total_records + 1):
        issue_date = pd.Timestamp("2026-01-01") + pd.Timedelta(days=random.randint(0, 250))
        return_date = issue_date + pd.Timedelta(days=random.randint(3, 20))
        due_date = issue_date + pd.Timedelta(days=14)
        days_late = max(0, (return_date - due_date).days)
        fine = days_late * 5
        status = "Late" if days_late > 0 else "Returned"

        issue_data.append([
            i,
            random.randint(101, 400),
            random.randint(1001, 1300),
            issue_date.date(),
            due_date.date(),
            return_date.date(),
            days_late,
            fine,
            status,
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
            "Status",
        ],
    )

    return books_df, students_df, issue_df


def summarize_library_data(books_df, students_df, issue_df):
    summary = {
        "total_books": len(books_df),
        "total_students": len(students_df),
        "total_issues": len(issue_df),
        "total_copies": int(books_df["Copies"].sum()),
        "total_fine": float(issue_df["Fine"].sum()),
        "average_fine": float(issue_df["Fine"].mean()),
        "late_returns": int((issue_df["Status"] == "Late").sum()),
        "returned_books": int((issue_df["Status"] == "Returned").sum()),
        "most_common_category": books_df["Category"].value_counts().idxmax(),
        "most_common_department": students_df["Department"].value_counts().idxmax(),
    }
    return summary


def analyze_book_popularity(books_df, issue_df):
    merged = issue_df.merge(books_df[["Book_ID", "Book_Name", "Category"]], on="Book_ID", how="left")
    popularity = (
        merged.groupby("Book_Name")
        .agg(issue_count=("Issue_ID", "count"), avg_fine=("Fine", "mean"))
        .sort_values(["issue_count", "avg_fine"], ascending=[False, False])
        .head(10)
    )
    return popularity


def analyze_student_fines(students_df, issue_df):
    combined = issue_df.merge(students_df[["Student_ID", "Department"]], on="Student_ID", how="left")
    department_fines = (
        combined.groupby("Department")["Fine"]
        .agg(["sum", "mean", "max"])
        .sort_values("sum", ascending=False)
    )
    return department_fines


def save_charts(books_df, students_df, issue_df, output_dir="."):
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    category_counts = books_df["Category"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    category_counts.plot(kind="bar", ax=ax, color="steelblue")
    ax.set_title("Books by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Count")
    plt.tight_layout()
    fig.savefig(out_dir / "books_by_category.png")
    plt.close(fig)

    department_counts = students_df["Department"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    department_counts.plot(kind="pie", ax=ax, autopct="%1.1f%%")
    ax.set_title("Students by Department")
    ax.set_ylabel("")
    plt.tight_layout()
    fig.savefig(out_dir / "students_by_department.png")
    plt.close(fig)

    late_status = issue_df["Status"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 5))
    late_status.plot(kind="bar", ax=ax, color=["forestgreen", "tomato"])
    ax.set_title("Issue Status")
    ax.set_xlabel("Status")
    ax.set_ylabel("Count")
    plt.tight_layout()
    fig.savefig(out_dir / "issue_status.png")
    plt.close(fig)

    return [
        str(out_dir / "books_by_category.png"),
        str(out_dir / "students_by_department.png"),
        str(out_dir / "issue_status.png"),
    ]


def print_summary(summary):
    print("\nLIBRARY MANAGEMENT SUMMARY")
    print("=" * 30)
    for key, value in summary.items():
        label = key.replace("_", " ").title()
        print(f"{label}: {value}")


def main():
    books_df, students_df, issue_df = build_library_data()
    summary = summarize_library_data(books_df, students_df, issue_df)
    print_summary(summary)

    top_books = analyze_book_popularity(books_df, issue_df)
    print("\nTOP 10 MOST ACTIVE BOOKS")
    print("=" * 30)
    print(top_books.head(10).to_string())

    student_fines = analyze_student_fines(students_df, issue_df)
    print("\nFINE SUMMARY BY DEPARTMENT")
    print("=" * 30)
    print(student_fines.to_string())

    chart_paths = save_charts(books_df, students_df, issue_df)
    print("\nCharts saved:")
    for path in chart_paths:
        print(f"- {path}")


if __name__ == "__main__":
    main()
