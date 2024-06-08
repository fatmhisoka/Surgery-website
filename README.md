# Surgical Department Database Application

## Overview
This database application manages the records and operations of a surgical department. It facilitates adding and deleting patients, surgeons, appointments, and operations while ensuring data integrity and consistency. The application also handles key error cases to maintain database integrity.

![Surgical Department Database](1.png)

## Features

### Patient Management
- **Add Patient:**
  - Attributes: patient_id, first_name, last_name, birth_date, gender, address, phone.
- **Delete Patient:**
  - Allows deletion of patient records based on patient_id.
- **View Patient Appointment:**
  - Allows viewing patient appointments based on patient_id.

![Patient Management](2.png)

### Surgeon Management
- **Add Surgeon:**
  - Attributes: surgeon_id, first_name, last_name, birth_date, gender, address, phone, email.
- **Delete Surgeon:**
  - Allows deletion of surgeon records based on surgeon_id.
- **View Surgeon Appointment:**
  - Allows viewing surgeon appointments based on surgeon_id.

### Appointment Management
- **Add Appointment:**
  - Attributes: appointment_id, patient_id, surgeon_id, operation_id, appointment_date, operationroom_id.
- **Delete Appointment:**
  - Allows deletion of appointment records based on appointment_id.

![Appointment Management](3.png)

### Operation Management
- **Add Operation:**
  - Attributes: operation_id, operation, description, cost.

![Operation Management](4.png)

## Error Handling
- **Unique IDs:**
  - Error message raised if duplicate patient, surgeon, or operation IDs are entered.
- **Appointment Conflicts:**
  - Error message raised if attempting to enter overlapping appointments for the same surgeon, patient, or operation room.
- **Foreign Key Integrity:**
  - Error message raised if attempting to enter an appointment with a non-existent surgeon_id, patient_id, operation_id, or operationroom_id.
- **Cascade Deletion of Appointments:**
  - Deleting an appointment for a surgeon will also delete the corresponding appointment for the patient and vice versa, ensuring appointment records integrity.

## Usage
Refer to the following SQL commands for database operations:

- **Adding a Patient:**
INSERT INTO patients (patient_id, first_name, last_name, birth_date, gender, address, phone) VALUES (...);
- **Deleting a Patient:**
DELETE FROM patients WHERE patient_id = ...;
- **Adding a Surgeon:**
INSERT INTO surgeons (surgeon_id, first_name, last_name, birth_date, gender, address, phone, email)
VALUES (...);
- **Deleting a Surgeon:**
DELETE FROM surgeons WHERE surgeon_id = ...;


## Conclusion
This application offers a robust solution for managing surgical department records and operations, maintaining data integrity, and effectively handling critical error cases.


