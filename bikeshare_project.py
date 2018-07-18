import time
import pandas as pd
import numpy as np

#filtering data according to city:
print('Hello! Let\'s explore some US bikeshare data!')
print('-'*100)

def get_filters_city():
    loop_count_city = 1
    city = ''
    while city!= 'chicago' and city!= 'new york city' and city!= 'washington':
        if loop_count_city != 1:
            print('-'*100)
            print('You entered a wrong value. Please try again.')
        city = input ('Would you like to see analysis of bikeshare for chicago, new york city, or washington?').lower()
        loop_count_city +=1
    print('-'*100)

    loop_count_month = 1
    day = ''
    month = ''
    while month != 'none' and month not in months:
        if loop_count_month != 1:
            print('-'*100)
            print('You entered a wrong value. Please try again.')
        month = input('Would you like to filter data by month!! \nif yes, which month - january, february, march, april, may or june? \nif no, type none  ').lower()
        loop_count_month +=1

    loop_count_day = 1
    print('-'*100)
    while day != 'none' and day not in weekdays:
        if loop_count_day != 1:
            print('-'*100)
            print ('You entered a wrong value. Please try again.')
        day = input('Would you like to filter data by day!! \nif yes, which day - monday, tuesday, wednesday, thursday, friday, saturday or sunday? \nif no, type none  ').lower()
        loop_count_day += 1

    print('-'*100)
    return city, month, day

#loading data
data= ''
months = ['january', 'february', 'march', 'april', 'may', 'june']
weekdays= ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
def load_data(city, month, day):
    if city == 'chicago':
        data= pd.read_csv('chicago.csv')
    elif city == 'new york city':
        data= pd.read_csv('new_york_city.csv')
    elif city == 'washington':
        data= pd.read_csv('washington.csv')
    else:
        print('you have choosen a city for which data is not available!')

    data['Start Time']= pd.to_datetime(data['Start Time'])
    data['month'] = data['Start Time'].dt.month
    if month != 'none':
        month = months.index(month) + 1
        data = data[data['month'] == month]


    data['weekday'] = data['Start Time'].dt.weekday
    if day != 'none':
        # filter by day of week to create the new dataframe
        day = weekdays.index(day)
        data = data[data['weekday'] == day]

    return data


def time_stats(month,day,data):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    if month == 'none':
        popular_month = data['month'].mode()[0]
        popular_month_names= months[popular_month - 1]
        print('Most Frequent Month of Travel:',popular_month_names.title())

    # display the most common day of week
    if day == 'none':
        popular_weekday = data['weekday'].mode()[0]
        popular_weekday_names= weekdays[popular_weekday]
        print('Most Frequent Day of Travel:', popular_weekday_names.title())

    # display the most common start hour
    data['hour'] = data['Start Time'].dt.hour
    popular_hour = data['hour'].mode()[0]
    print('Most Frequent Hour of Travel:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(data):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_ss= data['Start Station'].mode()[0]
    print('Most popular Start Station:', popular_ss)
    # display most commonly used end station
    popular_es= data['End Station'].mode()[0]
    print('Most popular End Station:', popular_es)
    # display most frequent combination of start station and end station trip
    data['start_end']= data['Start Station'] + data['End Station']
    popular_se= data['start_end'].mode()[0]
    print('Most popular combination of Start and End Station:', popular_se)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def trip_duration_stats(data):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_trip_time= data['Trip Duration'].sum()
    print('The Total Travel Time is {} Hours'. format(total_trip_time/3600))
    # display mean travel time
    avg_trip= data['Trip Duration'].mean()
    print('The Average Travel Time is {} Minutes'. format(avg_trip/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def user_stats(city, data):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = data['User Type'].value_counts()
    print(user_types)
    # Display counts of gender
    if city== 'chicago' or city == 'new york city':
        gender = data['Gender'].value_counts()
        print(gender)
    else:
        print('No Data for Gender Available')

    # Display earliest, most recent, and most common year of birth
    if city== 'chicago' or city== 'new york city':
        earliest_birth= data['Birth Year'].min()
        recent_birth= data['Birth Year'].max()
        common_birth= data['Birth Year'].mode()[0]
        print('The most common birth year to use bikeshare is', common_birth)
        print('The earliest birth year to use bikeshare is', earliest_birth)
        print('The most recent birth year to use bikeshare is', recent_birth)
    else:
        print('No Data for Birth Year Available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(data):
    n = 5
    m = n + 5
    loop_count_user = 1
    ask_user = ''
    loop_count_user_again = 1
    ask_user_again = ''
    loop_count_user_repeat = 1
    while ask_user != 'yes' and ask_user != 'no':
        if loop_count_user != 1:
            print('-'*100)
            print ('You entered a wrong value. Please try again.')
        ask_user = input('Would you like to see raw data? yes or no? ').lower()
        loop_count_user += 1

    if ask_user == 'yes':
        print(data.iloc[0:5])
        while ask_user_again != 'yes' and ask_user_again != 'no':
            if loop_count_user_again != 1:
                print('-'*100)
                print ('You entered a wrong value. Please try again.')
            ask_user_again = input('Would you like to see five more lines of raw data? yes or no? ').lower()
            loop_count_user_again += 1
    while ask_user_again == 'yes' :
        print(data.iloc[n:m])
        n += 5
        m += 5
        ask_user_again = input('would you like to see five more lines of raw data? yes or no? ').lower()
        while ask_user_again != 'yes' and ask_user_again != 'no':
            if loop_count_user_repeat != 1:
                print('-'*100)
                print ('You entered a wrong value. Please try again.')
            ask_user_again = input('Would you like to see five more lines of raw data? yes or no? ').lower()
            loop_count_user_repeat += 1


def main():
    while True:
        city, month, day = get_filters_city()
        data = load_data(city, month, day)
        time_stats(month,day,data)
        station_stats(data)
        trip_duration_stats(data)
        user_stats(city, data)
        display_data(data)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
