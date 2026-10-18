# Student Performance Analytics System

## 1. Project Overview

The Student Performance Analytics System is a Python-based data analysis project that processes student marks and attendance data. It calculates academic performance metrics and presents meaningful summaries to help understand student results.

## 2. Objective

The objective is to analyze student academic performance using Python, NumPy, and Pandas. The system calculates totals, averages, grades, pass/fail status, subject-wise averages, top performers, and attendance statistics.

## 3. Technologies Used

- Python 3.10
- NumPy
- Pandas
- CSV dataset
- Visual Studio Code

## 4. Dataset Description

The dataset is stored in `students.csv` and contains 20 student records.

Columns:
- Student_ID
- Name
- Department
- Math
- Python
- Statistics
- Database
- English
- Attendance

Each subject mark and attendance value is represented on a scale from 0 to 100.

## 5. Key Features

- Loads student data into a Pandas DataFrame.
- Validates required columns and numerical values.
- Calculates total and average marks.
- Assigns grades using defined grade boundaries.
- Determines pass/fail status based on individual subject marks.
- Calculates highest, lowest, and overall average performance.
- Displays grade distribution and pass/fail statistics.
- Performs subject-wise performance analysis.
- Identifies the top three performers, including ties.
- Analyzes attendance.
- Exports calculated results to `student_analysis_results.csv`.

## 6. Grading and Passing Rules

Grades are assigned based on average marks:

- A: 90 and above
- B: 80 to below 90
- C: 70 to below 80
- D: 60 to below 70
- E: 40 to below 60
- F: Below 40

A student passes only if they score at least 40 marks in every subject.

Students with attendance below 75% are listed separately for review. This is an attendance-reporting threshold, not an academic pass/fail condition.

## 7. How to Run the Project

1. Install Python 3.10.
2. Install the required libraries:

   `python -m pip install numpy pandas`

3. Keep `main.py` and `students.csv` in the same folder.
4. Run:

   `python main.py`

5. Review the analysis displayed in the terminal.
6. Open `student_analysis_results.csv` to view the calculated results.

## 8. Output

The program displays dataset information, individual student results, overall performance statistics, pass/fail statistics, grade distribution, subject-wise averages, top performers, and attendance analysis.

The calculated results are saved in `student_analysis_results.csv`.

## 9. Project Structure

- `main.py` — Main program and analysis functions.
- `students.csv` — Input dataset.
- `student_analysis_results.csv` — Generated analysis results.
- `README.md` — Project overview and instructions.
- `Project_Documentation.md` — Detailed project documentation.

## 10. Limitations

The project analyzes the supplied dataset. The results depend on the accuracy and completeness of the input records. The dataset contains sample student records for demonstration.

## 11. Author

Student Name: Siri Sampada Eshwaroju

Course: Python with AI

## 12. Repository

GitHub Repository: [https://github.com/Sirisampada21/student-performance-analytics.git](https://github.com/Sirisampada21/student-performance-analytics.git)
