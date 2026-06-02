from flask import Flask, render_template

app = Flask(__name__)

def generate_daily_plan():
    """Generate an AI-powered daily plan"""
    return {
        "tasks": ["Finish project", "Exercise", "Read 30 min"],
        "focus_time": "4 hours",
        "ai_tip": "Take a break at 14:00"
    }

@app.route('/')
def index():
    """Main landing page with AI daily plan"""
    plan = generate_daily_plan()
    return render_template('index.html', plan=plan)

@app.route('/dashboard')
def dashboard():
    """User dashboard (placeholder for future development)"""
    plan = generate_daily_plan()
    return render_template('index.html', plan=plan)

if __name__ == '__main__':
    print('AI Productivity SaaS 2026 - Ready to help people get more done')
    app.run(debug=True)
