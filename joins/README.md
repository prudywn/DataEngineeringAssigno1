--1. Inner Join:
--List all patients with their associated hospital 
--names.
select pd.first_name, pd.last_name, hospital_name
from patient_data pd 
inner join health_care_data hcd 
on pd.patient_id = hcd.hospital_id;

--2. Left Join:
--Display all hospitals and any patients admitted to 
--them (if any), 
--showing patient first name and last name.
select hcd.hospital_name, first_name, last_name
from health_care_data hcd 
left join patient_data pd 
on hcd.hospital_id = pd.patient_id

--3. Right Join:
--Show all patients, along with the hospital name
-- they were admitted to. 
--Include even those without hospital details in
select first_name, last_name, hcd.hospital_name
from health_care_data hcd  
right join patient_data pd 
on hcd.hospital_id =pd.patient_id;

--4. Full Outer Join:
--Get a list of all patients and hospitals, 
--even if a hospital has no patients or a patient 
--has no hospital.
select pd.first_name, pd.last_name, hospital_name
from patient_data pd 
full outer join health_care_data hcd 
on pd.patient_id = hcd.hospital_id;

--5. Self Join:
--Find patients in the same hospital 
--(match on hospital_id) but with different names. 
--Return their patient IDs and first names.
select p1.patient_id as patient1_id, p1.first_name as patient1_name,
p2.patient_id as patient2_id, 
p2.first_name as patient2_name,
p1.hospital_id
from patient_data p1
join patient_data p2
on p1.hospital_id = p2.hospital_id
and p1.first_name <> p2.first_name
and p1.patient_id <> p2.patient_id;

--6. Inner Join with Filter:
--Find all female patients along with the job title of
--staff at their hospital
select p.gender , h.hospital_name, h.job_title, p.first_name, p.last_name
from health_care_data h 
inner join patient_data p on h.hospital_id = p.patient_id
where p.gender = 'Female';

--7. Left Join with Aggregation:
--For each hospital, count the number of patients admitted 
--to it. Show hospital name and total number of patients.
select h.hospital_name, count(p.patient_id) 
as all_patients
from patient_data p  
left join health_care_data h 
on p.patient_id = h.hospital_id
group by h.hospital_name
order by all_patients desc;
