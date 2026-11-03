# 📊 Student Performance Prediction

An interactive Machine Learning application that predicts a student's expected examination score based on study habits, attendance, previous academic performance, and sleep hours.

Built using **Python, Scikit-learn, Pandas, and Streamlit**.

## 🚀 Project Overview

The Student Performance Prediction application uses a Machine Learning regression model to estimate a student's examination score based on four input parameters.

Users can enter their name, adjust the input values using interactive sliders, and generate a predicted examination score.

## ✨ Features

- **Study Hours:** Number of hours spent studying.
- **Attendance Percentage:** Student's attendance percentage.
- **Previous Score:** Score obtained in the previous examination.
- **Sleep Hours:** Average number of hours spent sleeping.
- **Interactive Interface:** User-friendly Streamlit interface with sliders.
- **Score Prediction:** Predicts the expected examination score using Linear Regression.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Dataset handling and manipulation |
| Scikit-learn | Machine Learning model |
| Linear Regression | Score prediction algorithm |
| Streamlit | Web application interface |

## 📂 Project Structure

```text
Streamlit/
│
├── app.py
├── examscore_predictor.py
├── student_performance.csv
├── requirements.txt
└── README.md
```

## 📁 Dataset Description

The project uses a synthetic student performance dataset containing 240 records.

| Feature | Description |
|---|---|
| study_hours | Daily study hours |
| attendance_percent | Attendance percentage |
| previous_score | Previous examination score |
| sleep_hours | Daily sleep duration |
| exam_score | Target variable to be predicted |

**Target Variable:** `exam_score`

## ⚙️ Machine Learning Workflow

1. Load the student performance dataset.
2. Separate input features and target variable.
3. Initialize the Linear Regression model.
4. Train the model using the dataset.
5. Collect user inputs through Streamlit sliders.
6. Pass the input features to the trained model.
7. Generate and display the predicted examination score.

## 💻 Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/tvnagasravani/GENAI.git
```

### 2. Navigate to the project folder

```bash
cd GENAI/Streamlit
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your default web browser.

## 📌 Future Improvements

- Implement train-test splitting.
- Evaluate model performance using MAE, MSE, RMSE, and R².
- Compare Linear Regression, Decision Tree, and Random Forest models.
- Improve the application with interactive data visualizations.

## 👩‍💻 Author

**T V Naga Sravani**

GitHub: [@tvnagasravani](https://github.com/tvnagasravani)

---

⭐ If you find this project interesting, feel free to explore the repository!
