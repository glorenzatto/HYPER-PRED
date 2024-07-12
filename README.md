# HYPER-PRED

## Features

- Load and preprocess data from an Excel file.
- Train a machine learning model (Random Forest) to predict hypertension risk.
- Evaluate the model's performance.
- Predict hypertension risk for given inputs (age, gender, race).
- Display the risk percentage and associated color coding.
- Visualize the risk level with a bar chart.

## Installation

### Prerequisites

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/glorenzatto/HYPER-PRED.git
   cd HYPER-PRED
   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Run the application:
   ```bash
   flask run
   
## Structure

- `static/python/hypertension_prediction.py`: Contains the main class with methods to load data, train the model, evaluate the model, predict risk, and determine risk color.

- `app.py`: Contains the Flask application code to handle web requests and render HTML templates.

- `templates/html`: Contains HTML templates for the web interface.

- `static/css/`: Contains CSS files for styling the web interface.

- `static/images/`: Contains the image files.

- `requirements.txt`: Contains the required packages.

- `input_dataset.xlsx`: Post-treatment dataset file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

