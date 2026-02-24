import pandas as pd

height_data = [
    {"Name": "Addiya", "Height": 179},
    {"Name": "Samen", "Height": 189},
    {"Name": "Darek", "Height": 199},
    {"Name": "John", "Height": 169},
]

weight_data = [
    {"Name": "Addiya", "Weight": 79},
    {"Name": "Samen", "Weight": 89},
    {"Name": "Darek", "Weight": 99},
    {"Name": "John", "Weight": 69},
]

marks_data = [
    {"Name": "Addiya", "Marks": 179},
    {"Name": "Samen", "Marks": 189},
    {"Name": "Darek", "Marks": 199},
    {"Name": "John", "Marks": 169},
]

height_data_df = pd.DataFrame(height_data)
weight_data_df = pd.DataFrame(weight_data)
marks_data_df = pd.DataFrame(marks_data)

writer = pd.ExcelWriter('excel_with_multiple_sheets.xlsx', engine="xlsxwriter")

height_data_df.to_excel(writer, sheet_name="height", index=False)
weight_data_df.to_excel(writer, sheet_name="weight", index=False)
marks_data_df.to_excel(writer, sheet_name="marks", index=False)

writer.close()
