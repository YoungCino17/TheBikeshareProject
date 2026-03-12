# US Bikeshare Data Explorer

A CLI-based Python application that provides descriptive statistics for bikeshare data across three major US cities: **Chicago**, **New York City**, and **Washington**.

## 📊 Project Overview
This project analyzes data from Motivate, a bikeshare system provider. The script interacts with the user to provide a filtered view (by month and day) of trip patterns, station popularity, and user demographics.

## 🛠️ Requirements
*   **Python 3.x**
*   **Pandas**
*   **NumPy**

## 📂 Dataset Files
The script expects the following CSV files in the project root:
*   `chicago.csv`
*   `new_york_city.csv`
*   `washington.csv`

> **Note:** Data for Washington does not include 'Gender' or 'Birth Year' information.

## 🚀 How to Use
1.  **Clone the repository** and ensure the CSV data files are in the same folder.
2.  **Run the script** via terminal or alternatively upload on Jupyter Notebook to keep it simple:
    ```bash
    python bikeshare.py
    ```
3.  **Follow the prompts** to filter data:
    *   Choose a city (Chicago, New York City, Washington).
    *   Choose a month (January - June, or "all").
    *   Choose a day (Monday - Sunday, or "all").

## 📈 Statistics Calculated
The application provides the following insights:
*   **Time Stats:** Most frequent month, day of week, and start hour.
*   **Station Stats:** Most common start and end stations, and the most popular trip route.
*   **Trip Duration:** Total travel time and average trip duration.
*   **User Stats:** Counts of user types, gender distribution, and birth year statistics (where available).
*   **Raw Data:** Option to view the raw data 5 rows at a time.

## 📝 Functions Explained
*   `get_filters()`: Handles user input validation for city, month, and day.
*   `load_data()`: Loads and cleans the dataset based on selected filters.
*   `time_stats()`, `station_stats()`, `trip_duration_stats()`, and `user_stats()`: Logic for calculating specific metrics.
*   `display_raw_data()`: Interactive loop to browse the underlying CSV data.

## 👤 Author
**Mompoloki Radimo**

## 📝 License
This project is completed as part of a **Udacity** Data Science curriculum. All datasets and project rubrics are provided by Udacity.

---
