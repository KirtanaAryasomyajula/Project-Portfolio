1)  Medical Insurance Cost Analysis (Python-Linear Regression)

This project analyzes the Medical Insurance Cost Dataset with the aim to explore how variables like age, gender, BMI, smoking habits, number of children, and region affect medical charges. It includes data cleaning, visualization, transformation, and possibly predictive modeling.

Initial Exploration

• Dataset loaded using pandas and has 1338 records.

• No missing values.

• Removed duplicate entries to ensure data integrity.

Univariate Analysis:

Categorical Variables:

sex, smoker, region, children were analyzed using pie and bar plots.
Most individuals are non-smokers.
Gender is nearly balanced.
Southeast region has the highest representation.
Numerical Variables:

age, bmi, and charges distributions examined using histograms and box plots
Charges were right-skewed, hence log-transformed for normalization.
BMI outliers were handled using IQR-based filtering.
Bivariate Analysis

Smokers vs Non-Smokers:

Smokers pay significantly more in charges.
Smoking status shows a strong influence on medical cost.
Age vs Charges:

Charges increase with age.
Visualized using scatter plots colored by intensity of charges.
BMI Analysis:

Higher BMI correlates with higher charges, especially among smokers.
Age and BMI were also studied together.
Region & Gender:

Some demographic trends seen, but not as influential on charges.
Transformations and Feature Engineering

• Encoding categorical variables:sex,smoker and region using Label Encoding.

• Log transformation applied to charges to handle skewness.

• BMI outliers removed using IQR filtering.

• Data visualizations updated post-cleaning for better accuracy.

Modeling

• Splitting into train and test datasets.

• Regression modeling (Linear Regression)

• Accuracy Score (80%) and Evaluation metrics: MSE

Interpretation

Smoker: Smokers pay drastically more, health risk indicator.
Age: Older individuals incur more charges.
BMI: High BMI(especially for smokers) linked to more cost due to potential health issues.
Children: No strong link found with medical cost.
Region: Region does not significantly affect cost.
Sex:Gender doesn't heavily impact charges.

2)  DRUG TYPE CLASSIFICATION


The aim of the project is to  classify which type of drug should be prescribed to a patient based on various medical features such as age, sex, blood pressure (BP), cholesterol level, and sodium-to-potassium ratio (Na_to_K).

2. Data Understanding:
•	Dataset: drug200.csv with 200 records.
•	Features:
o	Age: Numeric
o	Sex: Categorical
o	BP (Blood Pressure): Categorical (Low/Normal/High)
o	Cholesterol: Categorical (Normal/High)
o	Na_to_K (Sodium to Potassium ratio): Numeric
o	Drug: Target variable (categorical with 5 drug classes)

3. Exploratory Data Analysis (EDA):
•	Visualizations:
o	Count plots to show the distribution of drug types across sex, BP, and cholesterol.
o	Scatter plots to analyze how features like Age and Na_to_K vary with Drug.
o	Pie charts to show the proportion of different categories.
•	Outlier Detection:
o	Na_to_K variable was examined using box plots and filtered using the IQR method to remove outliers.

4. Data Preprocessing:
•	Encoding:
o	Label Encoding for Sex, BP, and Cholesterol.
•	Feature Scaling:
o	Standardization applied to all numerical features using StandardScaler.
•	Target-Feature Split:
o	Target: Drug
o	Features: Remaining columns after encoding and scaling.

5. Modeling:
•	Algorithms Used:
o	Logistic Regression
o	Decision Tree Classifier
•	Evaluation:
o	Models were evaluated using accuracy and confusion matrix.
o	The Decision Tree model likely provided better performance on this multiclass classification task due to its handling of categorical splits.

6. Conclusion:
   
•	The project successfully demonstrated the application of classification algorithms to a real-world medical dataset.

•	With proper data preprocessing and feature engineering, both Logistic Regression and Decision Tree models could predict drug types with reasonable accuracy.

•	This pipeline can serve as a foundation for more advanced modeling or for deployment in healthcare-related decision support systems.

   










