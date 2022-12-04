import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = data['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(data.loc[data['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(data.loc[data['education'] == 'Bachelors'])/len(data))*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = data.loc[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = data.loc[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round((len(higher_education.loc[higher_education['salary'] == '>50K'])/len(higher_education))*100, 1)
    lower_education_rich = round((len(lower_education.loc[lower_education['salary'] == '>50K'])/len(lower_education))*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = data['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(data.loc[data['hours-per-week'] == data['hours-per-week'].min()])

    rich_percentage = round((len(data.loc[(data['hours-per-week'] == data['hours-per-week'].min()) & (data['salary'] == '>50K')])/num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    s1 = data['native-country'].value_counts()
    s1.name = 'total'
    s2 = data.loc[data['salary'] == '>50K']['native-country'].value_counts()
    s2.name = '>50K'
    df = pd.concat([s1, s2], axis = 1)
    df.index.name = 'country'
    df['new-column'] = round((df['>50K']/df['total'])*100, 1)
    highest_earning_country = df.loc[df['new-column'] == df['new-column'].max()].index[0]
    highest_earning_country_percentage = df['new-column'].max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = data.loc[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
