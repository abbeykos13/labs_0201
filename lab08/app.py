from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import apod_model

app = Flask(__name__)

@app.route('/')
def index():
    data = apod_model.get_apod()
    return render_template('index.html', apod=data)

@app.route('/history', methods=['GET', 'POST'])
def history():
    error = None
    apod_data = None
    if request.method == 'POST':
        date = request.form['date']
        try:
            
            if date > datetime.today().strftime('%Y-%m-%d') or date < "1995-06-16":
                error = "Please enter a valid date between 1995-06-16 and today."
            else:
                apod_data = apod_model.get_apod(date)
        except Exception as e:
            error = str(e)

    return render_template('history.html', apod=apod_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
