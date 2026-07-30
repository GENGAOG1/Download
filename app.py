from flask import Flask, send_file
import os

app = Flask(__name__)

FILE_PATH1 = 'holy_pc_crash.py'   # Dateiname im Repo
FILE_PATH2 = 'random.py'
FILE_NAME = os.path.basename(FILE_PATH1)
FILE_NAME = os.path.basename(FILE_PATH2)

@app.route('/')
def forced_download():
    if not os.path.exists(FILE_PATH):
        return "Datei nicht gefunden auf dem Server!", 404
    
    return send_file(
        FILE_PATH1,
        FILE_PATH2,
        as_attachment=True,
        download_name=FILE_NAME,
        mimetype='application/octet-stream'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
