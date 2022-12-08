
import pickle
import json
import pandas as pd
import numpy as np
import config

class SaleData():
    def __init__(self, purpose, int_rate, installment, log_annual_inc, dti,
     fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid):
        self.purpose = purpose
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico =  fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        
        self.inq_last_6mths = inq_last_6mths
        self.delinq_2yrs =  delinq_2yrs
        self.pub_rec = pub_rec
        self.not_fully_paid =  not_fully_paid

    def load_model(self):
        with open(config.MODEL_FILE, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_credit_policy(self):

        self.load_model()       

    
        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.json_data["purpose_values"][self.purpose]
        array[1] = self.int_rate
        array[2] = self.installment
        array[3] = self.log_annual_inc
        array[4] = self.dti
        array[5] = self.fico
        array[6] = self.days_with_cr_line
        array[7] = self.revol_bal
        array[8] = self.revol_util
        array[9] = self.inq_last_6mths
        array[10] = self.delinq_2yrs
        array[11] = self.pub_rec
        array[12] = self.not_fully_paid

        print("Test Array -->\n",array)
        credit_policy = self.model.predict([array])[0]
        if credit_policy == 1:
            return "[YES] You Will Be Eligible For The Credit Policy of Our Bank"
        else:
            return "[NO] You Will <NOT> Be Eligible For The Credit Policy Of Our Bank"


if __name__ == "__main__":
    purpose = "home_improvement"
    int_rate = 0.118900
    installment = 829.100000
    log_annual_inc = 11.350407
    dti = 19.480000
    fico = 737.000000
    days_with_cr_line = 5639.958333
    revol_bal = 28854.000000
    revol_util = 52.100000
    inq_last_6mths = 0.000000
    delinq_2yrs = 0.000000
    pub_rec = 0.000000
    not_fully_paid = 0.00000

    credobj = SaleData(purpose, int_rate, installment, log_annual_inc, dti,
     fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid)
    policy = credobj.get_credit_policy()
    print()
    print(f"credit policy ::::: {policy}")