
class Patient:
    def __init__(self, patient_id, name, age, gender, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.illness = illness

    def display_info(self):
        print("\n--- Patient Information ---")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Illness:", self.illness)


class PatientManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        patient_id = input("Enter Patient ID: ").strip()

        if not patient_id:
            print("Patient ID cannot be empty!")
            return

        if self.search_patient(patient_id, display=False):
            print("Patient ID already exists!")
            return

        name = input("Enter Patient Name: ").strip()

        if not name:
            print("Patient name cannot be empty!")
            return

        try:
            age = int(input("Enter Patient Age: "))

            if age < 0 or age > 130:
                print("Please enter a valid age between 0 and 130.")
                return

        except ValueError:
            print("Invalid age! Please enter a whole number.")
            return

        gender = input("Enter Patient Gender: ").strip()
        illness = input("Enter Patient Illness: ").strip()

        if not gender or not illness:
            print("Gender and illness cannot be empty!")
            return

        patient = Patient(
            patient_id, name, age, gender, illness
        )

        self.patients.append(patient)
        print("Patient registered successfully!")

    def view_patients(self):
        if not self.patients:
            print("No patient records found.")
            return

        print("\n===== ALL PATIENT RECORDS =====")

        for patient in self.patients:
            patient.display_info()

    def search_patient(self, patient_id, display=True):
        for patient in self.patients:
            if patient.patient_id == patient_id.strip():
                if display:
                    patient.display_info()
                return patient

        if display:
            print("Patient not found.")

        return None

    def delete_patient(self):
        patient_id = input("Enter Patient ID to delete: ").strip()

        patient = self.search_patient(
            patient_id, display=False
        )

        if patient:
            confirm = input(
                f"Delete record for {patient.name}? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                self.patients.remove(patient)
                print("Patient record deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Patient not found.")

    def menu(self):
        while True:
            print("\n===== PATIENT MANAGEMENT SYSTEM =====")
            print("1. Register Patient")
            print("2. View All Patients")
            print("3. Search Patient")
            print("4. Delete Patient")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_patient()

            elif choice == "2":
                self.view_patients()

            elif choice == "3":
                patient_id = input("Enter Patient ID: ").strip()
                self.search_patient(patient_id)

            elif choice == "4":
                self.delete_patient()

            elif choice == "5":
                print("Exiting Patient Management System.")
                break

            else:
                print("Invalid choice. Please try again.")


# Main program
if __name__ == "__main__":
    system = PatientManagementSystem()
    system.menu()
