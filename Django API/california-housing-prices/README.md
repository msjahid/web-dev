# California Housing Prices Prediction

![Cover Image](https://github.com/msjahid/california-housing-prices/assets/12425488/f1c03818-54a7-4968-a75d-0a8ec7c9d136)

A RESTful API for predicting median house prices for California districts using machine learning.

## About the Project

This project provides a RESTful API for predicting median house prices for various California districts based on historical data and machine learning techniques. It serves as an educational project to explore and apply machine learning concepts and is built using Django REST framework.

### Dataset

The dataset used in this project is derived from the 1990 California census. It contains information about houses in California districts, including features such as housing median age, total rooms, total bedrooms, population, households, median income, and ocean proximity. The target variable is the median house value. The dataset is an excellent choice for learning machine learning and data preprocessing.

#### Dataset Columns

The dataset contains the following columns:

- `longitude`
- `latitude`
- `housing_median_age`
- `total_rooms`
- `total_bedrooms`
- `population`
- `households`
- `median_income`
- `median_house_value`
- `ocean_proximity`

#### Dataset Preview

Here's a preview of the dataset:

| longitude | latitude | housing_median_age | total_rooms | total_bedrooms | population | households | median_income | ocean_proximity | median_house_value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -122.23 | 37.88 | 41 | 880 | 129 | 322 | 126 | 8.3252 | NEAR BAY | 452600 |
| -122.22 | 37.86 | 21 | 7099 | 1106 | 2401 | 1138 | 8.3014 | NEAR BAY | 358500 |
| -122.24 | 37.85 | 52 | 1467 | 190 | 496 | 177 | 7.2574 | NEAR BAY | 352100 |
| -122.25 | 37.85 | 52 | 1274 | 235 | 558 | 219 | 5.6431 | NEAR BAY | 341300 |
| -122.25 | 37.85 | 52 | 1627 | 280 | 565 | 259 | 3.8462 | NEAR BAY | 342200 |
| -122.25 | 37.85 | 52 | 919 | 213 | 413 | 193 | 4.0368 | NEAR BAY | 269700 |
| -122.25 | 37.84 | 52 | 2535 | 489 | 1094 | 514 | 3.6591 | NEAR BAY | 299200 |
| -122.25 | 37.84 | 52 | 3104 | 687 | 1157 | 647 | 3.12 | NEAR BAY | 241400 |
| -122.26 | 37.84 | 42 | 2555 | 665 | 1206 | 595 | 2.0804 | NEAR BAY | 226700 |

## Installation

To run this project locally, you can follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/msjahid/california-housing-api.git

2. Navigate to the project directory.

    ```bash
    cd california-housing-api

3. Create a virtual environment (optional but recommended).

   ```bash
   python -m venv venv

4. Activate the virtual environment.
 - **On Windows:**

   ```bash
   venv\Scripts\activate
   ```
- **On macOS and Linux:**

   ```bash
   source venv/bin/activate

5. Install project dependencies.

   ```bash
   pip install -r requirements.txt
   
6. Unzip the machine learning model:

   ```bash
   unzip ml_model/model.zip


7. Run the Application 

   ```bash
   python manage.py runserver

### API Endpoints
#### The API provides the following endpoints:

- <b>`POST /api/predict/`:</b> Predict median house prices by sending a POST request with relevant data.
### Usage
1. Visit the local server using your web browser or a tool like Postman.

   ```bash
   http://localhost:8000/
   ```
   
2. Use the API endpoint to predict house prices based on various features.

3. Try different features and machine learning algorithms to improve prediction accuracy.

### Contributing
Contributions to this project are welcome! You can contribute by:

- Reporting issues
- Contributing to code
- Providing feedback and suggestions

### Author
Md Jahid Hasan

### License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file for details.

### Acknowledgments
- The California housing dataset used in this project is a modified version of the dataset available from [Kaggle's page](https://www.kaggle.com/datasets/shibumohapatra/house-price).
