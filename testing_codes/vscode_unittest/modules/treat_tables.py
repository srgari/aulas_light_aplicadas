def join_tables(part_of_table_name):
    """join_tables     
    """
    import pandas as pd 
    import os 
    
    list_files = os.listdir('input')
    
    selected_files = [
        file for file in list_files
        if part_of_table_name in file
    ]

    final_table = pd.DataFrame()
    # only return the first table
    for file in selected_files:
        df = pd.read_csv('input/' + file)
        final_table = final_table.append(df)
    return final_table