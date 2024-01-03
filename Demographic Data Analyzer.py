import pandas as pd
import numpy as np

def analyze_demographic_data(csv_file):
    df = pd.read_csv(csv_file)

    # Count of each race
    race_counts = df['race'].value_counts()

    # Average age of men
    avg_age_men = df[df['sex'] == 'Male']['age'].mean()

    # Percentage of people with a Bachelor's degree
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = bachelors_count / df.shape[0] * 100

    # Percentage of people with advanced education making more than 50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    df_advanced_education = df[df['education'].isin(advanced_education)]
    percentage_advanced_education_high_income = (df_advanced_education[df_advanced_education['salary'] == '>50K'].shape[0] / df_advanced_education.shape[0]) * 100

    # Percentage of people without advanced education making more than 50K
    df_non_advanced_education = df[~df['education'].isin(advanced_education)]
    percentage_non_advanced_education_high_income = (df_non_advanced_education[df_non_advanced_education['salary'] == '>50K'].shape[0] / df_non_advanced_education.shape[0]) * 100

    # Minimum number of hours a person works per week
    min_hours_worked = df['hours-per-week'].min()

    # Percentage of the people who work the minimum number of hours per week have a salary of more than 50K
    df_min_hours_worked = df[df['hours-per-week'] == min_hours_worked]
    percentage_min_hours_worked_high_income = (df_min_hours_worked[df_min_hours_worked['salary'] == '>50K'].shape[0] / df_min_hours_worked.shape[0]) * 100

    # Country with the highest percentage of people that earn >50K
    df_non_usa = df[df['native-country'] != 'United-States']
    country_income_percentage = df_non_usa.groupby('native-country')['salary'].value_counts(normalize=True) * 100
    highest_income_percentage_country = country_income_percentage[country_income_percentage == country_income_percentage.max()].index[0]
    highest_income_percentage = round(country_income_percentage.max(), 1)

    # Most popular occupation for those who earn >50K in India
    df_india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation_india = df_india_high_income['occupation'].value_counts().idxmax()

    return race_counts, avg_age_men, percentage_bachelors, percentage_advanced_education_high_income, percentage_non_advanced_education_high_income, min_hours_worked, percentage_min_hours_worked_high_income, highest_income_percentage_country, highest_income_percentage, most_popular_occupation_india

race_counts, avg_age_men, percentage_bachelors, percentage_advanced_education_high_income, percentage_non_advanced_education_high_income, min_hours_worked, percentage_min_hours_worked_high_income, highest_income