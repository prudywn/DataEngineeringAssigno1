select * from international_debt_with_missing_values idwmv;

-- What is the total amount of debt owed by all countries in the dataset?
select sum(debt) as total_debt 
from international_debt_with_missing_values idwmv;

-- How many distinct countries are recorded in the dataset?
select count(distinct country_name) 
from international_debt_with_missing_values idwmv;

-- What are the distinct types of debt indicators, and what do they represent?
select distinct idwmv.indicator_code  
from international_debt_with_missing_values idwmv;

-- Which country has the highest total debt, and how much does it owe?
select sum(debt) as total_debt, country_name 
from international_debt_with_missing_values idwmv
group by country_name 
having length(country_name)>0
order by total_debt  desc
limit 1; 

-- What is the average debt across different debt indicators?
select avg(debt) as avg_debt, indicator_name 
from international_debt_with_missing_values idwmv
group by indicator_name  
having length(indicator_name)>0
order by avg_debt desc; 

-- Which country has made the highest amount of principal repayments?
select country_name, sum(debt) as total_principal_repayments
from international_debt_with_missing_values idwmv
where indicator_code like 'DT.AMT.%'
and debt is not null
group by country_name
having length(country_name)>0
order by total_principal_repayments desc
limit 1;

-- What is the most common debt indicator across all countries?
select indicator_name, count(indicator_name) 
as common_debt_indicator
from international_debt_with_missing_values idwmv 
group by idwmv.indicator_name 
having length(indicator_name)>0
order by common_debt_indicator desc
limit 1;

--Identify any other key debt trends and summarize your findings.
select sum(debt) as total_debt, country_name 
from international_debt_with_missing_values idwmv
group by country_name 
order by total_debt  desc
limit 1;

-- Debt service patterns
with debt_service_analysis as (
select country_name,
sum(case when indicator_code like 'DT.AMT.%' then debt else 0 end)
as total_principal_payments,
sum(case when indicator_code like 'DT.INT.%' then debt else 0 end)
as total_interest_payments,
sum(case when indicator_code like 'DT.AMT.%' 
or indicator_code like 'DT.INT.%' then debt else 0 end) as total_debt_service
from international_debt_with_missing_values idwmv 
where debt is not null 
group by country_name
order by total_debt_service desc 
limit 1)
select * from debt_service_analysis;

