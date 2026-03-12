import time
import pandas as pd

CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

def get_user_input(prompt, options):
    """Validates user input against a list of options."""
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in options:
            return user_input
        print(f"Invalid input. Options: {', '.join(options)}")

def timed_analysis(label):
    """Helper to wrap stat functions with headers and timing."""
    print(f"\n--- Calculating {label} ---")
    start_time = time.time()
    yield
    print(f"Done in {time.time() - start_time:.4f}s")

def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data!')
    city = get_user_input("City (Chicago, New York City, Washington): ", list(CITY_DATA.keys()))
    month = get_user_input("Month (all, january...june): ", ['all', 'january', 'february', 'march', 'april', 'may', 'june'])
    day = get_user_input("Day (all, monday...sunday): ", ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract filter components
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    
    return df

def show_stats(df):
    """Main stats engine."""
    
    # 1. Time Stats
    with timed_analysis("Travel Times"):
        print(f"Most Common - Month: {df['month'].mode()[0].title()}, "
              f"Day: {df['day_of_week'].mode()[0].title()}, "
              f"Hour: {df['hour'].mode()[0]}")

    # 2. Station Stats
    with timed_analysis("Popular Stations"):
        pop_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
        print(f"Start: {df['Start Station'].mode()[0]}")
        print(f"End:   {df['End Station'].mode()[0]}")
        print(f"Trip:  {pop_trip}")

    # 3. Trip Duration
    with timed_analysis("Trip Duration"):
        total = df['Trip Duration'].sum()
        print(f"Total: {total:,.0f}s ({total/3600:,.1f} hrs) | Avg: {df['Trip Duration'].mean():.1f}s")

    # 4. User Stats
    with timed_analysis("User Demographics"):
        if 'User Type' in df:
            print(df['User Type'].value_counts().to_string(), "\n")
        if 'Gender' in df:
            print(df['Gender'].value_counts().to_string(), "\n")
        if 'Birth Year' in df:
            years = df['Birth Year'].dropna()
            if not years.empty:
                print(f"Birth Year - Earliest: {int(years.min())}, Latest: {int(years.max())}, Common: {int(years.mode()[0])}")

def display_raw_data(df):
    """Shows 5 lines of data at a time."""
    i = 0
    while get_user_input("View 5 rows of raw data? (yes/no): ", ['yes', 'no']) == 'yes':
        print(df.iloc[i : i + 5])
        i += 5
        if i >= len(df):
            print("No more data to show.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if not df.empty:
            show_stats(df)
            display_raw_data(df)
        else:
            print("No results found for those filters.")

        if get_user_input("\nRestart? (yes/no): ", ['yes', 'no']) != 'yes':
            break

if __name__ == "__main__":
    main()
