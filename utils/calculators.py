# Financial calculator utility functions
def calculate_home_loan_emi(loan_amount, annual_interest_rate, tenure_years):
    """Calculate EMI for home loan"""
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_months = tenure_years * 12
    if monthly_interest_rate == 0:
        return loan_amount / total_months
    emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months) / ((1 + monthly_interest_rate) ** total_months - 1)
    return emi

def calculate_total_liquid_assets(cash, bonds, gold, mutual_funds, stocks):
    """Calculate total liquid assets"""
    return cash + bonds + gold + mutual_funds + stocks

def calculate_total_expenses(housing, transportation, utilities, groceries, medical, dining, shopping, insurance_premiums, child_education, maid, miscellaneous, home_loan, car_loan, personal_loan, other_loans):
    """Calculate total expenses breakdown"""
    total_living_expense = housing + transportation + utilities + groceries + medical
    total_lifestyle_expense = dining + shopping
    total_other_expenses = insurance_premiums + child_education + maid + miscellaneous
    total_emis = home_loan + car_loan + personal_loan + other_loans
    total_expenses = total_living_expense + total_lifestyle_expense + total_other_expenses + total_emis
    return total_expenses, total_living_expense, total_lifestyle_expense, total_other_expenses, total_emis

def calculate_savings(total_income, total_expenses):
    """Calculate savings from income and expenses"""
    return total_income - total_expenses

def calculate_sip(corpus_goal, annual_return_rate, investment_period_months):
    """Calculate SIP amount needed for corpus goal"""
    monthly_return_rate = (1 + annual_return_rate) ** (1 / 12) - 1
    if monthly_return_rate == 0:
        return corpus_goal / investment_period_months
    sip = corpus_goal * monthly_return_rate / (((1 + monthly_return_rate) ** investment_period_months - 1) / monthly_return_rate)
    return sip

def calculate_corpus(sip, annual_return_rate, investment_period_months):
    """Calculate corpus from SIP amount"""
    monthly_return_rate = (1 + annual_return_rate) ** (1 / 12) - 1
    if monthly_return_rate == 0:
        return sip * investment_period_months
    corpus = sip * (((1 + monthly_return_rate) ** investment_period_months - 1) / monthly_return_rate) * (1 + monthly_return_rate)
    return corpus

def calculate_future_values(present_age, current_cost, inflation_rate, goal_age, roi, initial_lump_sum):
    """Calculate future values for children's future planning"""
    years_to_goal = goal_age - present_age
    future_cost = current_cost * (1 + inflation_rate / 100) ** years_to_goal

    if initial_lump_sum > 0:
        corpus_required = future_cost - initial_lump_sum * (1 + roi / 100) ** years_to_goal
    else:
        corpus_required = future_cost

    if corpus_required < 0:
        corpus_required = 0

    if roi == 0:
        monthly_investment = corpus_required / (years_to_goal * 12)
        lump_sum_investment = corpus_required
    else:
        monthly_investment = corpus_required / ((1 + roi / 100 / 12) ** (years_to_goal * 12) - 1) * (roi / 100 / 12)
        lump_sum_investment = corpus_required / (1 + roi / 100) ** years_to_goal
    
    annual_investment = monthly_investment * 12

    return {
        'corpus_required': round(corpus_required, 2),
        'monthly_investment': round(monthly_investment, 2),
        'annual_investment': round(annual_investment, 2),
        'lump_sum_investment': round(lump_sum_investment, 2)
    }

def calculate_tax(income, deductions):
    """Calculate income tax based on Indian tax slabs"""
    # Apply deductions
    taxable_income = income - deductions
    
    # Tax calculation based on Indian tax slabs
    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = (taxable_income - 600000) * 0.1 + 300000 * 0.05
    elif taxable_income <= 1200000:
        tax = (taxable_income - 900000) * 0.15 + 300000 * 0.1 + 300000 * 0.05
    elif taxable_income <= 1500000:
        tax = (taxable_income - 1200000) * 0.2 + 300000 * 0.15 + 300000 * 0.1 + 300000 * 0.05
    else:
        tax = (taxable_income - 1500000) * 0.3 + 300000 * 0.2 + 300000 * 0.15 + 300000 * 0.1 + 300000 * 0.05
    
    # Add 4% cess
    tax = tax + tax * 0.04
    return tax, taxable_income