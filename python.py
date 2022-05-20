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
    while True  :
                city = input ("please enter a city from ( chicago , new york city ,washington  )\n ").lower()
                if city not in CITY_DATA :
                    print ("invalid input , your input should be: chicago , new york city or washington")
                else:
                    break 
    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january' , 'february' , 'march' , 'april' ,'may' , 'june' , 'all' ]
    while True :
        month = input ("please enter a month : january , february , march , april ,may , june , all )\n :").lower()
        if month not in months :
            print ( " invalid input , your input should be: january, february, march, april, may, june or all ")
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday' , 'monday' , 'tuesday' , 'wednesday' , ' thursday' , 'friday' , 'saturday' ,'all']
    while True :
        day = input (" please enter a day : (sunday , monday , tuesday , wednesday , thursday , friday , saturday , all)\n :").lower()
        if day not in days:
            print ( ' invalid input , your input should be: sunday, ... friday, saturday or all ')
        else :  
            break
            
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
    #file_name = CITY_DATA[city]
        
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
   # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour 
    
    # filter by month if applicable
    if month != 'all': 
        # use the index of the months list to get the corresponding int
        months = ['january' , 'february' , 'march' , 'april' ,'may' , 'june'  ] 
        month = months.index(month) + 1
        df = df[df['month'] == month ]
   
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]      
                
    return df
def display_data (df):
    #display the first five rows of row data
    i=0
    data = input (' would you like to display the frist five row of data ? Yes / No : ').title()
    if data not in ['Yes' , 'No' ]:
        print (' invalid input , your input should be: Yes or No ')
    elif data =='No':
        print ('thank you')
    else :
        print (df.head(5))
         #display the more five rows of row data
        while True :
           i+=5
           data = input (' would you like to display the more row of data ? Yes / No : ').title()
           if data not in ['Yes' , 'No']:
                print (' invalid input , your input should be: Yes or No ')
           elif data =='Yes':
                print (df.iloc[i:i+5])
           else :
                print ('thank you')
                break 

def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:{}'.format( popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Day Of Week:', popular_day_of_week)

    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('the most start station is :{}'.format( popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('the most end station is :{}'.format( popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end = (df['Start Station'] + ',' +  df['End Station']).mode()[0]
    print ('most frequent : {}'.format(popular_start_end))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('total travel time: {}  seconds or  total travel time: {}  hours'.format(total_travel_time , round(total_travel_time/3600 , 4)))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean().round(2)
    print ('mean travel time : {} seconds or  mean travel time: {}  hours'.format( mean_travel_time , round(mean_travel_time/3600,4 )))

    print('\nThis took %s seconds.' % (time.time() - start_time)) 
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    User_types = df['User Type' ].value_counts()
    print ('User types' ,  User_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print (df['Gender'].value_counts())
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print ('the most common year of birth is ', df['Birth Year'].mode()[0] )
        print ('the most recent year of birth is ', df['Birth Year'].max())
        print ('the most earliest  year of birth is ', df['Birth Year'].min())
    else :
        print('there is no data for this city ')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city , month , day)
        display_data (df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
