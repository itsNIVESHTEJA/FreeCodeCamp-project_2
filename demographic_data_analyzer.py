import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.csv")
    

   
    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

   
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education]['salary'] == '>50K').mean() * 100, 1)

    
    lower_education = ~advanced_education
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    
    min_work_hours = df['hours-per-week'].min()

    
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

   
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    if not country_salary.empty and not country_counts.empty:
        highest_earning_country = (country_salary / country_counts * 100).idxmax()
        highest_earning_country_percentage = round((country_salary / country_counts * 100).max(), 1)
    else:
        highest_earning_country = None
        highest_earning_country_percentage = 0

   
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_rich.empty:
        top_IN_occupation = india_rich['occupation'].mode()[0]
    else:
        top_IN_occupation = None

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


