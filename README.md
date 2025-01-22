Maven Analytics MTA Commuter Challenge - December 2024 Maven Challenge

About this project

1 .AIM: The COVID-19 pandemic caused a dramatic decline in public transport usage, prompting the need to evaluate recovery trends across MTA services. To find out the trends in the usage of public transport and other transits like individual and para transit , after covid-19 , in order to check whether the services provided at present by MTA are up to the mark or not , there is a strong need to analyze the data.


2.KEY INSIGHTS:

Public transport recovery lagged significantly,when compared to before pandemic as the average estimated ridership is in millions (buses and subways) and the number only decreased slowly after pandemic.

Transport through bridges and tunnels recovered quickly, stabilizing at 98.91% of pre-pandemic levels.

Access-A-Ride surpassed pre-pandemic ridership reaching at 60.73% highlighting the increased demand for paratransit services.

Factors such as remote work have heavily influenced recovery trends.

When seen day-wise , Wednesday was the day with highest ridership.

When seen month-wise , January is the month with highest ridership and October with lower ridership.

3.IMPACT: The Power BI dashboard provides transportation authorities and stakeholders with insights to build strategies for rebuilding ridership, and improving service efficiency post-pandemic.

4.METRICS USED IN PROJECT:

1. Total % Estimated Ridership

Definition: The percentage of passengers using transportation during the analyzed period (2020–2024).

Total % Estimated Ridership = (AVERAGEX(MTA_Daily_Ridership,MTA_Daily_Ridership[Subways: Total Estimated Ridership]+MTA_Daily_Ridership[Buses: Total Estimated Ridership]+MTA_Daily_Ridership[LIRR: Total Estimated Ridership]+MTA_Daily_Ridership[Metro-North: Total Estimated Ridership]+MTA_Daily_Ridership[Access-A-Ride: Total Scheduled Trips]+MTA_Daily_Ridership[Bridges and Tunnels: Total Traffic]+MTA_Daily_Ridership[Staten Island Railway: Total Estimated Ridership]))/100

2. Total % of Pre-Pandemic Ridership

Definition: The percentage of passengers who used public transportation before the COVID-19 pandemic, based on 2019 ridership levels.

Total % Pre-Pandemic Ridership = (AVERAGEX(MTA_Daily_Ridership,MTA_Daily_Ridership[Access-A-Ride: % of Comparable Pre-Pandemic Day]+MTA_Daily_Ridership[Bridges and Tunnels: % of Comparable Pre-Pandemic Day]+MTA_Daily_Ridership[Buses: % of Comparable Pre-Pandemic Day]+MTA_Daily_Ridership[LIRR: % of Comparable Pre-Pandemic Day]+MTA_Daily_Ridership[Metro-North: % of Comparable Pre-Pandemic Day]+MTA_Daily_Ridership[Staten Island Railway: % of Comparable Pre-Pandemic Day]+MTA_Daily_Ridership[Subways: % of Comparable Pre-Pandemic Day]))*100

3. Total % Recovery Ridership

Definition: The percentage of pre-pandemic ridership levels regained during the analyzed period.

Total % Recovery Ridership = DIVIDE([Total % of Pre-Pandemic Ridership],[Total % Est Public Ridership])*100

4. Average % Change of Ridership for all modes of transport

Definition: The average percentage change in ridership during the analyzed period compared to pre-pandemic levels.

Measures used:

Access-A-Ride: % Change = ((SUM(MTA_Daily_Ridership[Access-A-Ride: Total Scheduled Trips])- ((SUM(MTA_Daily_Ridership[Access-A-Ride: % of Comparable Pre-Pandemic Day]))100))/SUM(MTA_Daily_Ridership[Access-A-Ride: Total Scheduled Trips]))100

Bridges and Tunnels : %Change = ((SUM(MTA_Daily_Ridership[Bridges and Tunnels: Total Traffic])-(SUM(MTA_Daily_Ridership[Bridges and Tunnels: % of Comparable Pre-Pandemic Day])100))/SUM(MTA_Daily_Ridership[Bridges and Tunnels: Total Traffic]))100

Buses-% Change = ((SUM(MTA_Daily_Ridership[Buses: Total Estimated Ridership])-(SUM(MTA_Daily_Ridership[Buses: % of Comparable Pre-Pandemic Day]))100)/SUM(MTA_Daily_Ridership[Bridges and Tunnels: Total Traffic]))100

LIRR:% Change = ((SUM(MTA_Daily_Ridership[LIRR: Total Estimated Ridership])-(SUM(MTA_Daily_Ridership[LIRR: % of Comparable Pre-Pandemic Day]))100)/SUM(MTA_Daily_Ridership[LIRR: Total Estimated Ridership]))100

Metro North : % Change = ((SUM(MTA_Daily_Ridership[Metro-North: Total Estimated Ridership])-(SUM(MTA_Daily_Ridership[Metro-North: % of Comparable Pre-Pandemic Day]))100)/SUM(MTA_Daily_Ridership[Metro-North: Total Estimated Ridership]))100

Staten Island Railway : % Change = ((SUM(MTA_Daily_Ridership[Staten Island Railway: Total Estimated Ridership])-(SUM(MTA_Daily_Ridership[Staten Island Railway: % of Comparable Pre-Pandemic Day]))100)/SUM(MTA_Daily_Ridership[Staten Island Railway: Total Estimated Ridership]))100

Subway : % Change = ((SUM(MTA_Daily_Ridership[Subways: Total Estimated Ridership])-(SUM(MTA_Daily_Ridership[Subways: % of Comparable Pre-Pandemic Day]))100)/SUM(MTA_Daily_Ridership[Subways: Total Estimated Ridership]))100

These metrics together offer an overview of ridership trends, declines, and recovery over time.
