# Accidents in Kenya - Road Accidents Fatality Prediction

![thika road road accidents](https://github.com/user-attachments/assets/1805f294-1858-45fc-8e24-0daf2505bead)


### Project Overview
This project analyzes road crashes in Kenya from 2012-2023 and builds a machine learning model to predict the likelihood of fatal outcomes in these crashes. By identifying high-risk factors and patterns, this model can support transportation agencies, public safety departments, and urban planners in developing interventions to reduce road fatalities.

### Main Objectives
- **Analyze historical crash data** to uncover patterns associated with fatal accidents.
- **Train a machine learning model** to predict the likelihood of fatalities in road crashes.
- **Deploy a web-based tool** for real-time fatality risk prediction, enabling users to enter crash details and receive a risk assessment.

### Specific Objectives
- Identify critical factors that influence fatality risks (e.g., location, time, weather).
- Provide insights to guide road safety campaigns, infrastructure improvements, and policy-making.

### Business Understanding
Road traffic accidents in Kenya contribute significantly to public health and safety challenges due to high fatality rates. Reducing these fatalities requires identifying factors that heighten death risks in crashes. This project leverages historical crash data to develop a model capable of estimating fatality probabilities, which can inform targeted safety measures.

### Data Understanding
The dataset used in this project includes crash data from Kenya (2012-2023) and is sourced from the **World Bank microdata platform**. Key features in the dataset:

- **Crash Date and Time**: Includes the time of day and date of each crash.
- **Location**: Geographic details like latitude, longitude, and road name.
- **Crash Description Keywords**: Descriptors indicating crash details, such as "fatality," "pedestrian," or "motorcycle."
- **Weather and Road Conditions**: Environmental context, including road wetness, fog, or traffic levels.
- **Crash Outcome**: Binary indicator marking whether the crash was fatal or non-fatal.

### Exploratory Data Analysis
- **Univariate Analysis**: Initial analysis of each feature to understand distributions.

![image](https://github.com/user-attachments/assets/25f4e17e-470c-428d-b330-97b79a90af2e)

- **Bivariate Analysis**: Feature coorelation Heatmap

![image](https://github.com/user-attachments/assets/7cc3d71d-6f31-4cc0-8c6b-92e4ff88c3e8)

- **Target Variable Analysis**: Investigating the proportion and characteristics of fatal vs. non-fatal crashes.
  
### Modeling Approach
- **Model Selection**: Machine learning algorithms such as Logistic Regression, Random Forest, and Decision Trees were tested.
- **Feature Engineering**: Created additional variables like time-of-day indicators and high-risk zone proximity.
- **Evaluation Metrics**: Model performance is evaluated using accuracy, precision, recall, and F1-score, with a particular focus on recall to ensure that fatal cases are accurately identified.

### Web-Based Deployment
The model is deployed in a web-based interface where users can:
- Input crash details and receive a real-time prediction on fatality risk.
- View relevant risk factors and suggestions for preventive actions.

### Results
- **Model Performance**: Details on model accuracy, precision, and recall scores.
- **Key Predictive Factors**: Insights into which factors most influence the likelihood of a fatal crash, such as crash location, weather conditions, and time of day.

### Real-World Context
Kenya has seen multiple tragic road incidents underscoring the need for enhanced road safety. Notable accident sites include:
- **Kiambu Road**: Frequent accidents, especially near Thindigua.
- **Nairobi Expressway**: Notable for high-speed incidents.
- **Londiani, Thika, and Voi Road Crashes**: Known areas with frequent fatalities, often due to high traffic and poor infrastructure.
  
  

### Future Improvements
- **Enhanced Feature Engineering**: Incorporating additional variables such as vehicle type or traffic density at crash sites.
- **Hyperparameter Tuning**: Further tuning of model parameters to improve predictive accuracy.
- **Real-Time Data Integration**: Potential for integrating real-time data sources, like live traffic or weather updates, to improve prediction accuracy.


