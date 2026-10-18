
"""
Student Performance Analytics System
Uses Python, NumPy, and Pandas.
"""

import numpy as np
import pandas as pd


DATA_FILE = "students.csv"

SUBJECTS = ["Math", "Python", "Statistics", "Database", "English"]

PASS_MARK = 40


def load_data(file_path):
    """Load and validate the student dataset."""
    df = pd.read_csv(file_path)

    required_columns = [
        "Student_ID", "Name", "Department",
        *SUBJECTS, "Attendance"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("The student dataset is empty.")

    if df["Student_ID"].isna().any():
        raise ValueError("Student IDs cannot be missing.")

    if df["Student_ID"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

    if df[["Name", "Department"]].isna().any().any():
        raise ValueError("Student names and departments are required.")

    numeric_columns = SUBJECTS + ["Attendance"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="raise")

        if df[column].isna().any():
            raise ValueError(f"Missing values in {column}.")

        if not df[column].between(0, 100).all():
            raise ValueError(
                f"{column} must contain values from 0 to 100."
            )

    return df


def calculate_total(marks):
    """Calculate total marks across all subjects."""
    return np.sum(marks)


def calculate_average(marks):
    """Calculate average marks across all subjects."""
    return np.mean(marks)


def assign_grade(average):
    """Assign a grade based on the student's average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= PASS_MARK:
        return "E"
    else:
        return "F"


def determine_result(marks):
    """Pass only if every subject mark is at least 40."""
    for mark in marks:
        if mark < PASS_MARK:
            return "Fail"
    return "Pass"


def process_students(df):
    """Calculate each student's performance."""
    results = df.copy()

    totals = []
    averages = []
    grades = []
    statuses = []

    for _, student in results.iterrows():
        marks = student[SUBJECTS].to_numpy(dtype=float)

        total = calculate_total(marks)
        average = calculate_average(marks)
        grade = assign_grade(average)
        status = determine_result(marks)

        totals.append(total)
        averages.append(average)
        grades.append(grade)
        statuses.append(status)

    results["Total_Marks"] = totals
    results["Average_Marks"] = np.round(averages, 2)
    results["Grade"] = grades
    results["Result"] = statuses

    return results


def show_basic_information(df):
    """Display dataset information."""
    print("\n" + "=" * 65)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)

    print(f"\nTotal students: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    print("\nDataset columns:")
    print(list(df.columns))

    print("\nDataset information:")
    df.info()

    print("\nMissing values by column:")
    print(df.isnull().sum())

    print("\nAll student records:")
    print(df.to_string(index=False))


def show_student_results(results):
    """Display totals, averages, grades, and pass/fail status."""
    columns = [
        "Student_ID", "Name", "Total_Marks",
        "Average_Marks", "Grade", "Result"
    ]

    print("\n" + "=" * 65)
    print("INDIVIDUAL STUDENT RESULTS")
    print("=" * 65)

    print(results[columns].to_string(index=False))


def show_overall_statistics(results):
    """Display highest, lowest, and average performance."""
    averages = results["Average_Marks"]

    highest = averages.max()
    lowest = averages.min()
    class_average = np.mean(averages)

    print("\n" + "=" * 65)
    print("OVERALL PERFORMANCE STATISTICS")
    print("=" * 65)

    print(f"Highest student average: {highest:.2f}")
    print(f"Lowest student average: {lowest:.2f}")
    print(f"Overall class average: {class_average:.2f}")

    highest_students = results[averages == highest]
    lowest_students = results[averages == lowest]

    print("\nHighest-performing student(s):")
    print(
        highest_students[
            ["Student_ID", "Name", "Average_Marks"]
        ].to_string(index=False)
    )

    print("\nLowest-performing student(s):")
    print(
        lowest_students[
            ["Student_ID", "Name", "Average_Marks"]
        ].to_string(index=False)
    )


def show_pass_fail_statistics(results):
    """Display pass/fail counts and percentages."""
    pass_count = (results["Result"] == "Pass").sum()
    fail_count = (results["Result"] == "Fail").sum()
    total = len(results)

    print("\n" + "=" * 65)
    print("PASS/FAIL STATISTICS")
    print("=" * 65)

    print(f"Students passed: {pass_count}")
    print(f"Students failed: {fail_count}")
    print(f"Pass percentage: {pass_count / total * 100:.2f}%")
    print(f"Fail percentage: {fail_count / total * 100:.2f}%")


def show_grade_distribution(results):
    """Display the number of students in each grade."""
    print("\n" + "=" * 65)
    print("GRADE DISTRIBUTION")
    print("=" * 65)

    grade_order = ["A", "B", "C", "D", "E", "F"]
    distribution = results["Grade"].value_counts()

    for grade in grade_order:
        print(f"Grade {grade}: {distribution.get(grade, 0)} student(s)")


def show_subject_analysis(results):
    """Compare average marks across subjects."""
    subject_averages = results[SUBJECTS].mean()

    print("\n" + "=" * 65)
    print("SUBJECT-WISE PERFORMANCE")
    print("=" * 65)

    for subject, average in subject_averages.items():
        print(f"{subject}: average = {average:.2f}")

    best_subject = subject_averages.idxmax()
    weakest_subject = subject_averages.idxmin()

    print(f"\nBest-performing subject: {best_subject}")
    print(f"Lowest-performing subject: {weakest_subject}")


def show_top_performers(results, count=3):
    """Display the top students by average marks."""
    top_students = results.nlargest(count, "Average_Marks")
    cutoff = top_students["Average_Marks"].min()

    # Include all students tied at the cutoff.
    top_students = results[
        results["Average_Marks"] >= cutoff
    ].sort_values(
        by=["Average_Marks", "Student_ID"],
        ascending=[False, True]
    )

    print("\n" + "=" * 65)
    print(f"TOP PERFORMERS (TOP {count}, INCLUDING TIES)")
    print("=" * 65)

    print(
        top_students[
            ["Student_ID", "Name", "Department",
             "Average_Marks", "Grade"]
        ].to_string(index=False)
    )


def show_attendance_analysis(results):
    """Display attendance statistics."""
    attendance = results["Attendance"]

    print("\n" + "=" * 65)
    print("ATTENDANCE ANALYSIS")
    print("=" * 65)

    print(f"Average attendance: {attendance.mean():.2f}%")
    print(f"Highest attendance: {attendance.max():.2f}%")
    print(f"Lowest attendance: {attendance.min():.2f}%")

    low_attendance = results[results["Attendance"] < 75]

    print("\nStudents with attendance below 75%:")
    if low_attendance.empty:
        print("No students found.")
    else:
        print(
            low_attendance[
                ["Student_ID", "Name", "Attendance"]
            ].to_string(index=False)
        )


def main():
    """Run the complete student performance analysis."""
    try:
        df = load_data(DATA_FILE)
        show_basic_information(df)

        results = process_students(df)

        show_student_results(results)
        show_overall_statistics(results)
        show_pass_fail_statistics(results)
        show_grade_distribution(results)
        show_subject_analysis(results)
        show_top_performers(results)
        show_attendance_analysis(results)

        # Save the analyzed data for review.
        results.to_csv("student_analysis_results.csv", index=False)

        print("\nAnalysis completed successfully.")
        print("Results saved to student_analysis_results.csv")

    except FileNotFoundError:
        print(
            f"Error: '{DATA_FILE}' was not found. "
            "Keep it in the project folder."
        )
    except (ValueError, KeyError) as error:
        print(f"Data validation error: {error}")


if __name__ == "__main__":
    main()
