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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    x = 'invalid'
    y = 'valid'
    z = 'valid'
    while x == 'invalid':
        city = input("\nWhich city would you like to explore today? ").lower()
        message = "\n    Ok, let\'s go to {}!"
        if city.lower() == 'chicago':
            x ='valid'
            print(message.format(city.title()))
            y = 'invalid'
        elif city.lower() == 'new york city':
            x ='valid'
            print(message.format(city.title()))
            y = 'invalid'
        elif city.lower() == 'washington':
            x ='valid'
            print(message.format(city.title()))
            y = 'invalid'
        else:
            print('\n    *** Oops, we don\'t have data for {} ***'.format(city.title()))
            print('\n    Please try again. We can accept: Chicago, New York City, or Washington. ')


    # get user input for month (all, january, february, ... , june)
    while y =='invalid':
        month = input("\nWhich month are you interested in? ").lower()
        message = "\n    Ok, let\'s look at {} in {}!"
        if month.lower() == 'january':
            y ='valid'
            print(message.format(city.title(),month.title()))
            z = 'invalid'
        elif month.lower() == 'february':
            y = 'valid'
            print(message.format(city.title(),month.title()))
            z = 'invalid'
        elif month.lower() == 'march':
            y = 'valid'
            print(message.format(city.title(),month.title()))
            z = 'invalid'
        elif month.lower() == 'april':
            y = 'valid'
            print(message.format(city.title(),month.title()))
            z = 'invalid'
        elif month.lower() == 'may':
            y = 'valid'
            print(message.format(city.title(),month.title()))
            z = 'invalid'
        elif month.lower() == 'june':
            y = 'valid'
            print(message.format(city.title(),month.title()))
            z = 'invalid'
        elif month.lower() == 'all':
            y = 'valid'
            print("\n    Ok, let\'s look at {} months from January until June!".format(month.upper()))
            z = 'invalid'
        else:
            print('\n    *** Oops, we don\'t have data for {} ***'.format(month.title()))
            print('\n    Please try again. We can accept any month from January until June or ALL. ')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while z == 'invalid':
        day = input("\nWhich day of the week would you like to look at? ").lower()
        message = "\n    Excellent. You\'re final fiter selections are:\n    City: {}\n    Month(s): {}\n    Day(s): {}\n    Let\'s go!!!"
        if day.lower() == 'monday':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
            day = 0
        elif day.lower() == 'tuesday':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
            day = 1
        elif day.lower() == 'wednesday':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
            day = 2
        elif day.lower() == 'thursday':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
            day = 3
        elif day.lower() == 'friday':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
            day = 4
        elif day.lower() == 'saturday':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
            day = 5
        elif day.lower() == 'sunday':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
            day = 6
        elif day.lower() == 'all':
            z = 'valid'
            print(message.format(city.title(),month.title(),day.title()))
        else:
            print('\n    *** Oops, we don\'t have data for {} ***'.format(day.title()))
            print('\n    Please try again. We can accept: Monday through Sunday or ALL. ')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    ### display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month
    popular_month = df['month'].mode()[0]
    month_names = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}
    popular_month_name = month_names[popular_month]
    print('Most common month:', popular_month_name)

    ### display the most common day of week
    #extract weekday from Start Time column to create a weekday column
    df['day_of_week'] = df['Start Time'].dt.weekday
    # find the most common day
    popular_day = df['day_of_week'].mode()[0]
    day_names = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    popular_day_name = day_names[popular_day]
    print('Most common day:', popular_day_name)
    ### display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    hour_conversion = {0:'12:00am',1:'1:00am',2:"2:00am",3:'3:00am',4:'4:00am',5:'5:00am',6:'6:00am',7:'7:00am',8:'8:00am',9:'9:00am',10:'10:00am',11:'11:00am',12:'12:00pm',13:'1:00pm',14:'2:00pm',15:'3:00pm',16:'4:00pm',17:'5:00pm',18:'6:00pm',19:'7:00pm',20:'8:00pm',21:'9:00pm',22:'10:00pm',23:'11:00pm'}
    popular_hour_conversion = hour_conversion[popular_hour]
    print('Most Frequent Start Hour:', popular_hour_conversion)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most common Start Station: ', popular_start)
    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most common End Station: ', popular_end)

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] +" - "+ df['End Station']
    popular_combo = df['Start End'].mode()[0]
    print('Most popular start station to end station trip: ', popular_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total trip time (seconds): ', total_time)
    print('Approximate total trip time (minutes): ', round(total_time / 60, 2))

    # display mean travel time
    average_time = df['Trip Duration'].mean()
    print('Average trip time (seconds): ', average_time)
    print('Approximate average trip time (minutes): ', round(average_time / 60, 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except KeyError:
        print('No gender data is available in this dataset')
    # Display earliest, most recent, and most common year of birth
    try:
        birth_years = df['Birth Year'].unique()
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        popular_year = df['Birth Year'].mode()
        print('The earliest birth year is: {}\nThe most recent birth year is: {}\nand the most common birth year is: {}'.format(int(earliest_year), int(recent_year), int(popular_year)))
    except KeyError:
        print('No birth year data is available in this dataset')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays 5 rows of raw data to user until user opts out"""
    a = -5
    b = -4
    c = -3
    d = -3
    e = -1
    opt_in = input('\nWould you like to see five rows of raw data? Enter yes or no.\n')
    while opt_in.lower() == 'yes':
        pd.set_option('display.max_columns',200)
        a += 5
        b += 5
        c += 5
        d += 5
        e += 5
        print(df.iloc[[a,b,c,d,e]])
        opt_in = input('\nWould you like to see the next 5 rows of data? Enter yes or no.\n')
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
