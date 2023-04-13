from flask import Flask, request, render_template, url_for
import pyqrcode

app = Flask(__name__,template_folder='templates')   #initiating flask

@app.route('/')        #calling index.html
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])   #calling python to perform request
def generate():                            #initiating generation process
    Data = request.form['data']            #requesting data from user in form of text
    filename = request.form['filename']  # Get filename from user input
    GeneratedQr = pyqrcode.create(Data)     #Qr is generated
    GeneratedQr.png(f'static/{filename}.png', scale=8)    #qr is saved in static folder in css, so that an image link is created
    return render_template('result.html', filename=filename) #calling result.html

if __name__ == '__main__':
    app.run(debug=True)
