import time
import pandas as pd

CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

def get_user_input(prompt, options):
    """Universal helper for validated user input."""
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in options:
            return user_input
        print(f"Invalid choice. Please select from: {', '.join(options)}")

def load_data(city, month, day):
    """Loads and filters data based on city, month, and day."""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract time components
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    
    return df

def run_stats(df):
    """Displays all statistical calculations."""
    
    # 1. Time Stats
    print("\n--- Calculating Travel Times ---")
    start = time.time()
    # Fixed .mode() handling by accessing index [0]
    print(f"Most Common Month: {df['month'].mode()[0].title()}")
    print(f"Most Common Day:   {df['day_of_week'].mode()[0].title()}")
    print(f"Most Common Hour:  {df['hour'].mode()[0]}")
    print(f"Done in {time.time() - start:.4f}s")

    # 2. Station Stats
    print("\n--- Calculating Popular Stations ---")
    start = time.time()
    print(f"Start Station: {df['Start Station'].mode()[0]}")
    print(f"End Station:   {df['End Station'].mode()[0]}")
    pop_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f"Most Popular Trip: {pop_trip}")
    print(f"Done in {time.time() - start:.4f}s")

    # 3. Trip Duration
    print("\n--- Calculating Trip Duration ---")
    start = time.time()
    total_sec = df['Trip Duration'].sum()
    print(f"Total Travel Time:   {total_sec:,.0f}s ({total_sec/3600:,.1f} hrs)")
    print(f"Average Travel Time: {df['Trip Duration'].mean():.1f}s")
    print(f"Done in {time.time() - start:.4f}s")

    # 4. User Stats
    print("\n--- Calculating User Stats ---")
    start = time.time()
    if 'User Type' in df:
        print(df['User Type'].value_counts().to_string(), "\n")
    if 'Gender' in df:
        print(df['Gender'].value_counts().to_string(), "\n")
    if 'Birth Year' in df:
        years = df['Birth Year'].dropna()
        if not years.empty:
            print(f"Birth Year - Oldest: {int(years.min())}, Youngest: {int(years.max())}, Common: {int(years.mode()[0])}")
    print(f"Done in {time.time() - start:.4f}s")

def display_raw_data(df):
    """Asks user if they want to see 5 lines of raw data at a time."""
    i = 0
    while True:
        view = input("\nWould you like to see 5 rows of raw trip data? (yes/no): ").lower()
        if view != 'yes':
            break
        print(df.iloc[i : i + 5])
        i += 5
        if i >= len(df):
            print("End of data reached.")
            break

def main():
    while True:
        city, month, day = (
            get_user_input("Select City (Chicago, New York City, Washington): ", list(CITY_DATA.keys())),
            get_user_input("Select Month (all, january...june): ", ['all', 'january', 'february', 'march', 'april', 'may', 'june']),
            get_user_input("Select Day (all, monday...sunday): ", ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
        )

        df = load_data(city, month, day)

        if not df.empty:
            run_stats(df)
            display_raw_data(df)
        else:
            print("\nNo data matches those filters. Please try again.")

        if input("\nRestart? (yes/no): ").lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
