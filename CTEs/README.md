# Common Table Expressions (CTEs) in Healthcare Data Analysis

This folder demonstrates the use of SQL Common Table Expressions (CTEs) to analyze healthcare and patient data. Each example below includes a description of the analytical goal, the CTE logic, and the final query.

---

## 1. Find the Youngest Patient(s) in Each Hospital

**Goal:**  
Identify the youngest patient(s) in every hospital.

**Approach:**

- Use a CTE to calculate the minimum age per hospital.
- Join this result with patient details to list all patients matching the minimum age in their hospital.

**SQL:**

```sql
WITH MinAgePerHospital AS (
  SELECT hospital_name, MIN(age) AS min_age
  FROM health_care_data hcd
  INNER JOIN patient_data pd ON hcd.hospital_id = pd.patient_id
  GROUP BY hospital_name
),
YoungestPatient AS (
  SELECT hcd.hospital_name, pd.first_name, pd.last_name, pd.age
  FROM health_care_data hcd
  INNER JOIN patient_data pd ON hcd.hospital_id = pd.hospital_id
  INNER JOIN MinAgePerHospital mph
    ON hcd.hospital_name = mph.hospital_name AND pd.age = mph.min_age
)
SELECT * FROM YoungestPatient;
```

---

## 2. Count Gender Distribution per Hospital

**Goal:**  
Count the number of male and female patients in each hospital.

**Approach:**

- Use a CTE to aggregate gender counts per hospital.

**SQL:**

```sql
WITH GenderDistribution AS (
  SELECT h.hospital_name,
         SUM(CASE WHEN p.gender = 'Female' THEN 1 ELSE 0 END) AS total_females,
         SUM(CASE WHEN p.gender = 'Male' THEN 1 ELSE 0 END) AS total_males
  FROM patient_data p
  JOIN health_care_data h ON p.patient_id = h.hospital_id
  GROUP BY h.hospital_name
)
SELECT * FROM GenderDistribution;
```

---

## 3. List Hospitals with More Than 5 Patients

**Goal:**  
Identify hospitals that have more than five patients.

**Approach:**

- Use a CTE to count patients per hospital.
- Filter for hospitals with more than five patients.

**SQL:**

```sql
WITH PatientsPerHospital AS (
  SELECT COUNT(p.patient_id) AS total_patients, h.hospital_name
  FROM patient_data p
  JOIN health_care_data h ON p.patient_id = h.hospital_id
  GROUP BY h.hospital_name
)
SELECT * FROM PatientsPerHospital
WHERE total_patients > 5;
```

---

## 4. Analyze Gender Match Between Staff and Patients

**Goal:**  
Find out how many patients share the same gender as hospital staff at their hospital.

**Approach:**

- Use a CTE to join staff and patient data by hospital.
- Count patients whose gender matches the staff gender.

**SQL:**

```sql
WITH GenderMatch AS (
  SELECT h.hospital_name, h.gender AS staff_gender,
         p.gender AS patient_gender, p.first_name, p.last_name
  FROM health_care_data h
  JOIN patient_data p ON h.hospital_id = p.hospital_id
)
SELECT hospital_name, COUNT(*) AS same_gender_patient_count
FROM GenderMatch
WHERE staff_gender = patient_gender
GROUP BY hospital_name;
```

---

**How to Use:**

- Copy and run each query in your SQL environment.
- Replace table and column names as needed to match your schema.
