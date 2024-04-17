# Ironhack Final Project

## Overview

This project aims to predict the cost per goal for advertising campaigns based on various input parameters such as vertical, advertiser country, and advertising platform ID.

## Data Source

The dataset used in this project was based on data from an online advertising platform, but none of the values are real In order to maintain data confidentiality.


## Tools and Libraries

- Python: Programming language used for data analysis and manipulation.
- Pandas: Library used for data manipulation and analysis with DataFrame structures.
- Matplotlib: Library used for creating plots and visualizations.
- Seaborn: Library used for creating attractive and informative statistical graphics.
- NumPy: Library used for numerical computations and data manipulation with arrays.
- SciPy: Library used for scientific computing and advanced mathematics.
- Scikit-learn (sklearn): Library used for machine learning algorithms and tools.
- Joblib: Library used for lightweight pipelining in Python.
- XGBoost: Library used for gradient boosting algorithms.
- Regular Expressions (re): Used for pattern matching and text processing.
- DateTime: Library used for manipulating dates and times.

## Project Structure

- `Final Project.ipynb`: Jupyter Notebook containing the main code.
- `README.md`: This file providing an overview of the project.
- `data`: Directory containing the dataset used for analysis.
- `slides`: Project presentation

## Analysis Steps

1. **Data Loading and Preprocessing:** The dataset is loaded into a DataFrame and cleaned as needed.
2. **Exploratory Data Analysis (EDA):** Basic statistics and visualizations are used to understand the dataset's structure and distributions.
3. **Feature Engineering:** Additional features are created or extracted from existing ones to facilitate analysis.
4. **Visualization:** Various plots and graphs are generated to visualize trends, distributions, and relationships within the data.
5. **Insights and Interpretation:** The findings from the analysis are summarized, and conclusions are drawn based on the observed patterns.
6. **Hypothesis Testing:** Statistical tests are performed to validate hypotheses or make inferences about the population based on sample data.
7. **Machine Learning Model Testing:** Various machine learning algorithms are trained and tested on the data to predict outcomes or uncover patterns. Model performance metrics are evaluated to select the best-performing model.

## Results and Findings

- The database must be divided into Clicks and Leads, otherwise the standard deviation is too high and the number of outliers will jeopardize the ML Model.
- The best criteria to use in the machine learning model to predict CPG are countries, verticals and platforms. These are the ones that have shown the highest correlation.
- Adding more fields to the ML Model will make it more complete and reduce the margin for error. The ideal Model will be when it is possible to consider all the keywords for each country, city, platform and vertical. Each campaign can contain 30, 40, 50 or more keywords. 


## Conclusion

This project provides a comprehensive analysis of the behavior of cost per goal in online campaigns and how certain factors influence this metric, offering valuable insights that allow you to build a machine learning model that helps predict the cost_per_goal of a campaign.

## Future Work

- Incorporate additional datasets and metrics to enrich the analysis and the machine learning model.

## Author

Élio Vieira
