
from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import SaleData
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Medicle Insurance Charges Prediction")
    return render_template("index.html")


@app.route('/credit', methods = ["POST"])
def get_credit():

    print("We are using POST Method")

    purpose = request.form.get("purpose")
    int_rate = eval(request.form.get("int_rate"))
    installment = eval(request.form.get("installment"))
    log_annual_inc = eval(request.form.get("log_annual_inc"))
    dti = eval(request.form.get("dti"))
    fico = eval(request.form.get("fico"))
    days_with_cr_line = eval(request.form.get("days_with_cr_line"))
    revol_bal = eval(request.form.get("revol_bal"))
    revol_util = eval(request.form.get("revol_util"))
    inq_last_6mths = eval(request.form.get("inq_last_6mths"))
    delinq_2yrs = eval(request.form.get("delinq_2yrs"))
    pub_rec = eval(request.form.get("pub_rec")) 
    not_fully_paid = eval(request.form.get("not_fully_paid"))   

    print("purpose, int_rate, installment, log_annual_inc, dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid\n",
    purpose, int_rate, installment, log_annual_inc, dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid)

    credobj = SaleData(purpose, int_rate, installment, log_annual_inc, dti,fico,days_with_cr_line,revol_bal,revol_util,
    inq_last_6mths,delinq_2yrs,pub_rec,not_fully_paid)
    policy = credobj.get_credit_policy()

    return render_template("index.html", prediction = policy)
       


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config.PORT_NUMBER, debug=True)