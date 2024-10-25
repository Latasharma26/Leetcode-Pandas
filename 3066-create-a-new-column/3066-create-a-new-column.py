import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2  # Create a new column 'bonus' that is double the 'salary'
    return employees  # Return the updated DataFrame