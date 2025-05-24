# 💰 SmartSpend: Personal Finance & Investment Manager

**SmartSpend** is a full-stack **Flask-based web application** that helps users track their expenses, calculate financial metrics, and manage savings & investments — all in one place.

![SmartSpend Dashboard](https://github.com/user-attachments/assets/2a0428d8-d87c-4492-809a-0a47cc8dc438)

---

## 🚀 Features

### 🧾 Expense Tracker
- Track **daily and monthly** expenses.
- Categorize spending: accommodation, groceries, transportation, etc.
- Visualize trends with interactive **bar graphs** and **pie charts**.
- Analyze **ideal vs actual** spending.

![Daily Expense Entry](https://github.com/user-attachments/assets/addb9baa-a1ec-4f40-89de-675f847648fb)
![Expense Graph](https://github.com/user-attachments/assets/4720f14a-2628-43ae-8f83-12336e1304e7)

---

### 📊 Financial Calculators

1. **📅 SIP Calculator**
   - Calculate future value of monthly SIPs based on tenure and CAGR.
   - ![SIP Calculator](https://github.com/user-attachments/assets/f637e9d5-8264-4807-beac-3ff386a0371f)

2. **🎓 Children's Future Planning**
   - Estimate future corpus needed for a child's education using inflation and ROI.
   - ![Children Planning](https://github.com/user-attachments/assets/5f9ad810-dace-4e4d-80b6-a7ca0296f98f)

3. **🏠 Affordability Calculator**
   - Check eligibility for home/vehicle loans based on income and investment assets.
   - ![Loan Input](https://github.com/user-attachments/assets/5d644a47-a91c-4e1d-8d88-b4a36f88f749)
   - ![Loan EMI Output](https://github.com/user-attachments/assets/e457ceb3-b76f-4bdd-91c2-f706839fc567)

4. **💸 Tax Calculator**
   - Calculates taxable income and tax after Section 80C and other deductions.
   - ![Tax Form](https://github.com/user-attachments/assets/e8a5f183-101e-4eb6-b28d-718b1c755a13)
   - ![Tax Output](https://github.com/user-attachments/assets/04be6aaf-189e-4adb-951b-60ea828d5cbf)

---

### 📈 Investment & Savings Tools

- View **company fundamentals** and **technical analysis** (support/resistance).
- Check **quarterly reports**, **P&L**, and **stock trends**.
- Suggestions for **pension plans** and **equity-based savings**.

![Stock Analysis](https://github.com/user-attachments/assets/e242481d-4709-4b95-9c58-4ec02e53ab3e)
![Quarterly Report](https://github.com/user-attachments/assets/0dc3a879-5ace-4846-98df-a7b187b9119f)
![Technical Analysis](https://github.com/user-attachments/assets/f849101f-30f8-45f1-ad99-749b64b7283d)

---

## 🔐 Authentication & User Flow

- **User Registration & Login** for secure access.
- Personalized dashboard based on user input.

---

## 🛠️ Tech Stack

| Layer       | Technologies                 |
|-------------|------------------------------|
| Frontend    | HTML, CSS, JavaScript        |
| Backend     | Python, Flask, Jinja2        |
| Database    | JSON-based user data storage |
| Deployment  | Render                       |
| Charts      | Chart.js                     |

---

## 🚀 Deployment

Live on **Render**: [SmartSpend App](https://spendsmart-9oph.onrender.com)

> To deploy manually:
```bash
git clone https://github.com/Ambar1533/spendsmart.git
cd spendsmart
pip install -r requirements.txt
python app.py
```

---

## 📁 Folder Structure

```
SMARTSPEND-MAIN/
├── static/               # CSS, images
├── templates/            # HTML templates
├── utils/                # Calculation logic
├── app.py                # Main application file
├── forms.py              # Flask-WTF form classes
├── requirements.txt      # Python dependencies
├── render.yaml           # Render deployment config
├── Procfile              # Gunicorn launch command
├── runtime.txt           # Python runtime for Render
└── README.md             # Project documentation
```

---

## 🧪 Testing Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Ambar1533/spendsmart
   cd spendsmart
   ```

2. Create virtual environment and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Access the app at:
   ```bash
   http://127.0.0.1:8000/
   ```

---

## 🙌 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Chart.js](https://www.chartjs.org/)
- [Render](https://render.com/)
- [email-validator](https://pypi.org/project/email-validator/)

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

> SmartSpend: Helping you spend smarter, save better, and invest wiser.