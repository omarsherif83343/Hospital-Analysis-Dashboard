CREATE TABLE Patients (
    Patient_ID INT PRIMARY KEY,
    Patient_Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    City VARCHAR(50)
);

INSERT INTO Patients VALUES
(1,'Ahmed Ali',25,'Male','Cairo'),
(2,'Sara Mohamed',30,'Female','Alexandria'),
(3,'Omar Hassan',40,'Male','Giza'),
(4,'Mona Adel',35,'Female','Cairo'),
(5,'Youssef Samy',28,'Male','Mansoura'),
(6,'Nour Tarek',22,'Female','Alexandria'),
(7,'Khaled Fathy',45,'Male','Cairo'),
(8,'Aya Mostafa',32,'Female','Giza'),
(9,'Mahmoud Essam',27,'Male','Tanta'),
(10,'Fatma Ali',38,'Female','Cairo');

CREATE TABLE Doctors (
    Doctor_ID INT PRIMARY KEY,
    Doctor_Name VARCHAR(100),
    Department VARCHAR(50)
);

INSERT INTO Doctors VALUES
(1,'Dr. Ahmed','Cardiology'),
(2,'Dr. Sara','Neurology'),
(3,'Dr. Omar','Orthopedics'),
(4,'Dr. Mona','Pediatrics'),
(5,'Dr. Khaled','Dermatology');

CREATE TABLE Appointments (
    Appointment_ID INT PRIMARY KEY,
    Patient_ID INT,
    Doctor_ID INT,
    Appointment_Date DATE,
    Cost DECIMAL(10,2),
    FOREIGN KEY (Patient_ID) REFERENCES Patients(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctors(Doctor_ID)
);

INSERT INTO Appointments VALUES
(1,1,1,'2024-01-05',500),
(2,2,2,'2024-01-07',700),
(3,3,1,'2024-01-10',500),
(4,4,3,'2024-01-12',600),
(5,5,4,'2024-01-15',400),
(6,6,5,'2024-01-18',350),
(7,7,1,'2024-02-02',500),
(8,8,2,'2024-02-05',700),
(9,9,3,'2024-02-10',600),
(10,10,4,'2024-02-15',400),
(11,1,5,'2024-03-03',350),
(12,2,1,'2024-03-08',500),
(13,3,2,'2024-03-12',700),
(14,4,3,'2024-03-15',600),
(15,5,4,'2024-03-20',400);


select sum(cost) as total_revenues from Appointments;
select count(*) as count_of_patients from Patients;
select count(*) as count_of_doctors from Doctors;
select count(Appointment_Date) as count_of_date 
from Appointments;


select d.Doctor_Name,count(*) as Total_Appointments
from Doctors d inner join Appointments a
on d.Doctor_ID = a.Doctor_ID
group by d.Doctor_Name
order by Total_Appointments desc
limit 1;


select d.Department,count(*) as total_Appointments
from Doctors d inner join Appointments a
on d.Doctor_ID = a.Doctor_ID
group by d.Department
order by total_Appointments desc
limit 1;



select sum(A.cost) as total_cost,d.Department from 
Doctors d inner join Appointments a
on d.Doctor_ID = a.Doctor_ID group by d.Department; 

select count(*) as count_of_patients,City
from Patients group by City;

select avg(cost) as Average_Of_Cost from Appointments;

select max(cost) as Maximum_Cost from Appointments;