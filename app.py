from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from io import BytesIO
import tempfile
import csv
import os 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'treyas19012024'

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # postgresql://treyas_user:MiO3siLFd4jS5CUTjE79840SZYszUfwZ@dpg-cmv6jc0l5elc73eckmlg-a.oregon-postgres.render.com/treyas
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

# Create the table if it doesn't exist
with app.app_context():
    db.create_all()

class FormSubmission:
    def submit_form(self, name, phone_number, email):
        new_form_data = FormData(name=name, phone_number=phone_number, email=email)
        db.session.add(new_form_data)
        db.session.commit()
        flash('Form submitted successfully!')
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/Technology training')
def Technology_training():
     
    return render_template('Technology_training.html')

@app.route('/Power BI')
def Power_BI():
  
    return render_template('Power_BI.html')

@app.route('/Tablue')
def Tablue():
    
    return render_template('Tablue.html')

@app.route('/SQL')
def SQL():
    
    return render_template('SQL.html')

@app.route('/Salesforce')
def Salesforce():
    
    return render_template('Salesforce.html')

@app.route('/Full stack development')
def Full_stack_development():
    
    return render_template('Full_stack_development.html')

@app.route('/Python')
def Python():
    
    return render_template('Python.html')

@app.route('/Product management courses')
def Product_management_courses():
    
    return render_template('Product_management_courses.html')

@app.route('/Product management and analytics')
def Product_management_and_analytics():
    
    return render_template('Product_management_and_analytics.html')

@app.route('/enroll')
def enroll():
    return render_template('enroll_now.html')

@app.route('/Agile methodologies training')
def Agile_methodologies_training():
    
    return render_template('Agile_methodologies_training.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        FormSubmission().submit_form(name, phone_number, email)
        return redirect(url_for('index'))
    else:
        # Handle other HTTP methods if needed
        flash('Invalid form submission.')
        return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'admin' and password == 'admin_password':
            form_data = FormData.query.all()

            # Create a temporary file
            temp_file, temp_filename = tempfile.mkstemp(suffix='.csv')

            with os.fdopen(temp_file, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                # Write header
                csv_writer.writerow(['ID', 'Name', 'Phone Number', 'Email'])

                # Write data rows
                for data in form_data:
                    csv_writer.writerow([data.id, data.name, data.phone_number, data.email])

            # Send CSV file for download
            return send_file(temp_filename, mimetype='text/csv', as_attachment=True, download_name='form_data.csv')

        else:
            flash('Invalid credentials. Please try again.')

    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
 