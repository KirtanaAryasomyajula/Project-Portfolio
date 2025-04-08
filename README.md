Data Analysis and Visualization (Power BI) -  Maven Analytics (Datasets from Maven)

Spotify Data Analysis (Power BI) - Maven Analytics 


Medical Insurance Cost Analysis (Python-Linear Regression)

  Project Summary
    Objective:
      To analyze a medical cost dataset (insurance.csv) and understand the relationship between medical insurance charges and other demographic and health-related 
      variables.
    Target Variable:
      charges (continuous): Represents the medical insurance cost charged to individuals.

    1.	Libraries Imported:
             numpy, pandas, matplotlib.pyplot,  seaborn and scikit learn for data  modeling .
    2.	Data Import and Exploration:
              Dataset is read using pandas.read_csv().
              Shape: 1338 rows (observations).
    3.	Variables in the Dataset:
             age: Age of primary beneficiary
             sex: Gender of the individual
             bmi: Body mass index
             children: Number of dependents
             smoker: Smoking status (yes/no)
             region: Residential region
             charges: Medical costs billed by health insurance
    4.	Initial Data Inspection:
 	           head(), info(), and shape of the dataset likely checked.
	           Distribution of numerical and categorical variables examined.
    5.	Visualization and EDA (Expected):
          	 Use of histograms, boxplots, scatter plots, and bar charts to understand variable relationships.
	    
    Smoker Effect:   Smokers typically incur much higher charges, which is a critical cost-driving factor.
   	Age & BMI:        Both show positive correlation with charges, indicating older individuals and those with higher BMI tend to have higher medical costs.
  	Children & Region: These might show less direct influence on charges but are still considered in the model. 
    Model Evaluation: Mean Squared Error  to assess prediction accuracy.








