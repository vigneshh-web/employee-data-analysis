Employee Data Analysis

Project Overview

This project analyses employee data to understand salary patterns, differences between departments, and the relationship between salary and work experience.

Dataset

Original dataset: employees_messy.csv

Cleaned dataset: clean_data.csv

Records after cleaning: 1,470 employees

Tools Used

Python

Pandas

Matplotlib

Jupyter Notebook

Data Cleaning

Removed duplicate records.

Handled missing values.

Standardised text values.

Corrected data types.

Detected and handled salary outliers using the IQR method.

Visualisations

Average Salary by Department

Distribution of Employee Salaries

Salary vs Experience

Average Salary by Experience

Salary Distribution by Department

Charts are saved in reports/figures/.

How to Run the Project

Install Python.

Install the required libraries:

python -m pip install pandas matplotlib jupyter nbconvert

Open the project folder in VS Code.

Open Task 4.ipynb in Jupyter Notebook.

Run the notebook cells from top to bottom.

Limitations

The analysis uses the available employee dataset. The results may not represent every organisation, and the charts show relationships rather than proving cause and effect.