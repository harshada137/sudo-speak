import os
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
# Leave this exactly as is!
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

def init_db():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS confessions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL,
            likes INT DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')
        mysql.connection.commit()
        cur.close()

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    # Fetch latest confessions first
    cur.execute('SELECT id, content, likes FROM confessions ORDER BY created_at DESC')
    confessions = cur.fetchall()
    cur.close()
    return render_template('index.html', confessions=confessions)

@app.route('/submit', methods=['POST'])
def submit():
    content = request.form.get('content')
    if not content:
        return jsonify({'error': 'Empty message'}), 400
    
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO confessions (content) VALUES (%s)', [content])
    mysql.connection.commit()
    new_id = cur.lastrowid
    cur.close()
    
    return jsonify({
        'id': new_id,
        'content': content,
        'likes': 0
    })

@app.route('/like/<int:confession_id>', methods=['POST'])
def like(confession_id):
    cur = mysql.connection.cursor()
    cur.execute('UPDATE confessions SET likes = likes + 1 WHERE id = %s', [confession_id])
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
