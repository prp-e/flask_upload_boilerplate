import os 
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__, static_folder='uploads')
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', filename=filename)

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)