'''Lauren Whitaker: This module provides a reusable byline for the author's services. '''

import math
import statistics

def main():
  #define variables 
  company_name: str = 'Dogs 4 All, LLC'
  company_description: str = 'Top Rated Dog Adoption Service'
  current_employees: int = 12
  company_founding_year: int = 2024
  company_city: str = 'Kansas City'
  company_state: str = 'Missouri'
  has_all_analytics: bool = True
  employee_satisfaction: float = 7.5
  breakroom_snacks: list = ['Coffee', 'Water',  
  'Dog Treats']
  company_ratings: list = [9.2, 9.4, 9.8, 
  9.7, 9.5]
  work_options: list = ['Onsite']

# Multiline string with byline using f-string formatting
  general_overview_string: str = f"""
  Company: {company_name}
  Description: {company_description}
  Has All Analytics: {has_all_analytics}
  Employee Satisfaction: {employee_satisfaction} out of 10!
  Work Options: {work_options}
  Breakroom Snacks: {breakroom_snacks}
  """

  stats_string: str = f"""
  More Details: 
  Number of Happy Employees: {current_employees}
  Lowest Outside Rating: {min(company_ratings)}
  Highest Outside Rating: {max(company_ratings)}
  Number of Ratings: {len(company_ratings)}
  Average Outside Rating: 
  {statistics.mean(company_ratings)}
  Total: {sum(company_ratings)}
  Mode: {statistics.mode(company_ratings)}
  Median: {statistics.median(company_ratings)}
  Standard Deviation: {statistics.stdev(company_ratings)}
  """

  byline: str = f"""
  {general_overview_string}
  {stats_string}
  """
  print(byline)

if __name__ == '__main__':
  main()
