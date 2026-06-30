class Patient:

    def __init__(self, patient_id, name, age, gender, disease, doctor_name, room_number, blood_group):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.doctor_name = doctor_name
        self.room_number = room_number
        self.blood_group = blood_group

    def checkup(self):
        print(self.name, "is under checkup.")

    def admit(self):
        print(self.name, "has been admitted.")

    def discharge(self):
        print(self.name, "has been discharged.")

    def take_medicine(self):
        print(self.name, "is taking medicine.")

    def show_report(self):
        print("\n----- Patient Report -----")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Disease:", self.disease)
        print("Doctor Name:", self.doctor_name)
        print("Room Number:", self.room_number)
        print("Blood Group:", self.blood_group)

patient1 = Patient(101,"Anjali",20,"Female","Fever","Dr. Sharma",205,"O+")

patient1.show_report()
patient1.checkup()
patient1.admit()
patient1.take_medicine()
patient1.discharge()