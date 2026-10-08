# Hospital Patient Data Analysis

A beginner-friendly Python mini project for analysing hospital patient data using **Pandas** and **Matplotlib**. The project analyses patient age, diseases, treatments, treatment costs, hospital stays, and provides simple visualizations.

## 📌 Project Overview

The **Hospital Patient Data Analysis** project demonstrates how Python can be used to organize and analyse hospital patient information.

The program uses a sample dataset containing **20 patient records** and provides a menu-driven interface for performing different types of analysis.

## 🎯 Objectives

- Store patient information using Pandas DataFrame.
- Calculate basic patient statistics.
- Analyse patient age groups.
- Find the most common diseases.
- Analyse treatment patterns.
- Analyse treatment costs.
- Analyse hospital stay duration.
- Search for a patient using Patient ID.
- Create charts using Matplotlib.

## 📊 Dataset

The dataset contains **20 hospital patient records** with the following fields:

| Column | Description |
|---|---|
| Patient_ID | Unique ID of the patient |
| Name | Patient name |
| Age | Patient age |
| Gender | Patient gender |
| Disease | Disease diagnosed |
| Treatment | Treatment provided |
| Treatment_Cost | Treatment cost in ₹ |
| Hospital_Days | Number of days spent in hospital |

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Matplotlib**

## 📦 Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install pandas matplotlib
```

Or install them from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/hospital-patient-data-analysis.git
```

Move into the project folder:

```bash
cd hospital-patient-data-analysis
```

Run the Python program:

```bash
python hospital_patient_analysis.py
```

## 📋 Menu Options

The program provides the following options:

```text
1. Show All Patients
2. Patient Statistics
3. Age Analysis
4. Disease Analysis
5. Treatment Analysis
6. Cost Analysis
7. Search Patient
8. Exit
```

## 📈 Analysis Performed

### Patient Statistics

The program calculates:

- Total number of patients
- Average age
- Median age
- Standard deviation of age
- Average treatment cost
- Average hospital stay
- Gender distribution

### Age Analysis

Patients are divided into:

- Child
- Young Adult
- Adult
- Senior Citizen

A bar chart is generated to show the number of patients in each age group.

### Disease Analysis

The program counts the number of patients suffering from each disease.

The sample dataset contains:

- Diabetes
- Hypertension
- Fever
- Asthma
- Heart Disease

A bar chart is generated to display disease frequency.

### Treatment Analysis

The program analyses different treatments:

- Medication
- Surgery
- Inhaler

A pie chart is generated to show the treatment distribution.

### Cost Analysis

The program identifies:

- Highest treatment cost
- Lowest treatment cost
- Average treatment cost by treatment type

## 🔍 Sample Findings

Some important findings from the sample dataset are:

- Total patients: **20**
- Average patient age: **46.95 years**
- Median patient age: **45.5 years**
- Average hospital stay: **5.2 days**
- Most common disease: **Diabetes**
- Most common treatment: **Medication**
- Highest treatment cost: **₹90,000**
- Lowest treatment cost: **₹2,000**
- Longest hospital stay: **16 days**

## 📁 Project Structure

```text
hospital-patient-data-analysis/
│
├── hospital_patient_analysis.py
├── requirements.txt
├── README.md
└── Hospital_Patient_Data_Analysis_Case_Study.docx
```

## 🚀 Future Scope

The project can be improved by:

- Adding a larger hospital dataset.
- Reading data from CSV or Excel files.
- Using NumPy for advanced numerical calculations.
- Using Seaborn for advanced visualizations.
- Adding correlation analysis.
- Creating an interactive dashboard.
- Adding machine learning for prediction of treatment cost or hospital stay.

## 🎓 Academic Information

**Project:** Hospital Patient Data Analysis  
**Course:** BCA – Data Science  
**University:** Chandigarh University  
**Type:** Python Mini Project

## 👨‍💻 Author

**Mohil**

BCA – Data Science  
Chandigarh University

## 📄 License

This project is created for educational and academic purposes.
