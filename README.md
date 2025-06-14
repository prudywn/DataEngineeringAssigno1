# DataEngineeringAssigno1
-- i)What is the total amount of debt owed by all countries in the dataset?
select sum(debt) as total_debt 
from international_debt_with_missing_values idwmv;
-- total debt = 2823894597632

-- ii)How many distinct countries are recorded in the dataset?
select count(distinct country_name) 
from international_debt_with_missing_values idwmv;
-- answer = 124 since one country had an empty string as its name and code

-- iii)What are the distinct types of debt indicators, and what do they represent?
select distinct idwmv.indicator_code  
from international_debt_with_missing_values idwmv;
-- answer = 
DT.DIS.MLAT.CD - Disbursements on external debt, multilateral (current US$)
DT.DIS.PROP.CD - Disbursements on external debt, private nonguaranteed (current US$)
DT.AMT.PCBK.CD - Principal repayments on external debt, private creditors (current US$)
DT.INT.PCBK.CD - Interest payments on external debt, private creditors (current US$)
DT.DIS.PCBK.CD - Disbursements on external debt, private creditors (current US$)
DT.INT.DLXF.CD - Interest payments on external debt, long-term + IMF (current US$)
DT.AMT.PBND.CD - Principal repayments on external debt, private bonds (current US$)
DT.AMT.OFFT.CD - Principal repayments on external debt, official creditors (current US$)
DT.INT.BLAT.CD - Interest payments on external debt, bilateral (current US$)
DT.AMT.BLAT.CD - Principal repayments on external debt, bilateral (current US$)
DT.DIS.DLXF.CD - Disbursements on external debt, long-term + IMF (current US$)
DT.INT.PRVT.CD - Interest payments on external debt, private nonguaranteed (current US$)
DT.AMT.DLXF.CD - Principal repayments on external debt, long-term + IMF (current US$)
DT.INT.OFFT.CD - Interest payments on external debt, official creditors (current US$)
DT.AMT.PRVT.CD - Principal repayments on external debt, private nonguaranteed (current US$)
DT.INT.DPNG.CD - Interest payments on external debt, private nonguaranteed (current US$)
DT.INT.MLAT.CD - Interest payments on external debt, multilateral (current US$)
DT.AMT.PROP.CD - Principal repayments on external debt, private nonguaranteed (current US$)
DT.INT.PROP.CD - Interest payments on external debt, private nonguaranteed (current US$)
DT.AMT.MLAT.CD - Principal repayments on external debt, multilateral (current US$)
The key abbreviations are:

AMT = Principal repayments (amount)
INT = Interest payments
DIS = Disbursements
MLAT = Multilateral creditors
BLAT = Bilateral creditors
PCBK/PRVT/PROP = Private creditors/nonguaranteed
OFFT = Official creditors
DLXF = Long-term debt + IMF
PBND = Private bonds

-- iv) Which country has the highest total debt, and how much does it owe?
select sum(debt) as total_debt, country_name 
from international_debt_with_missing_values idwmv
group by country_name 
having length(country_name)>0
order by total_debt  desc
limit 1; 
-- answer = 266455760896	China

-- v) What is the average debt across different debt indicators?
select avg(debt) as avg_debt, indicator_name 
from international_debt_with_missing_values idwmv
group by indicator_name  
having length(indicator_name)>0
order by avg_debt desc; 
-- answer = 
6385102887.177184	Principal repayments on external debt, long-term (AMT, current US$)
5617528387.785466	Principal repayments on external debt, private nonguaranteed (PNG) (AMT, current US$)
1952507090.1727273	Disbursements on external debt, long-term (DIS, current US$)
1813818513.165587	PPG, private creditors (AMT, current US$)
1466122955.496287	Interest payments on external debt, long-term (INT, current US$)
1414863557.1479592	PPG, bonds (AMT, current US$)
1351457466.1052632	PPG, official creditors (DIS, current US$)
1274168401.2139423	PPG, official creditors (AMT, current US$)
1125436968.0428574	PPG, bilateral (DIS, current US$)
884860496.6477431	PPG, other private creditors (AMT, current US$)
838769987.1021506	PPG, multilateral (DIS, current US$)
834951106.7052951	PPG, bonds (INT, current US$)
805805043.9498488	PPG, commercial banks (AMT, current US$)
744083352.2397337	PPG, private creditors (INT, current US$)
717492052.7281746	Interest payments on external debt, private nonguaranteed (PNG) (INT, current US$)
597027169.620087	PPG, bilateral (AMT, current US$)
547859195.5535715	PPG, multilateral (AMT, current US$)
321224580.57375	PPG, official creditors (INT, current US$)
303359589.2244318	PPG, private creditors (DIS, current US$)
271701783.9847561	PPG, commercial banks (DIS, current US$)
177040112.0222447	PPG, commercial banks (INT, current US$)
134041574.36760753	PPG, bilateral (INT, current US$)
131281505.21572581	PPG, multilateral (INT, current US$)
92727243.40364583	PPG, other private creditors (DIS, current US$)
5691548.604166667	PPG, other private creditors (INT, current US$)

-- vi) Which country has made the highest amount of principal repayments?
select country_name, sum(debt) as total_principal_repayments
from international_debt_with_missing_values idwmv
where indicator_code like 'DT.AMT.%'
and debt is not null
group by country_name
having length(country_name)>0
order by total_principal_repayments desc
limit 1; 
-- answer == China	194126905344

-- vii) What is the most common debt indicator across all countries?
select indicator_name, count(indicator_name) 
as common_debt_indicator
from international_debt_with_missing_values idwmv 
group by idwmv.indicator_name 
having length(indicator_name)>0
order by common_debt_indicator desc
limit 1;
-- answer == PPG, official creditors (INT, current US$) =>	116

 -- viii) Identify any other key debt trends and summarize your findings.
 The country with the highest debt is actually unnamed with a debt of = 275179339776	

 -- Identifed the countries that are having the most gain in the debt service
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
 answer == China	total_principal=>194126905344	total_interest=>37412380672	total_debt_service=>231539277824
 
