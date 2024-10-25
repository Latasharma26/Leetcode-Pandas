import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    result = weather.pivot(
        index='month',
        columns='city',
        values='temperature',  # Corrected spelling
             # Use 'aggfunc' instead of 'afffunc'
    )  # Reset the index to keep 'month' as a column


    return result