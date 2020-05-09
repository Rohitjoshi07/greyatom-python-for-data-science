# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here

bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var =bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode(axis=0)
for i in banks.columns:
    a= list(bank_mode[i])
    print(a)
    banks[i].fillna(a[0],inplace=True)
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here
avg_loan_amount =  pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean') #it can print the average loan amount for every category of index like female,not maried,unemplyed.




# code ends here



# --------------
# code starts here

loan_approved_se = len(banks[banks['Self_Employed']=='Yes'][banks['Loan_Status']=='Y']['Self_Employed'])

loan_approved_nse = len(banks[banks['Self_Employed']=='No'][banks['Loan_Status']=='Y']['Self_Employed'])

Loan_Status =614


percentage_se = loan_approved_se * 100 /Loan_Status
percentage_nse = loan_approved_nse * 100 /Loan_Status
# code ends here



# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term =0
for i in loan_term:
    if i>=25:
        big_loan_term +=1

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values=loan_groupby.mean()
print(mean_values)


# code ends here


