🚲 **Public Bicycle Rental System - README** 🚲

## Project Overview
📝 This project aims to predict the total count of bicycles rented during each hour for a public bicycle rental system. The provided dataset contains hourly rental data spanning two years, and the task is to make predictions for the test set using only information available prior to the rental period. The data consists of various features such as season, weather conditions, temperature, and more. We'll use the LightGBM Regressor model for accurate predictions.

## Data Files
📊 The project includes the following data files:
- `train.csv`: This file contains the training data, which includes the first 19 days of each month.
- `test.csv`: This file contains the testing data, covering the 20th to the end of each month.
- `sample_submission.csv`: This file is a sample submission format for the predictions we'll make.

## Data Fields
📋 The dataset contains the following data fields:

- `datetime`: The hourly date and timestamp for each rental record.
- `season`: The season in which the rental occurred (encoded as 1 = spring, 2 = summer, 3 = fall, and 4 = winter).
- `holiday`: Binary indicator for whether the day is considered a holiday (1) or not (0).
- `workingday`: Binary indicator for whether the day is neither a weekend nor a holiday (1) or not (0).
- `weather`: Categorical variable representing different weather conditions.
- `temp`: Temperature in Celsius at the time of the rental.
- `atemp`: "Feels like" temperature in Celsius at the time of the rental.
- `humidity`: Relative humidity at the time of the rental.
- `windspeed`: Wind speed at the time of the rental.
- `casual`: Number of non-registered user rentals initiated.
- `registered`: Number of registered user rentals initiated.
- `count`: Total number of rentals (casual + registered) for each hour (target variable).

## Approach

### 1. Data Exploration and Preprocessing
🔍 We'll begin by exploring the data to gain insights and handle any missing or inconsistent values. Additionally, we'll convert categorical features into numerical representations for our models.

```python
# Load the training and testing data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Data preprocessing steps...
```

### 2. Feature Selection and Engineering
🔍 We'll select relevant features and create new ones if needed to improve our model's performance.

```python
# Feature selection and engineering...
```

### 3. Model Training and Comparisons
⚙️ We'll train multiple regression models using the training data and compare their performances. The models considered are Decision Tree Regressor, XGBoost Regressor, and LightGBM Regressor.

```python
# Model training and comparisons...

from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

# Decision Tree Regressor
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, Y_train)

# XGBoost Regressor
xgb_model = XGBRegressor()
xgb_model.fit(X_train, Y_train)

# LightGBM Regressor
lgbm_model = LGBMRegressor()
lgbm_model.fit(X_train, Y_train)
```

### 4. Model Evaluation
📊 We'll evaluate the trained models using suitable metrics and validate their performance on the validation set.

```python
# Model evaluation...

from sklearn.metrics import mean_squared_error

# Model evaluation for Decision Tree Regressor
dt_predictions = dt_model.predict(X_validate)
dt_rmse = np.sqrt(mean_squared_error(Y_validate, dt_predictions))

# Model evaluation for XGBoost Regressor
xgb_predictions = xgb_model.predict(X_validate)
xgb_rmse = np.sqrt(mean_squared_error(Y_validate, xgb_predictions))

# Model evaluation for LightGBM Regressor
lgbm_predictions = lgbm_model.predict(X_validate)
lgbm_rmse = np.sqrt(mean_squared_error(Y_validate, lgbm_predictions))
```

### 5. Making Predictions
🔮 After selecting the best-performing model (LightGBM Regressor), we'll use it to make predictions on the test set.

```python
# Make predictions...

predictions = lgbm_model.predict(X_test)
```

### 6. Submission
📑 Finally, we'll format the predictions according to the sample submission format and create the submission file.

```python
# Create submission...

submission = pd.DataFrame({
    'datetime': test['datetime'],
    'count': predictions
})
submission.to_csv('submission.csv', index=False)
```

## Model Selection: LightGBM Regressor
🚀 LightGBM Regressor is chosen over Decision Tree Regressor and XGBoost Regressor for the following reasons:

1. **Efficiency**: LightGBM is known for its efficiency in training and prediction. It is designed to be highly optimized and can handle large datasets much faster than traditional gradient boosting algorithms.

2. **Accuracy**: LightGBM often provides better accuracy compared to Decision Trees, especially when dealing with high-dimensional datasets and large sample sizes. It can capture complex interactions between features, leading to improved predictions.

3. **Handling Non-linearity**: LightGBM can naturally handle non-linear relationships between features and the target variable, which is important for modeling real-world phenomena like bike rentals.

4. **Regularization**: LightGBM has built-in support for L1 and L2 regularization, which helps prevent overfitting and enhances the model's generalization ability.

5. **Data Handling**: LightGBM can handle missing values and categorical features without the need for explicit preprocessing steps.

6. **Memory Efficiency**: LightGBM consumes less memory during training due to its leaf-wise tree growth strategy.

In this project, LightGBM Regressor is expected to provide accurate predictions and high efficiency, making it a suitable choice for the bicycle rental prediction task.

## Usage
💻 To run the project, make sure you have the required libraries installed. You can install them using `pip`:

```bash
pip install pandas scikit-learn xgboost lightgbm
```

## Google Collaboratory Link
🔗 To showcase the project and its execution, you can access the Google Colaboratory notebook using the following link:

Google Colab - Public Bicycle Rental System
(https://colab.research.google.com/drive/1eHO-B4Kkv0soiqua_4D9ov902oUFaFpA#scrollTo=DV_M2snLZDuo)

## Results
📈 The model's performance and predictions will be reflected in the submission file. We aim to achieve accurate predictions of bicycle rental counts using the LightGBM Regressor.

## Model Deployment and GUI Implementation
🚀 For model deployment, we used the `joblib` library to save and load the trained LightGBM Regressor model. After training the model, we saved it to a file using `joblib.dump()`. This allows us to reuse the trained model without retraining it every time the application runs.

In addition, we implemented a graphical user interface (GUI) using the `tkinter` library. The GUI allows users to input various features (season, holiday, weather, temperature, etc.) for a specific hour and get the predicted count of bicycles for that hour using the trained LightGBM Regressor model.

The GUI consists of text labels, entry fields, and a submit button. Users can enter values for each feature, and upon clicking the "Predict Count" button, the GUI sends the input values to the model, which then returns the predicted bicycle count. The output is displayed on the GUI.

## Contact Details
📬 Feel free to reach out to me via the following channels:

- **Email**: [mssannitya@gmail.com]
- **LinkedIn**: [https://www.linkedin.com/in/m-s-052080214/]

## Conclusion
🚴‍♂️ This project demonstrates how to build a predictive model for a public bicycle rental system using LightGBM Regressor. The usage of LightGBM Regressor ensures efficient and accurate predictions, making it a suitable choice for this task. The knowledge gained from this project can be applied to real-world bike rental systems for better resource management and customer satisfaction.

🚴 Happy biking and happy coding! 🚴
