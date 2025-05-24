##forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange, Length, Optional

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

class TaxForm(FlaskForm):
    income = FloatField('Annual Income', validators=[DataRequired(), NumberRange(min=0)])
    deduction_80c = FloatField('Section 80C', validators=[Optional()], default=0)
    deduction_80ccc = FloatField('Section 80CCC', validators=[Optional()], default=0)
    deduction_80ccd1 = FloatField('Section 80CCD(1)', validators=[Optional()], default=0)
    deduction_80ccd1b = FloatField('Section 80CCD(1B)', validators=[Optional()], default=0)
    deduction_80ccd2 = FloatField('Section 80CCD(2)', validators=[Optional()], default=0)
    deduction_80d = FloatField('Section 80D', validators=[Optional()], default=0)
    deduction_80dd = FloatField('Section 80DD', validators=[Optional()], default=0)
    deduction_80ddb = FloatField('Section 80DDB', validators=[Optional()], default=0)
    deduction_80e = FloatField('Section 80E', validators=[Optional()], default=0)
    deduction_80ee = FloatField('Section 80EE', validators=[Optional()], default=0)
    deduction_80g = FloatField('Section 80G', validators=[Optional()], default=0)
    deduction_80gg = FloatField('Section 80GG', validators=[Optional()], default=0)
    deduction_80gga = FloatField('Section 80GGA', validators=[Optional()], default=0)
    deduction_80ggc = FloatField('Section 80GGC', validators=[Optional()], default=0)
    deduction_80u = FloatField('Section 80U', validators=[Optional()], default=0)
    submit = SubmitField('Calculate Tax')

class HomeLoanForm(FlaskForm):
    cost_of_property = FloatField('Cost of Property (₹)', validators=[DataRequired(), NumberRange(min=0)])
    down_payment = FloatField('Down Payment (₹)', validators=[DataRequired(), NumberRange(min=0)])
    loan_amount = FloatField('Loan Amount (₹)', validators=[DataRequired(), NumberRange(min=0)])
    annual_interest_rate = FloatField('Annual Interest Rate (%)', validators=[DataRequired(), NumberRange(min=0)])
    tenure_years = IntegerField('Tenure (Years)', validators=[DataRequired(), NumberRange(min=1)])
    cost_of_registration = FloatField('Cost of Registration (₹)', validators=[DataRequired(), NumberRange(min=0)])
    cash_in_bank_accounts = FloatField('Cash in Bank Accounts (₹)', validators=[DataRequired(), NumberRange(min=0)])
    bonds = FloatField('Value of Bonds (₹)', validators=[DataRequired(), NumberRange(min=0)])
    gold = FloatField('Value of Gold (₹)', validators=[DataRequired(), NumberRange(min=0)])
    mutual_funds = FloatField('Value of Mutual Funds (₹)', validators=[DataRequired(), NumberRange(min=0)])
    stocks = FloatField('Value of Stocks (₹)', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Calculate EMI')

class SipForm(FlaskForm):
    sip_amount = FloatField('Monthly SIP Amount (₹)', validators=[DataRequired(), NumberRange(min=1)])
    investment_period_months = IntegerField('Investment Period (Months)', validators=[DataRequired(), NumberRange(min=1)])
    annual_return_rate = FloatField('Expected Annual Return Rate (%)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Calculate Corpus')

class ChildrenFutureForm(FlaskForm):
    present_age = IntegerField('Present Age (Years)', validators=[DataRequired(), NumberRange(min=0)])
    goal_age = IntegerField('Goal Age (Years)', validators=[DataRequired(), NumberRange(min=0)])
    current_cost = FloatField('Current Cost (₹)', validators=[DataRequired(), NumberRange(min=0)])
    inflation_rate = FloatField('Expected Inflation Rate (%)', validators=[DataRequired(), NumberRange(min=0, max=50)])
    roi = FloatField('Expected ROI (%)', validators=[DataRequired(), NumberRange(min=0, max=50)])
    initial_lump_sum = FloatField('Initial Lump Sum Investment (₹)', validators=[Optional()], default=0)
    submit = SubmitField('Calculate Plan')
