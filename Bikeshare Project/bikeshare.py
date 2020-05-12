import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['all','january','february','march','april','may','june']
weekdaynames = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
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
    city=input("\nPlease enter any of the following cities to explore the data: chicago, new york city, washington: ").lower()
    
    while(True):
        if city in CITY_DATA.keys():
            break
        else:
            city=input("\nPlease enter the correct city name: ").lower()
                   
    # TO DO: get user input for month (all, january, february, ... , june)
   
    month = input("\nPlease enter any of the filter month: all,january,february,march,april,may,june: ").lower()
    
    while(True):    
        if month in months:
            break
        else:
            month=input("\nPlease enter the correct month name: ").lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("\nPlease enter any of the filter day: all,monday,tuesday,wednesday,thursday,friday,saturday,sunday: ").lower()
    while(True):
        if day in weekdaynames:
            break
        else:
            day=input("\nPlease enter the correct day name: ").lower()
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel.
    Input: DataFrame, month name, day of week
    Conditions: In case the month is All, mode is not displayed, similarly, if day is all, mode is not displayed
    Output: Mode value of the various station columns
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if(month == 'all'):
        print("The most common month is: {}".format(pd.to_datetime(df['Start Time']).dt.month_name().mode()[0]))

    # TO DO: display the most common day of week
    if(day == 'all'):
        print("The most common day is: {}".format(weekdaynames[pd.to_datetime(df['Start Time']).dt.dayofweek.mode()[0]]))

    # TO DO: display the most common start hour
    print("The most common hour is: {}".format(pd.to_datetime(df['Start Time']).dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Input: DataFrame
    Output: Mode value of the various station columns
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most commonly used start station: {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("\nThe most commonly used end station: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    print("\nThe most frequent from and to stations are: {}".format(df['combination'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Input: DataFrame
    Output: Duration calculated in terms of Day, hour, minute & seconds
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    num_seconds = df['Trip Duration'].sum()
    days = num_seconds // (60 * 60 * 24)
    num_seconds -= days * (60 * 60 * 24)
    hours = num_seconds // (60 * 60)
    num_seconds -= hours * (60 * 60)
    minutes = num_seconds // 60
    num_seconds = minutes % 60
    print("\nTotal travel time: {} Days, {} hours , {} Minutes and {} Seconds".format( days, hours, minutes, num_seconds))

    # TO DO: display mean travel time
    meantt= df['Trip Duration'].mean()
    days = meantt // (60 * 60 * 24)
    meantt -= days * (60 * 60 * 24)
    hours = meantt // (60 * 60)
    meantt -= hours * (60 * 60)
    minutes = meantt // 60
    meantt = minutes % 60
    print("\nMean travel time: {} hours , {} Minutes and {} Seconds".format(hours, minutes, meantt))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #Loop according to the user type column and print all the index and values
    for i in df['User Type'].value_counts().index.tolist():
        print("\nUser type:{}, Value: {}".format(i,df['User Type'].value_counts()[i]))
    # TO DO: Display counts of gender

    if('Gender' in df.columns):
        if df['Gender'].isnull().any():
            print("\nNaN values found in Gender. Forward filling them.....")
            df['Gender']=df['Gender'].fillna(method = 'ffill', axis=0)
        
        data=df['Gender'].value_counts()
        for i in data.index.tolist():
            print("\nGender:{}, Value: {}".format(i,data[i]))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        if df['Birth Year'].isnull().any():
            print("\nNaN values found in Birth Year. Forward filling them.....")
            df['Birth Year']=df['Birth Year'].fillna(method = 'ffill', axis=0)
        print("\nEarliest Year of birth: {}".format(df['Birth Year'].min()))
        print("\nMost Recent Year of birth: {}".format(df['Birth Year'].max()))
        print("\nMost Common of birth: {}".format(df['Birth Year'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)

def display(df):
    rows=5
    st=0
    end=rows-1
    
    while(True):
        view_data = input("\nWould you like to view some user data? Enter yes or no: ")
        if view_data.lower()=='yes':
            print("\nDisplaying rows {} to {}".format(st+1, end+1))
            print('\n', df.iloc[st:end+1])
            st+=rows
            end+=rows
        elif view_data.lower == 'no':
            break
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
