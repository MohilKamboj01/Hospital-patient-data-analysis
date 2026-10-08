import pandas as pd
import matplotlib.pyplot as plt

# Sample hospital patient data
data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

    "Name": ["Aman", "Riya", "Rahul", "Simran", "Karan",
             "Neha", "Arjun", "Priya", "Rohit", "Anjali",
             "Vikas", "Sneha", "Manish", "Pooja", "Varun",
             "Kavya", "Amit", "Nisha", "Deepak", "Mehak"],

    "Age": [25, 45, 32, 67, 54, 29, 71, 38, 62, 24,
            48, 35, 59, 43, 76, 31, 52, 68, 27, 57],

    "Gender": ["Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female",
               "Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],

    "Disease": ["Diabetes", "Hypertension", "Fever", "Heart Disease",
                "Diabetes", "Asthma", "Heart Disease", "Fever",
                "Hypertension", "Diabetes", "Fever", "Asthma",
                "Diabetes", "Hypertension", "Heart Disease",
                "Fever", "Diabetes", "Asthma", "Hypertension",
                "Diabetes"],

    "Treatment": ["Medication", "Medication", "Medication", "Surgery",
                  "Medication", "Inhaler", "Surgery", "Medication",
                  "Medication", "Medication", "Medication", "Inhaler",
                  "Medication", "Medication", "Surgery", "Medication",
                  "Medication", "Inhaler", "Medication", "Medication"],

    "Treatment_Cost": [5000, 4500, 2000, 75000, 5500,
                       3500, 85000, 2500, 5000, 6000,
                       2200, 4000, 6500, 4800, 90000,
                       2800, 5200, 4500, 3500, 5800],

    "Hospital_Days": [3, 4, 2, 12, 5, 3, 15, 2, 5, 4,
                      2, 3, 6, 4, 16, 2, 5, 4, 3, 5]
}

# Create DataFrame
df = pd.DataFrame(data)


# Function to display patient data
def show_patients():
    print("\n========== PATIENT RECORDS ==========")
    print(df.to_string(index=False))


# Function for general statistics
def patient_statistics():
    print("\n========== PATIENT STATISTICS ==========")
    print("Total Patients:", len(df))
    print("Average Age:", round(df["Age"].mean(), 2))
    print("Average Treatment Cost: ₹", round(df["Treatment_Cost"].mean(), 2))
    print("Average Hospital Stay:", round(df["Hospital_Days"].mean(), 2), "days")

    print("\nGender Distribution:")
    print(df["Gender"].value_counts())


# Function for age analysis
def age_analysis():
    print("\n========== AGE ANALYSIS ==========")

    def age_group(age):
        if age < 18:
            return "Child"
        elif age <= 35:
            return "Young Adult"
        elif age <= 60:
            return "Adult"
        else:
            return "Senior Citizen"

    df["Age_Group"] = df["Age"].apply(age_group)

    print(df["Age_Group"].value_counts())

    # Age group graph
    df["Age_Group"].value_counts().plot(
        kind="bar",
        title="Patients by Age Group",
        xlabel="Age Group",
        ylabel="Number of Patients"
    )

    plt.tight_layout()
    plt.show()


# Function for disease analysis
def disease_analysis():
    print("\n========== DISEASE ANALYSIS ==========")

    disease_count = df["Disease"].value_counts()

    print("\nNumber of patients by disease:")
    print(disease_count)

    print("\nMost common disease:", disease_count.idxmax())

    # Disease graph
    disease_count.plot(
        kind="bar",
        title="Disease-wise Patient Analysis",
        xlabel="Disease",
        ylabel="Number of Patients"
    )

    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()


# Function for treatment analysis
def treatment_analysis():
    print("\n========== TREATMENT ANALYSIS ==========")

    treatment_count = df["Treatment"].value_counts()

    print("\nTreatment patterns:")
    print(treatment_count)

    print("\nMost common treatment:", treatment_count.idxmax())

    # Treatment graph
    treatment_count.plot(
        kind="pie",
        autopct="%1.1f%%",
        title="Treatment Pattern"
    )

    plt.ylabel("")
    plt.show()


# Function for cost analysis
def cost_analysis():
    print("\n========== TREATMENT COST ANALYSIS ==========")

    print("Highest Treatment Cost: ₹", df["Treatment_Cost"].max())
    print("Lowest Treatment Cost: ₹", df["Treatment_Cost"].min())
    print("Average Treatment Cost: ₹", round(df["Treatment_Cost"].mean(), 2))

    expensive_patient = df.loc[df["Treatment_Cost"].idxmax()]

    print("\nPatient with highest treatment cost:")
    print("Patient ID:", expensive_patient["Patient_ID"])
    print("Name:", expensive_patient["Name"])
    print("Disease:", expensive_patient["Disease"])
    print("Treatment:", expensive_patient["Treatment"])
    print("Cost: ₹", expensive_patient["Treatment_Cost"])


# Function to search for a patient
def search_patient():
    patient_id = int(input("\nEnter Patient ID: "))

    patient = df[df["Patient_ID"] == patient_id]

    if patient.empty:
        print("Patient not found.")
    else:
        print("\nPatient Details:")
        print(patient.to_string(index=False))


# Main menu
while True:

    print("\n")
    print("==============================================")
    print("       HOSPITAL PATIENT DATA ANALYSIS")
    print("==============================================")
    print("1. View Patient Records")
    print("2. Patient Statistics")
    print("3. Age Analysis")
    print("4. Disease Analysis")
    print("5. Treatment Analysis")
    print("6. Treatment Cost Analysis")
    print("7. Search Patient")
    print("8. Exit")
    print("==============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_patients()

    elif choice == "2":
        patient_statistics()

    elif choice == "3":
        age_analysis()

    elif choice == "4":
        disease_analysis()

    elif choice == "5":
        treatment_analysis()

    elif choice == "6":
        cost_analysis()

    elif choice == "7":
        search_patient()

    elif choice == "8":
        print("\nThank you for using Hospital Patient Data Analysis.")
        break

    else:
        print("\nInvalid choice. Please try again.")