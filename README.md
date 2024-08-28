# E-Commerce Data Analysis Dashboard

## Overview

This project is designed for analysing e-commerce data. It provides insights into purchase frequency distribution by city and state, payment method trends over time, and payment method distribution. The dashboard visualises data using various plots.

## Features

- **Dashboard View**: Provides an overview of e-commerce data, including:
  - Top 10 cities and states by purchase frequency.
  - Payment method trends over time.
  - Payment method distribution as a chart.

- **Purchase Frequency Distribution**: 
  - Displays the top 10 cities and states by the number of orders.

- **Payment Method Trends**: 
  - Shows the most frequently used payment methods over time.
  - Provides a table of payment method distribution with percentages.
  - Includes a pie chart of payment method distribution.

## Try it

https://data-analysis-py-richardrflsn.streamlit.app/

## Installation

### Setup Environment - Anaconda
```
conda create --name main-ds python=3.11.9
conda activate main-ds
pip install -r requirements.txt
```
### Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
### Run streamlit app
```
cd dashboard
streamlit run dashboard.py
```

## Installation using github

### Setup
```
git clone https://github.com/Richardrflsn/Data-Analysis-Py.git
cd Data-Analysis-Py
```
### Create virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### Install the required packages
```
pip install -r requirements.txt
```
### Run streamlit app
```
cd dashboard
streamlit run dashboard.py
```
## Folder Structure
```
Data-Analysis-Py
├───dashboard
| ├───combined_data.csv
| └───dashboard.py
├───data
| ├───customer_dataset.csv
| └───geolocation_dataset.csv
| └───order_items_dataset.csv
| └──-order_payments_dataset.csv
| └───order_reviews_dataset.csv
| └───product_category_name_translation.csv
| └───products_dataset.csv
| └───sellers_dataset.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
