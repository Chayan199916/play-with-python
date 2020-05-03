from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])
def success():
    global file
    if request.method == 'POST':
        file = request.files['chosen-file']
        with open(secure_filename('uploaded_' + file.filename), 'wb') as f:
            f.write(file.read())
        with open('uploaded_' + file.filename, 'a') as f:
            f.write("\nThis was added later")
        return render_template('index.html', dw_btn = "download.html")
 
@app.route('/download')
def download():
    return send_file('uploaded_' + file.filename, attachment_filename='yourfile.csv', as_attachment=True)

if __name__ == "__main__":
    app.debug = True
    app.run()