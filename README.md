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

![Daily Tracker](https://github.com/user-attachments/assets/addb9baa-a1ec-4f40-89de-675f847648fb)

---

### 📊 Financial Calculators

1. **📅 SIP Calculator**
   - Calculate future value of monthly SIPs based on tenure and CAGR.

2. **🎓 Children's Future Planning**
   - Estimate future corpus needed for a child's education using inflation and ROI.

3. **🏠 Affordability Calculator**
   - Check eligibility for home/vehicle loans based on income and investment assets.

4. **💸 Tax Calculator**
   - Calculates taxable income and tax after Section 80C and other deductions.

![Tax Calculator](https://github.com/user-attachments/assets/e8a5f183-101e-4eb6-b28d-718b1c755a13)

---

### 📈 Investment & Savings Tools

- View **company fundamentals** and **technical analysis** (support/resistance).
- Check **quarterly reports**, **P&L**, and **stock trends**.
- Suggestions for **pension plans** and **equity-based savings**.

![Stock Analysis](https://github.com/user-attachments/assets/e242481d-4709-4b95-9c58-4ec02e53ab3e)

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

Live on **Render**: [App Link](https://spendsmart-9oph.onrender.com)

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
📦 spendsmart
│
├── static/                # CSS & images
├── templates/             # HTML templates
├── utils/                 # Helper functions
├── app.py                 # Flask entry point
├── forms.py               # Flask-WTF forms
├── render.yaml            # Render deployment config
├── requirements.txt       # Python packages
├── Procfile               # Deployment start command
└── README.md
```

---

## 🤝 Contributors

- [Ambar Mistry](https://github.com/Ambar1533)

---

## 📃 License

This project is licensed under the MIT License.

---

> SmartSpend: Helping you spend smarter, save better, and invest wiser.
---

## 🚀 Live Demo

You can access the deployed app here: [SmartSpend on Render](https://spendsmart-9oph.onrender.com)

---

## 📦 Tech Stack

- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Backend**: Python 3.11, Flask, Flask-WTF
- **Database**: JSON-based storage (extensible to SQL/NoSQL)
- **Tools**: Chart.js, Gunicorn, Render for Deployment

---

## 📂 Folder Structure

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
   ```
   git clone https://github.com/Ambar1533/spendsmart
   cd spendsmart
   ```

2. Create virtual environment and activate:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```
   python app.py
   ```

5. Access the app at:
   ```
   http://127.0.0.1:8000/
   ```

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Chart.js](https://www.chartjs.org/)
- [Render](https://render.com/)
- [email-validator](https://pypi.org/project/email-validator/)
