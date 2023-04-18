import os
import pandas as pd
from BMI_Healthy_Carmen import BMI_Healthy_Carmen
from functions_merge import write_excel


if __name__ == '__main__':

    # 14-04-2023 Carmen request
    path_in = r'L:\KKM_LuFu\OfficeData\Biomedical Engineers\Lea\04.Data Management\140423_BMI_Healthy_Carmen'
    path_out = path_in

    tablePatsCarmen_in = pd.read_excel(os.path.join(path_in, r'for_Lea.xlsx'))
    tableNamesUID_in = pd.read_excel(os.path.join(path_in, r'tabPatNames.xlsx'))
    tableCRF_in = pd.read_excel(os.path.join(path_in, r'tabFU_CRF.xlsx'))
    tableCRFSpiro_in = pd.read_excel(os.path.join(path_in, r'tabFU_CRF_Spiro.xlsx'))

    table_out = BMI_Healthy_Carmen(tablePatsCarmen_in, tableNamesUID_in, tableCRF_in, tableCRFSpiro_in)
    write_excel(table_out, path_out, 'merged_Pats_BMI_Spiro')

