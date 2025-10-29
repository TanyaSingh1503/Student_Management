import pandas as pd

input_file = "data.xlsx" #input excel sheet which has to be segregated
df = pd.read_excel(input_file)


split_column = "College_Code"  # Replace with your exact column_name


output_file = "segregated_data.xlsx"  # New segregated file with multiple sheets of different colleges codes
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for code, group in df.groupby(split_column):
        sheet_name = str(code)[:31]  
        
        group.to_excel(writer, sheet_name=sheet_name, index=False)
        
print("✅ Data has been segregated successfully into multiple sheets!")
print(f"Output saved as: {output_file}")