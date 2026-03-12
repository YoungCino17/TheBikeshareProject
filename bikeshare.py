import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Choose a city (Chicago, New York City, Washington): ").lower()
        if city in cities:
            break
        print("Oops! Please pick one of the three cities listed.")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Filter by month (all, january, february, ... , june): ").lower()
        if month in months:
            break
        print("Invalid month. Note: We only have data for January through June.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Filter by day (all, monday, tuesday, ... sunday): ").lower()
        if day in days:
            break
        print("That's not a day! Try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load city data from a file (e.g., a CSV file named after the city)
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime objects
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        df = df[df['Month'] == month.title()]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print('Most Common Day of Week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
     

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Create a new combination column
    df['Trip Route'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['Trip Route'].mode()[0]
    print('Most frequent combination of start station and end station trip:', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("Total Travel Time:", total_duration, "seconds")
    print("Total Travel Time (hours):", total_duration / 3600, "hours")

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print("Average Travel Time:", mean_duration, "seconds")
    print("Average Travel Time (minutes):", mean_duration / 60, "minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print('Counts of user types:\n', user_types)
    else:
        print('User type data not available.')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:\n', gender_counts)
    else:
        print('\nGender data not available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print('\nEarliest year of birth:', earliest)
        print('Most recent year of birth:', recent)
        print('Most common year of birth:', common)
    else:
        print('\nBirth year data not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Prompts the user to see raw data and displays 5 rows at a time.
    """
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    
    # Continue as long as user says 'yes'
    while view_data == 'yes':
        # Select 5 rows using iloc and print them
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        
        # Check if we've reached the end of the data
        if start_loc >= len(df):
            print("\nNo more data to display.")
            break
            
        view_data = input("Do you wish to see the next 5 rows? Enter yes or no: ").lower()

    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
              
              