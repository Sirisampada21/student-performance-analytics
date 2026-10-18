# Student Performance Analytics System

## 1. Project Title and Student Details

Project Title: Student Performance Analytics System  
Student Name: Siri Sampada Eshwaroju 
Course: Python with AI  
Programming Language: Python 3.10  
Project Type: Data Analysis Project  

## 2. Objective

The objective of this project is to analyze student academic performance using Python, NumPy, and Pandas. The system processes student marks and attendance data to calculate total marks, average marks, grades, and pass/fail results. It also identifies top-performing students and analyzes subject-wise performance.

## 3. Technologies Used

- Python 3.10: Used to implement the program logic, functions, loops, and calculations.
- Pandas: Used to load, organize, process, and analyze student data using DataFrames.
- NumPy: Used for numerical calculations and statistical analysis.
- CSV: Used to store the student dataset.
- Visual Studio Code: Used to write, run, and test the program.

## 4. Dataset Description

The project uses a CSV dataset named `students.csv`, containing 20 student records.

The dataset includes the following nine columns:

| Column       |            Description             |
|--------------|------------------------------------|
| Student_ID   |       Unique student identifier    |
| Name         |            Student name            |
| Department   |         Student's department       |
| Math         |          Mathematics marks         |
| Python       |         Python subject marks       |
| Statistics   |          Statistics marks          |
| Database     |       Database subject marks       |
| English      |        English subject marks       |
| Attendance   |    Student attendance percentage   |

Marks and attendance values are represented on a scale of 0 to 100. The program validates the dataset before performing the analysis.

## 5. Implementation

The project is implemented using the following steps:

1.  Load the dataset: Pandas reads the `students.csv` file into a DataFrame.
2.  Validate the data: The program checks required columns, student IDs, missing values, and valid numerical ranges.
3.  Calculate total marks: A reusable function uses NumPy to calculate the total marks obtained by each student across five subjects.
4.  Calculate average marks: The program calculates each student's average marks.
5.  Assign grades: Grades are assigned according to the student's average marks.
6.  Determine results: A student passes only when their marks in every subject are at least 40.
7.  Analyze performance: The program calculates overall statistics, grade distribution, and pass/fail counts.
8.  Analyze subjects: It calculates average marks for each subject and identifies the highest- and lowest-performing subjects.
9.  Identify top performers: The program displays the three highest-performing students, including ties where applicable.
10. Analyze attendance: It displays attendance statistics and identifies students with attendance below 75%.
11. Export results: The processed data is saved to `student_analysis_results.csv`.

### Grading Criteria

| Average Marks | Grade |
|---------------|-------|
| 90–100        |   A   |
| 80–89.99      |   B   |
| 70–79.99      |   C   |
| 60–69.99      |   D   |
| 40–59.99      |   E   |
| Below 40      |   F   |

**Pass/Fail Rule:** A student passes if all five subject marks are 40 or above. If any subject mark is below 40, the result is Fail.

## 6. Key Features

- Reads student records from a CSV file.
- Uses a Pandas DataFrame to manage student data.
- Uses NumPy for numerical calculations.
- Calculates total and average marks for every student.
- Assigns grades based on average marks.
- Determines pass/fail results.
- Displays overall performance statistics.
- Calculates subject-wise average marks.
- Identifies the top-performing students.
- Analyzes student attendance.
- Validates input data and handles common errors.
- Exports the analyzed results to a new CSV file.

## 7. Output and Screenshots

The program displays student performance results, overall statistics, grade distribution, subject-wise analysis, top performers, and attendance information in the terminal.

The program also generates `student_analysis_results.csv`, which contains the original student information along with calculated total marks, average marks, grades, and results.

### Screenshots to Include

1. The project files in VS Code.
2. The terminal showing student performance results.
3. The terminal showing subject-wise analysis and top performers.
4. The terminal showing attendance analysis and successful completion.
5. The generated `student_analysis_results.csv` opened in VS Code or a spreadsheet application.

## 8. Final Outcome

The Student Performance Analytics System successfully processes the sample student dataset and produces useful academic performance information. It calculates student totals and averages, assigns grades, determines pass/fail status, analyzes subject performance and attendance, identifies top performers, and exports the results to a CSV file.

The project demonstrates the practical use of Python programming, functions, loops, NumPy, Pandas, and basic data analysis.

## 9. Challenges and Learning

During this project, the following concepts and skills were practiced:

- Creating and managing a structured CSV dataset.
- Loading and analyzing data with Pandas.
- Performing numerical calculations with NumPy.
- Writing reusable Python functions.
- Using loops to process student records.
- Applying conditions to assign grades and results.
- Validating data and handling errors.
- Exporting processed data to a CSV file.
- Testing program logic and checking the generated output.
- Organizing project files for GitHub submission.

## 10. GitHub Repository Link

GitHub Repository: [https://github.com/Sirisampada21/student-performance-analytics.git]
