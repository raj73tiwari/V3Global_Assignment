Data Analysis Web Application

This web application allows users to upload CSV files, perform basic data analysis, and visualize results. The application is built using Django and Matplotlib.


Installation

1. Clone the repository:
   git clone https://github.com/raj73tiwari/V3Global_Assignment.git

2. Install the required packages:
   pip install -r requirements.txt

4. Run the Django development server:
   python manage.py runserver

5. Access the application:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

Usage

1. Upload a CSV File:
   Choose a CSV file and click the "Analyze" button.

2. Results:
   After uploading, the application displays the first few rows of the data.
   Summary statistics are shown for numerical columns.
   Any missing values are highlighted.

3. Visualizations:
   Histograms for numerical columns are displayed on the results page.


Features

1. File Upload:
   Users can upload CSV files through a web interface.
   Only CSV files are allowed.

2. Data Analysis:
   The application reads the uploaded CSV file using pandas.
   Displays the first few rows of the data.
   Calculates summary statistics such as mean, median, and standard deviation for numerical columns.
   Identifies missing values.

3. Data Visualization:
   Generates histograms for numerical columns using Matplotlib.
   Displays the generated plots on the results page.


Technologies Used

1. Django
2. Pandas
3. Matplotlib
