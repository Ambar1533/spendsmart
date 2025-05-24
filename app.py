import flask
import json
import os
import secrets
from flask import session, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash

# Import utility functions
from utils.calculators import (
    calculate_home_loan_emi, calculate_total_liquid_assets,
    calculate_total_expenses, calculate_savings,
    calculate_sip, calculate_corpus, calculate_future_values,
    calculate_tax
)

# Import forms
from forms import LoginForm, RegisterForm, TaxForm, HomeLoanForm, SipForm, ChildrenFutureForm

app = flask.Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate secure secret key

# Initialize CSRF Protection
csrf = CSRFProtect(app)

# Data file path
USER_DATA_FILE = 'user_data.json'

# Helper functions for data management
def load_user_data():
    """Load user data from JSON file"""
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_user_data(data):
    """Save user data to JSON file"""
    try:
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except IOError:
        return False

def get_current_user():
    """Get current logged-in user from session"""
    return session.get('user_email')

def is_user_authenticated(user_email):
    """Check if user is authenticated and exists"""
    current_user = get_current_user()
    return current_user == user_email and current_user is not None

# Routes
@app.route('/')
def index():
    """Index page"""
    form = LoginForm()
    return flask.render_template('index.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data.strip()
        password = form.password.data

        user_data = load_user_data()

        if email in user_data:
            flash('User already exists', 'error')
            return flask.render_template('register.html', form=form, data=0)

        hashed_password = generate_password_hash(password)
        user_data[email] = {
            "password": hashed_password,
            "created_at": flask.datetime.datetime.now().isoformat()
        }

        if save_user_data(user_data):
            flash('Registration successful! Please login.', 'success')
            return flask.redirect('/')
        else:
            flash('Registration failed. Please try again.', 'error')

    return flask.render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Handle user login with CSRF protection"""
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data.strip()
        password = form.password.data
        
        user_data = load_user_data()
        
        if not user_data:
            flash('No users registered', 'error')
            return flask.render_template('index.html', form=form, data=4)
        
        if email in user_data:
            if check_password_hash(user_data[email]['password'], password):
                session['user_email'] = email
                flash('Login successful', 'success')
                return flask.redirect(f'{email}/home')
            else:
                flash('Invalid password', 'error')
                return flask.render_template('index.html', form=form, data=2)
        else:
            flash('User not found', 'error')
            return flask.render_template('index.html', form=form, data=3)
    
    # Handle form validation errors
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return flask.render_template('index.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle user registration with validation"""
    form = RegisterForm()
    
    if form.validate_on_submit():
        email = form.email.data.strip()
        password = form.password.data
        
        user_data = load_user_data()
        
        # Check if user already exists
        if email in user_data:
            flash('User already exists', 'error')
            return flask.render_template('register.html', form=form, data=0)
        
        # Hash password and save user
        hashed_password = generate_password_hash(password)
        user_data[email] = {
            "password": hashed_password,
            "created_at": flask.datetime.datetime.now().isoformat()
        }
        
        if save_user_data(user_data):
            flash('Registration successful! Please login.', 'success')
            return flask.redirect('/')
        else:
            flash('Registration failed. Please try again.', 'error')
            return flask.render_template('register.html', form=form, data=1)
    
    # Handle form validation errors
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return flask.render_template('register.html', form=form)

@app.route('/logout')
def logout():
    """Handle user logout"""
    session.clear()
    flash('You have been logged out', 'info')
    return flask.redirect('/')

@app.route('/profile')
def profile():
    """Profile page"""
    if not get_current_user():
        flash('Please login to access your profile', 'error')
        return flask.redirect('/')
    return flask.render_template('profile.html')

@app.route('/display')
def display():
    """Display page"""
    return flask.render_template('display.html')

@app.route('/<id>/home')
def home(id):
    """User home page"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    user_data = load_user_data()
    if id in user_data:
        return flask.render_template('home.html', data=[id])
    else:
        return flask.render_template('404Error.html')

@app.route('/<id>/expense-tracker')
def expense_tracker(id):
    """Expense tracker page"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    user_data = load_user_data()
    if id in user_data:
        return flask.render_template('expense_tracker.html', data=[id])
    else:
        return flask.render_template('404Error.html')

@app.route('/<id>/financial-calculators')
def financial_calculators(id):
    """Financial calculators page"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    user_data = load_user_data()
    if id in user_data:
        return flask.render_template('finanial_cal.html', data=[id])
    else:
        return flask.render_template('404Error.html')

@app.route('/<id>/daily', methods=['GET', 'POST'])
def daily_expense(id):
    """Handle daily expense tracking"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    if flask.request.method == 'POST':
        purpose = flask.request.form.get('purpose', '').strip()
        date = flask.request.form.get('date', '')
        amount = flask.request.form.get('amount', '')
        
        # Validation
        if not purpose or not date or not amount:
            flash('All fields are required', 'error')
            return flask.render_template('daily.html', data=[id])
        
        try:
            amount_float = float(amount)
            if amount_float <= 0:
                flash('Amount must be positive', 'error')
                return flask.render_template('daily.html', data=[id])
        except ValueError:
            flash('Invalid amount format', 'error')
            return flask.render_template('daily.html', data=[id])
        
        user_data = load_user_data()
        
        if id in user_data:
            if 'expense_tracker' in user_data[id]:
                user_data[id]['expense_tracker'].append([date, purpose, amount])
            else:
                user_data[id]['expense_tracker'] = [[date, purpose, amount]]
            
            if save_user_data(user_data):
                flash('Expense added successfully', 'success')
            else:
                flash('Failed to save expense', 'error')
            
            return flask.render_template('daily.html', data=[id])
    
    user_data = load_user_data()
    if id in user_data:
        return flask.render_template('daily.html', data=[id])
    else:
        return flask.render_template('404Error.html')

@app.route('/<id>/monthly', methods=['GET', 'POST'])
def monthly_expense(id):
    """Handle monthly expense view"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    user_data = load_user_data()
    if id in user_data:
        if 'expense_tracker' in user_data[id]:
            expenses = user_data[id]['expense_tracker']
            total = 0
            for expense in expenses:
                try:
                    total += float(expense[2])
                except (ValueError, IndexError):
                    continue
            
            chart_values = []
            for expense in expenses:
                try:
                    if total > 0:
                        percentage = (float(expense[2]) / total) * 100
                        chart_values.append(round(percentage, 2))
                    else:
                        chart_values.append(0)
                except (ValueError, IndexError):
                    chart_values.append(0)
            
            return flask.render_template('monthly.html', data=[expenses, total, chart_values, id])
        else:
            return flask.render_template('monthly.html', data=[[], 0, [], id])
    
    return flask.render_template('404.html')

@app.route('/<id>/tax-calculator', methods=['GET', 'POST'])
def tax_calculator(id):
    """Handle tax calculation"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    form = TaxForm()
    
    if form.validate_on_submit():
        try:
            original_income = form.income.data
            
            # Get all deduction values from form
            deductions = {
                'deduction_80c': form.deduction_80c.data or 0,
                'deduction_80ccc': form.deduction_80ccc.data or 0,
                'deduction_80ccd1': form.deduction_80ccd1.data or 0,
                'deduction_80ccd1b': form.deduction_80ccd1b.data or 0,
                'deduction_80ccd2': form.deduction_80ccd2.data or 0,
                'deduction_80d': form.deduction_80d.data or 0,
                'deduction_80dd': form.deduction_80dd.data or 0,
                'deduction_80ddb': form.deduction_80ddb.data or 0,
                'deduction_80e': form.deduction_80e.data or 0,
                'deduction_80ee': form.deduction_80ee.data or 0,
                'deduction_80g': form.deduction_80g.data or 0,
                'deduction_80gg': form.deduction_80gg.data or 0,
                'deduction_80gga': form.deduction_80gga.data or 0,
                'deduction_80ggc': form.deduction_80ggc.data or 0,
                'deduction_80u': form.deduction_80u.data or 0
            }
            
            # Calculate total deductions with limits
            section_80c_total = min(
                deductions['deduction_80c'] + deductions['deduction_80ccc'] + deductions['deduction_80ccd1'], 
                150000
            )
            section_80ccd1b_total = min(deductions['deduction_80ccd1b'], 50000)
            section_80ccd2_total = deductions['deduction_80ccd2']  # No limit
            other_deductions = min(
                deductions['deduction_80d'] + deductions['deduction_80dd'] + deductions['deduction_80ddb'] + 
                deductions['deduction_80e'] + deductions['deduction_80ee'] + deductions['deduction_80g'] + 
                deductions['deduction_80gg'] + deductions['deduction_80gga'] + deductions['deduction_80ggc'] + 
                deductions['deduction_80u'], 
                200000
            )
            
            total_deductions = (section_80c_total + section_80ccd1b_total + 
                              section_80ccd2_total + other_deductions)
            
            tax, taxable_income = calculate_tax(original_income, total_deductions)
            
            return flask.render_template('tax_output.html', 
                                       data=[original_income, tax, taxable_income, total_deductions, 1])
        
        except Exception as e:
            flash('Error processing tax calculation. Please check your inputs.', 'error')
    
    # Handle form validation errors
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return flask.render_template('tax.html', form=form, data=[0])

@app.route('/<id>/affordability-calculator', methods=['GET', 'POST'])
def affordability_calculator(id):
    """Handle home loan affordability calculation"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    form = HomeLoanForm()
    
    if form.validate_on_submit():
        try:
            data = {
                'cost_of_property': form.cost_of_property.data,
                'down_payment': form.down_payment.data,
                'loan_amount': form.loan_amount.data,
                'annual_interest_rate': form.annual_interest_rate.data,
                'tenure_years': form.tenure_years.data,
                'cost_of_registration': form.cost_of_registration.data,
                'cash_in_bank_accounts': form.cash_in_bank_accounts.data,
                'bonds': form.bonds.data,
                'gold': form.gold.data,
                'mutual_funds': form.mutual_funds.data,
                'stocks': form.stocks.data
            }
            
            # Additional business logic validation
            if data['annual_interest_rate'] > 100:
                flash('Interest rate seems too high. Please check.', 'error')
                return flask.render_template('home_loan.html', form=form)
            
            data['EMI'] = calculate_home_loan_emi(
                data['loan_amount'], 
                data['annual_interest_rate'], 
                data['tenure_years']
            )
            data['total_liquid_assets'] = calculate_total_liquid_assets(
                data['cash_in_bank_accounts'], data['bonds'], 
                data['gold'], data['mutual_funds'], data['stocks']
            )
            
            return flask.render_template('home_loanoutput.html', data=data)
        
        except Exception as e:
            flash('Error processing loan calculation. Please check your inputs.', 'error')
    
    # Handle form validation errors
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return flask.render_template('home_loan.html', form=form)

@app.route('/<id>/sip-calculator', methods=['GET', 'POST'])
def sip_calculator(id):
    """Handle SIP calculation with form validation"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    form = SipForm()
    
    if form.validate_on_submit():
        try:
            data = {
                'sip_amount': form.sip_amount.data,
                'investment_period_months': form.investment_period_months.data,
                'annual_return_rate': form.annual_return_rate.data / 100  # Convert percentage to decimal
            }

            corpus = calculate_corpus(
                data['sip_amount'], 
                data['annual_return_rate'], 
                data['investment_period_months']
            )
            
            result_data = {
                'sip_amount': data['sip_amount'],
                'investment_period_months': data['investment_period_months'],
                'annual_return_rate': form.annual_return_rate.data,  # Keep original percentage for display
                'corpus': corpus
            }
            
            return flask.render_template('sip_output.html', data=result_data)
        
        except Exception as e:
            flash('Error processing SIP calculation. Please check your inputs.', 'error')
    
    # Handle form validation errors
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    
    return flask.render_template('sip_calculator.html', form=form)

@app.route('/<id>/children-future-planning', methods=['GET', 'POST'])
def children_future_planning(id):
    """Handle children's future planning calculation with form validation"""
    if not is_user_authenticated(id):
        flash('Access denied', 'error')
        return flask.render_template('404Error.html')
    
    form = ChildrenFutureForm()
    
    if form.validate_on_submit():
        try:
            # Additional business logic validation
            if form.present_age.data >= form.goal_age.data:
                flash('Goal age must be greater than present age', 'error')
                return flask.render_template('children_fut.html', form=form)
            
            data = {
                'present_age': form.present_age.data,
                'goal_age': form.goal_age.data,
                'current_cost': form.current_cost.data,
                'inflation_rate': form.inflation_rate.data,
                'roi': form.roi.data,
                'initial_lump_sum': form.initial_lump_sum.data or 0
            }

            results = calculate_future_values(
                data['present_age'],
                data['current_cost'],
                data['inflation_rate'],
                data['goal_age'],
                data['roi'],
                data['initial_lump_sum']
            )

            return flask.render_template('children_fut_op.html', data=results)
        
        except Exception as e:
            flash('Error processing future planning calculation. Please check your inputs.', 'error')
    
    # Handle form validation errors
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')

    return flask.render_template('children_fut.html', form=form)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return flask.render_template('404Error.html'), 404

@app.errorhandler(500)
def internal_error(error):
    flash('An internal error occurred. Please try again later.', 'error')
    return flask.render_template('index.html'), 500

# Import datetime for user creation timestamp
import datetime
flask.datetime = datetime

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', debug=True)