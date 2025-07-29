# Snowflake Data Warehouse: Setup, Querying Process, and Results

## 1. Creating the Database, Schema, and Tables in Snowflake

Follow these steps to set up your data warehouse structure in Snowflake:

### Step 1: Create a Database

In the Snowflake UI worksheet, run:

```sql
CREATE DATABASE retail_data;
```

### Step 2: Add a Schema

You can add a schema using the UI (+Schema) or with SQL:

```sql
USE DATABASE retail_data;
CREATE SCHEMA analytics;
```

### Step 3: Create Tables in the Schema

Switch to your schema and run the following SQL statements to create all required tables:

```sql
USE SCHEMA retail_data.analytics;

CREATE TABLE DIM_PRODUCTS(
    Product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    Category VARCHAR(100),
    Brand VARCHAR(100),
    price FLOAT
);

CREATE TABLE DIM_CUSTOMERS(
    Customer_id INT PRIMARY KEY,
    Full_name VARCHAR(100),
    Gender VARCHAR(100),
    age INT,
    location VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE DIM_STORES(
    Store_id INT PRIMARY KEY,
    Store_name VARCHAR(100),
    City VARCHAR(100),
    region VARCHAR(100),
    Store_type VARCHAR(100)
);

CREATE TABLE DIM_EMPLOYEES(
    Employee_id INT PRIMARY KEY,
    Ful_name VARCHAR(100),
    position VARCHAR(100),
    Hire_date DATE,
    Employee_store_id INT,
    FOREIGN KEY (Employee_store_id) REFERENCES DIM_STORES(Store_id)
);

CREATE TABLE DIM_TIME(
    Date_id INT PRIMARY KEY,
    Date DATE,
    Month INT,
    Quarter INT,
    year INT,
    Day_of_the_week VARCHAR
);

CREATE TABLE Fact_sales(
    Transactional_id INT PRIMARY KEY,
    Date_id INT,
    Product_id INT,
    Store_id INT,
    Customer_id INT,
    Quantity_sold INT,
    Price FLOAT,
    FOREIGN KEY (Date_id) REFERENCES DIM_TIME(Date_id),
    FOREIGN KEY(Product_id) REFERENCES DIM_PRODUCTS(Product_id),
    FOREIGN KEY(Customer_id) REFERENCES DIM_CUSTOMERS(Customer_id),
    FOREIGN KEY(Store_id) REFERENCES DIM_STORES(Store_id)
);

CREATE TABLE fact_inventory(
    Movement_id INT PRIMARY KEY,
    date_id INT,
    product_id INT,
    Store_id INT,
    Movement_type VARCHAR,
    Quantity_change VARCHAR,
    FOREIGN KEY (date_id) REFERENCES DIM_TIME(Date_id),
    FOREIGN KEY(Product_id) REFERENCES DIM_PRODUCTS(Product_id),
    FOREIGN KEY(Store_id) REFERENCES DIM_STORES(Store_id)
);

CREATE TABLE fact_customer_interaction(
    Interaction_id INT,
    Date_id INT,
    Product_id INT,
    Store_id INT,
    Customer_id INT,
    Employee_id INT,
    Interaction_type VARCHAR,
    Feedback_score INT,
    FOREIGN KEY (date_id) REFERENCES DIM_TIME(Date_id),
    FOREIGN KEY(Product_id) REFERENCES DIM_PRODUCTS(Product_id),
    FOREIGN KEY(Store_id) REFERENCES DIM_STORES(Store_id)
);
```

### Step 4: Load Data into Each Table

After creating the tables, load your data into each specific table using the `COPY INTO` command or the Snowflake UI data loading wizard. Ensure your data files match the table structures.

---

## Querying Process and Results

# Snowflake Data Warehouse: Querying Process and Results

This folder documents the process of running analytical SQL queries in Snowflake and provides the results for each question.

## Overview

- The file `inventory.sql` contains six SQL queries, each addressing a specific business question.
- The output (results) of each query has been saved here.

## Process

1. **Write SQL Queries:**
   - All queries are in `inventory.sql`.
2. **Run Queries in Snowflake:**
   - Open a worksheet in the Snowflake UI.
   - Copy and execute each query from `inventory.sql`.
3. **Export Results:**
   - After running each query, export the result as a CSV file.
   - Save each result as `q1.csv`, `q2.csv`, ..., `q6.csv` corresponding to the question number.

## Answers to Each Question

Below are the answers (CSV contents) for each question:

### 1. What are the top 5 best-selling products by quantity sold?

```
PRODUCT_NAME   TOTAL_SOLD
Product_2           16
Product_6            9
Product_10           8
Product_3            7
Product_1            7
Product_9            6
Product_5            5
Product_7            2
```

### 2. Which store generated the highest total revenue in the last 10 days?

```
STORE_NAME   TOTAL_REVENUE
Store_2            6200.55
```

### 3. What is the net inventory movement (IN - OUT) for each product?

```
PRODUCT_NAME   NET_MOVEMENT
Product_10           21
Product_1            13
Product_7             3
Product_3             0
Product_2            -4
Product_9            -9
Product_6           -13
Product_5           -19
```

### 4. On which day of the week do customer interactions occur most frequently?

```
DAY_OF_THE_WEEK   TOTAL_DAYS
Saturday                4
```

### 5. What is the average customer feedback score per store?

```
STORE_NAME   AVG_SCORE
Store_1         5.000000
Store_4         4.000000
Store_5         3.500000
Store_3         2.750000
Store_2         1.500000
```

### 6. What is the trend of daily sales revenue over the past 10 days?

```
DATE_ID   DAILY_REVENUE
5         4710.92
6         3534.65
7         2876.53
3         2356.40
1         2145.85
2         1693.58
8         1406.71
10         604.54
```

## Summary

- To reproduce, run the queries in `inventory.sql` and export the results as shown above.
