import sales_pipe
import weather_pipe
import pandas as pd

def main()->pd.DataFrame:
    weather_temp = list()
    weather_description = list()
    sales_data = sales_pipe.data()
    for entry in sales_data:
        temp, des = weather_pipe.grep_data(entry["plz"])
        weather_temp.append(temp)
        weather_description.append(des)
    sales_data["Temperature"] = weather_temp
    sales_data["Description"] = weather_description
    return sales_data
