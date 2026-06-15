import mysql.connector as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

conn = sql.connect(host="localhost",user="root",password="omarahmed123@",database="company")
mycursor = conn.cursor()

patients = "select * from patients"
doctors = "select * from doctors"
appointments = "select * from appointments"

mycursor.execute(patients)

patient_fetch = mycursor.fetchall()
column1 = [col[0] for col in mycursor.description]
patient_df = pd.DataFrame(patient_fetch,columns = column1)

mycursor.execute(doctors)
doctor_fetch = mycursor.fetchall()
column2 = [col[0] for col in mycursor.description]
doctor_df = pd.DataFrame(doctor_fetch,columns = column2)
mycursor.execute(appointments)
appointment_fetch = mycursor.fetchall()
column3 = [col[0] for col in mycursor.description]
appointment_df = pd.DataFrame(appointment_fetch,columns = column3)

print(patient_df.head())
print(doctor_df.head())
print(appointment_df.head())
print("-----------------------")
print(patient_df.info())
print(doctor_df.info())
print(appointment_df.info())
print("-----------------------")
print(patient_df.describe())
print(doctor_df.describe())
print(appointment_df.describe())
print("-----------------------")
print(patient_df.dtypes)
print(doctor_df.dtypes)
print(appointment_df.dtypes)
print("------------------------")
print(patient_df.empty)
print(doctor_df.empty)
print(appointment_df.empty)
print("------------------------")
print(patient_df.duplicated())
print(doctor_df.duplicated())
print(appointment_df.duplicated())
patient_df.drop_duplicates(inplace=True)
doctor_df.drop_duplicates(inplace=True)
appointment_df.drop_duplicates(inplace=True)
#---------------------------------------------
patient_df.dropna(inplace=True)
doctor_df.dropna(inplace=True)
appointment_df.dropna(inplace=True)
#--------------------------------------------
print(patient_df.dtypes.index)
print(doctor_df.dtypes.index)
print(appointment_df.dtypes.index)
#--------------------------------------------
appointment_df["Appointment_Date"] = pd.to_datetime(appointment_df["Appointment_Date"])
#--------------------------------------------
merge1 = pd.merge(appointment_df,doctor_df,on="Doctor_ID")
merge2 = pd.merge(merge1,patient_df,on="Patient_ID")
print(merge1)
print(merge2)
#---------------------------------------------
total_revenue = appointment_df["Cost"].sum()
total_patients = patient_df["Patient_ID"].count()
total_doctors = doctor_df["Doctor_ID"].count()
total_appointments = appointment_df["Appointment_ID"].count()
avg_appointment_cost = appointment_df["Cost"].mean()
max_appointment_cost = appointment_df["Cost"].max()
print("----------------------------------------")
print(total_revenue)
print(total_patients)
print(total_doctors)
print(total_appointments)
print(avg_appointment_cost)
print(max_appointment_cost)
#------------------------------------------------
#Department_Analysis
merge2["Cost"] = pd.to_numeric(merge2["Cost"])
count_of_date_by_dept = merge2.groupby("Department")["Appointment_Date"].count()
revenue_by_dept = merge2.groupby("Department")["Cost"].sum()
print(count_of_date_by_dept)
print(revenue_by_dept)
#------------------------------------------------
#Doctor_Analysis
count_of_date_by_doc = merge2.groupby("Doctor_Name")["Appointment_Date"].count()
revenue_by_doc = merge2.groupby("Doctor_Name")["Cost"].sum()
print(count_of_date_by_doc)
print(revenue_by_doc)
#-------------------------------------------------
#Patient_Analysis
patient_by_city = merge2.groupby("City")["Patient_ID"].count()
patient_by_gender = merge2.groupby("Gender")["Patient_ID"].count()
avg_patient_age = merge2["Age"].mean()
print(patient_by_city)
print(patient_by_gender)
print(avg_patient_age)
#--------------------------------------------------
#Time_Analysis
merge2["Appointment_Date"] = pd.to_datetime(merge2["Appointment_Date"])
merge2["Month"] = merge2["Appointment_Date"].dt.month
revenue_by_month = merge2.groupby("Month")["Cost"].sum()
appointment_by_month = merge2.groupby("Month")["Appointment_ID"].count()
print(revenue_by_month)
print(appointment_by_month)
#--------------------------------------------------
#Charts Analysis

plt.figure(figsize=(10,6))
revenue_by_dept.plot(kind="bar")
plt.title("Revenue by Department")
plt.xlabel("Department")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.show()

#---------------------------------------------------
plt.figure(figsize=(10,6))
appointments_by_doc = merge2.groupby("Doctor_Name")["Appointment_ID"].count()
appointments_by_doc.plot(kind="bar")
plt.title("Appointments by Doctor")
plt.xlabel("Doctors")
plt.ylabel("Appointments")
plt.xticks(rotation=0)
plt.show()
#---------------------------------------------------
plt.figure(figsize=(10,6))
patient_by_city.plot(kind="bar")
plt.title("Patients by City")
plt.xlabel("City")
plt.ylabel("Count Of Patients")
plt.xticks(rotation=0)
plt.show()
#-----------------------------------------------------
plt.figure(figsize=(10,6))
revenue_by_month.plot(kind="line")
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.show()
#-----------------------------------------------------
gender_by_patients = merge2.groupby("Gender")["Patient_ID"].nunique()
plt.figure(figsize=(10,6))
gender_by_patients.plot(kind="pie",labels=gender_by_patients.index,autopct="%1.1f%%")
plt.legend(title="Gender")
plt.title("Gender Distribution")
plt.show()
#------------------------------------------------------
age_by_patients = merge2.groupby("Age")["Patient_ID"].count()
plt.figure(figsize=(10,6))
plt.hist(merge2["Age"],bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show()