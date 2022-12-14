#!/usr/bin/python3
# Author: Oladapo Okikiola
print("""
Author: Oladapo Okikiola\n
Description: A applicant named:\n1. "Vitality" or "Okikiola" has no criminal recored, has high income and good_credit\nHe is very eligible for loan\n\n2. "daniel" has no criminal record and high income but has good_credit\nHe is therefore eligible for the loan\n\n3. "richy" has criminal record, high income, but no good credit\nHe is therefore Certainly not eligible for the loan\n\nAny other user is not eligible for the loan
""")
User = input("Enter your loanee name: ")
if User == "Vitality" or User == "Okikiola":
    good_credit = True
    high_income = True
    criminal_record = False
elif User == "daniel":
    criminal_record = False
    high_income = False
    good_credit = True
elif User == "richy":
    high_income = True
    good_credit = False
    criminal_record = True
else:
    good_credit = None
    high_income = None
    criminal_record = None
if criminal_record == False and (good_credit == True and high_income  == True):
    print("Very eligible for loan")
elif criminal_record == False and (good_credit == True or high_income == True):
    print("eligible for loan")
elif criminal_record == True and (good_credit == False and high_income == True):
    print("Certainly not available for loan")
else:
    print("Not eligible for loan")
