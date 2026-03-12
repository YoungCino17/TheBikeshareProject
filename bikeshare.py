import time
import pandas as pd
import numpy as np

CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

def get_user_input(prompt, options):
    """Universal helper to handle user input and validation."""
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(options)}")

def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data!')
    
    city = get_user_input(
        "Choose a city (Chicago, New York City, Washington): ", 
        list(CITY_DATA.keys())
    )
    
    month = get_user_input(
        "Filter by month (all, january, february, march, april, may, june): ",
        ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    )
    
    day = get_user_input(
        "Filter by day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ",
        ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    )

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # Convert to datetime once
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract components
    df['month_name'] = df['Start Time'].dt.month_name().str.lower()
    df['day_name'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Apply filters
    if month != 'all':
        df = df[df['month_name'] == month]
    
    if day != 'all':
        df = df[df['day_name'] == day]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    print(f"Most Common Month:    {df['month_name'].mode()[0].title()}")
    print(f"Most Common Day:      {df['day_name'].mode()[0].title()}")
    print(f"Most Common Hour:     {df['hour'].mode()[0]}")

    print(f"\nCalculation took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    print(f"Start Station: {df['Start Station'].mode()[0]}")
    print(f"End Station:   {df['End Station'].mode()[0]}")

    # Find most frequent combo without creating a permanent column
    popular_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f"Common Trip:   {popular_trip}")

    print(f"\nCalculation took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...')
    start_time = time.time()

    total_sec = df['Trip Duration'].sum()
    mean_sec = df['Trip Duration'].mean()

    print(f"Total Travel Time:   {total_sec:,.2f} seconds ({total_sec/3600:.2f} hours)")
    print(f"Average Travel Time: {mean_sec:,.2f} seconds ({mean_sec/60:.2f} minutes)")

    print(f"\nCalculation took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...')
    start_time = time.time()

    # Generic check for columns to avoid KeyErrors
    if 'User Type' in df:
        print(f"User Types:\n{df['User Type'].value_counts().to_string()}\n")
    
    if 'Gender' in df:
        print(f"Gender Counts:\n{df['Gender'].value_counts().to_string()}\n")

    if 'Birth Year' in df:
        print(f"Birth Year Stats:")
        print(f"  Earliest: {int(df['Birth Year'].min())}")
        print(f"  Recent:   {int(df['Birth Year'].max())}")
        print(f"  Common:   {int(df['Birth Year'].mode()[0])}")

    print(f"\nCalculation took {time.time() - start_time:.4f} seconds.")
    print('-'*40)

def display_raw_data(df):
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of raw trip data? (yes/no): ').lower()
        if view_data != 'yes':
            break
        
        print(df.iloc[start_loc : start_loc + 5])
        start_loc += 5
        
        if start_loc >= len(df):
            print("End of data reached.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("No data found for those filters. Please try again.")
            continue

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        if input('\nWould you like to restart? (yes/no): ').lower() != 'yes':
            break

if __name__ == "__main__":
    main()
