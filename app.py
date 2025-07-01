from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/biodata')
def biodata():
    data = {
        'nama': 'Sirly Ziadatul Mustafidah',
        'umur': 21,
        'email': 'personalsirly@gmail.com',
        'alamat': 'Jl. Merpati No. 12, Jakarta',
        'pendidikan': 'S1 Informatika - Universitas Ahmad Dahlan',
        'pekerjaan': 'Mahasiswa & Freelancer',
        'skill': ['Python', 'Flask', 'TensorFlow', 'HTML/CSS', 'Figma']
    }
    return render_template('biodata.html', biodata=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)