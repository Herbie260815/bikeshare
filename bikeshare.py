# Version 2: refactored for clarity
# Author: Herbie

# Websites I used to check some commands and Python in general
# https://stackoverflow.com/
# https://pandas.pydata.org/pandas-docs/
# https://www.datasciencemadesimple.com/
# https://www.w3schools.com/python/
# https://realpython.com/
# https://python-kurs.eu/python3_kurs.php
# https://www.python.org/

# Changes July 12th 26
# Refactoring Step 2: improved code readability
           
import time
import datetime
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
    
    city = " "
    month = " "
    day = " "
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    zaehler = 0
    while city == " ":
        zaehler = zaehler + 1
        if (zaehler == 1):
            cityeingabe = input("Please enter the name of the city (Chicago, New York City, Washington) you want to analyze: ")
        else:
            cityeingabe = input("Please try again. There wa something wrong with the first attempt. Please enter the name of the city you want to analyze again: ")
        city = check_cityname(cityeingabe)
        
    print("The selected value for city is " + city + "\n")
    
       
    
    # TO DO: get user input for month (all, january, february, ... , june)
    zaehler = 0
    
    while month == " ":
        zaehler = zaehler + 1
        if (zaehler == 1):
            montheingabe = input("Please enter any month (all, january, february, ... , june) you want to analyze: ")
        else:
            montheingabe = input("Please try again. There wa something wrong with the first attempt. Please enter the name of the month (all, january, february, ... , june) you want to analyze again: ")
        month = check_monthname(montheingabe)
        
    print("The selected value for month is " + month + "\n")
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    zaehler = 0
    
    while day == " ":
        zaehler = zaehler + 1
        if (zaehler == 1):
            dayeingabe = input("Please enter any day of the week (all, monday, tuesday, ... sunday) you want to analyze: ")
        else:
            dayeingabe = input("Please try again. There wa something wrong with the first attempt. Please enter the name of the day (all, monday, tuesday, ... sunday) you want to analyze again: ")
        day = check_dayname(dayeingabe)
        
    print("The selected value for day is " + day + "\n")
    
    print('-'*80)
    print("\n")
    return city, month, day




def check_cityname(name):
    cities = ("chicago", "newyorkcity", "newyork", "washington")
    name = name.lower().replace(" ", "")
    
    if (name.isalpha() == True) and (name in cities):
        if name == "newyork" or name == "newyorkcity":
            name = "new york city"
        name = name.title()
    else:
        name = " "
    return name




def check_monthname(name):
    #monate = ("all", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
    monate = ("all", "january", "february", "march", "april", "may", "june")
    name = name.lower().replace(" ", "")

    if (name.isalpha() == True) and (name in monate):
        name = name.title()
    else:
        name = " "
    return name




def check_dayname(name):
    tage = ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    name = name.lower().replace(" ", "")
    
    if (name.isalpha() == True) and (name in tage):
        name = name.title()
    else:
        name = " "
    return name




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
    
    monate = ["All", "January", "February", "March", "April", "May", "June"]
    monate_int = monate.index(month)    
    
    tage = ["All", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]
    tage_int = tage.index(day)

    filename = (city.lower().replace(" ", "_") + '.csv')
    df = pd.read_csv(filename)
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['filter_month'] = df['Start Time'].dt.month
    df['filter_day'] = df['Start Time'].dt.day
    df['filter_weekday'] = df['Start Time'].dt.weekday    # Monday = 0
    df['hour'] = df['Start Time'].dt.hour
        
    if (month != 'All'):
        df = df[df['filter_month'] == monate_int]
        
    if (day != 'All'):
        df = df[df['filter_weekday'] == (tage_int - 1)]    
    
    return df




def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    monate = ["All", "January", "February", "March", "April", "May", "June"]                         #perhaps it would be better to use this as a global variable
    tage = ["All", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday" ]     #perhaps it would be better to use this as a global variable
    

    # TO DO: display the most common month

    if (month == 'All'):
        print("The most common month is: ", monate[df['filter_month'].mode()[0]])

    # TO DO: display the most common day of week
    if (day == 'All'):
        print("The most common day of the week is: ", tage[df['filter_weekday'].mode()[0]])    
    
    # TO DO: display the most common start hour
    print("The most common start hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    print("\n")

    
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])
    

    # TO DO: display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])

    # Note if start and end the same
    if((df['Start Station'].mode()[0]) == (df['End Station'].mode()[0])):
        print("The most commonly used start station and the most commonly used end station are identically!")

    # TO DO: display most frequent combination of start station and end station trip
    combination_string =  ('From: ' + df['Start Station'] + '  To: ' + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is: " + combination_string) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    print("\n")

    
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    sec_total = df['Trip Duration'].sum()
    
    #  I assume that sec_total is not below 60 minutes
    
    if sec_total >= 86400:    # days, hours, minutes, seconds
        total_days = int(sec_total / 86400)
        total_hours =  int((sec_total - 86400 * total_days) / 3600)
        total_minutes = int((sec_total - (86400 * total_days + 3600 * total_hours)) / 60)
        total_seconds = round(sec_total - (86400 * total_days + 3600 * total_hours + 60 * total_minutes), 3)
        print("The total travel time is", total_days, "days,", total_hours, "hours,", total_minutes, "minutes and", total_seconds, "seconds.")
        
    elif sec_total >= 3600:   #hours, minutes, seconds
        total_hours =  int(sec_total / 3600)
        total_minutes = int((sec_total - (3600 * total_hours)) / 60)
        total_seconds = round(sec_total - (3600 * total_hours + 60 * total_minutes), 3)
        print("The total travel time is", total_hours, "hours,", total_minutes, "minutes and", total_seconds, "seconds.")
        
    # TO DO: display mean travel time
    #  I assume that the mean travel time is less than one hour and therefore I don't 'convert' the value into hours, but minutes and seconds
    
    mean_total = df['Trip Duration'].mean()
    mean_minutes = int(mean_total / 60)
    mean_seconds = round(mean_total - (60 * mean_minutes), 3)
    print("The mean travel time is", mean_minutes, "minutes and", mean_seconds, "seconds.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    print("\n")

    
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...\n')
    start_time = time.time()
    
    # Check columns
    # ==> comes later

    # TO DO: Display counts of user types
    print("User Type distribution:\n\n", df['User Type'].value_counts().to_frame(), "\n\n\n")
    
    # TO DO: Display counts of gender
    if ("Gender" in df):
        print("Gender distribution:\n\n", df['Gender'].value_counts().to_frame(), "\n\n\n")
    else:
        print("There is no column for \"Gender\" in this database.\n\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    if ("Birth Year" in df):
        print("The earliest year of birth: ", int(df['Birth Year'].min()), "\n")
        print("The most recent year of birth: ", int(df['Birth Year'].max()), "\n")
        print("The most common year of birth: ", int(df['Birth Year'].mode()[0]), "\n")
        #print("\n\nValue Counts(most common year of birth): ", df['Birth Year'].value_counts())
    else:
        print("There is no column for \"Birth year\" in this database.\n\n")
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
    print("\n")
    
    
    
    
def show_rows(df, city, month, day):
    
    print("Do you want to see the raw data (all months and all days) for the selected city?")
    raw_input = input("Please type \"Yes\" to see the first five rows or \"No\" to cancel this function:     ")
    
    if(raw_input.lower() == 'yes'):
        #Check if df has already the full raw data for this city or if it's limited. If it's limited by month or day it has to be load again.
        if((month != 'All') or (day != 'All')):
            month = 'All'
            day = 'All'
            print("csv has to be load again!\n")
            df = load_data(city, month, day)            
            
        startrow = 0          
        maxvalue = len(df)    
            
        while(raw_input.lower() == 'yes'):        
            print(df[startrow:(startrow + 5)])
            startrow = startrow + 5
                
            if(startrow < maxvalue):
                raw_input = input("\nPlease type \"Yes\" to see the next five rows or \"No\" to cancel this function:     ")
            else:
                print("\nYou have already reached the end of the raw data list!\n\n\n")
                raw_input = "No"
                       
    print("\nThis is the end of the program!\n\n\n\n\n")                
              
        
        
              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
    
        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_rows(df, city, month, day)

        restart = input('\nWould you like to restart? Please enter \"yes\" for another run of the program. Any other input will terminate the program.\n')
        if restart.lower() != 'yes':
            break

            
            

if __name__ == "__main__":
	main()