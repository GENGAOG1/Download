from flask import Flask, send_file, redirect, url_for
import os

app = Flask(__name__)

DATEIEN = ['holy_pc_crash.py', 'random.py']
DOWNLOAD_COUNT = 0

@app.route('/')
def index():
    global DOWNLOAD_COUNT
    DOWNLOAD_COUNT = 0  # Zurücksetzen
    return redirect(url_for('download_first'))

@app.route('/download')
def download_first():
    global DOWNLOAD_COUNT
    DOWNLOAD_COUNT = 1
    
    datei = DATEIEN[0]
    
    if not os.path.exists(datei):
        return "Datei nicht gefunden!", 404
    
    response = send_file(datei, as_attachment=True, download_name=datei, mimetype='application/octet-stream')
    response.headers['Refresh'] = '0.5; url=/visit'
    return response

@app.route('/visit')
def download_second():
    global DOWNLOAD_COUNT
    
    if DOWNLOAD_COUNT != 1:
        return "Bereits heruntergeladen!", 200
    
    datei = DATEIEN[1]
    
    if not os.path.exists(datei):
        return "Datei nicht gefunden!", 404
    
    DOWNLOAD_COUNT = 2  # Markieren als fertig
    
    response = send_file(datei, as_attachment=True, download_name=datei, mimetype='application/octet-stream')
    response.headers['Refresh'] = '0.5; url=/fertig'
    return response

@app.route('/fertig')
def fertig():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Fertig!</title></head>
    <body>
        <h1>✅ Downloads abgeschlossen!</h1>
        <p>Beide Dateien wurden erfolgreich heruntergeladen.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
