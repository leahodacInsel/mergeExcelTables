import pandas as pd
import numpy as np
import datetime
from functions_merge import strip_df, datetime2date




def BMI_Healthy_Carmen(tablePatsCarmen_in, tableNamesUID_in, tableCRF_in, tableCRFSpiro_in):

    tablePatsCarmen_in = strip_df(tablePatsCarmen_in)
    tableNamesUID_in = strip_df(tableNamesUID_in)
    tableCRF_in = strip_df(tableCRF_in)
    tableCRFSpiro_in = strip_df(tableCRFSpiro_in)

    tablePatsCarmen_in = datetime2date(tablePatsCarmen_in)
    tableNamesUID_in = datetime2date(tableNamesUID_in)
    tableCRF_in = datetime2date(tableCRF_in)
    tableCRFSpiro_in = datetime2date(tableCRFSpiro_in)

    keys_CRFSpiro = tableCRFSpiro_in.keys()

    # link names in tablePats_in with UID in tableNames_in
    table_PatsUID = tablePatsCarmen_in.merge(tableNamesUID_in, how='left', left_on=['Name1', 'Name2'], right_on=['patNaSirName', 'patNaFirstName'])
    table_PatsUID = table_PatsUID[['Name1', 'Name2', 'patient_ID', 'date', 'DOB', 'sex', 'patNamesUID']]

    # link CRF with CRF_Spiro
    table_CRFSpiro = tableCRF_in.merge(tableCRFSpiro_in, how='left', left_on=['CRF_UID'], right_on=['FU_CRF_Spiro_UID'], indicator=True)


    table_out = table_PatsUID

    for idxPats, rowPats in table_PatsUID.iterrows():
        for idxCRF, rowCRF in table_CRFSpiro.iterrows():
            if type(rowCRF['CRF_ID_Sentry']) == str and type(rowPats['Name1']) == str and type(rowPats['date']) == datetime.date and type(rowCRF['CRF_Date']) == datetime.date:
                if (rowPats['Name1'].casefold() == rowCRF['CRF_ID_Sentry'].casefold() or rowPats['patNamesUID'] == rowCRF['CRF_UID']) and -15 < (rowPats['date']-rowCRF['CRF_Date']).days < 15:
                    table_out.at[idxPats, 'patNamesUID'] = rowPats['patNamesUID']
                    table_out.at[idxPats, 'CRF_Date'] = rowCRF['CRF_Date']
                    table_out.at[idxPats, 'delta_dates'] = (rowPats['date'] - rowCRF['CRF_Date']).days
                    # table_out.at[idxPats, 'CRF_Bepnek'] = rowBMI['CRF_ID_Sentry']
                    table_out.at[idxPats, 'CRF_Height'] = rowCRF['CRF_Height']
                    table_out.at[idxPats, 'CRF_Weight'] = rowCRF['CRF_Weight']

                    for key in keys_CRFSpiro:
                        table_out.at[idxPats, key] = rowCRF[key]

        if 'Bepnek' in rowPats['Name1']:
            # add UID from the 5 last Benpek ID caracters
            table_out.at[idxPats, 'patNamesUID'] = int(rowPats['Name1'][-5:])


    return table_out
