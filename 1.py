from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    jiji_page = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Jiji's Page</title>
        <style>
            body {
                font-family: 'Helvetica Neue', Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #4CAF50;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .profile img {
                width: 200px;
                height: 200px;
                border-radius: 50%;
                object-fit: cover;
                border: 5px solid #4CAF50;
                margin-bottom: 20px;
            }
            .info {
                text-align: left;
                margin: 0 auto;
                max-width: 600px;
            }
            .info p {
                font-size: 1.2em;
                line-height: 1.6;
                margin: 10px 0;
            }
            .info p span {
                font-weight: bold;
                color: #4CAF50;
            }
            footer {
                margin-top: 30px;
                font-size: 0.9em;
                color: #888;
            }
            .button {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 1.2em;
                color: #fff;
                background-color: #4CAF50;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                text-decoration: none;
            }
            .button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Jiji's Page</h1>
            <div class="profile">
                <img src="{{ url_for('static', filename='cat-placeholder.jpg') }}" alt="Jiji's Picture">
            </div>
            <div class="info">
                <p><span>Name:</span> Jiji</p>
                <p><span>Age:</span> 3 months</p>
                <p><span>Personality:</span> Jiji is a curious and affectionate kitten. He loves to sleep, eat, cuddle, and explore. His favorite food is wet food.</p>
                <p><span>Unique Trait:</span> Jiji has a distinctive white bit on top of his head.</p>
                <p><span>Hobbies:</span> Jiji enjoys playing with his favorite toys, watching birds from the window, and discovering new hiding spots around the house.</p>
                <p><span>Favorite Places:</span> Cozy spots in the sun, Our lap, and in bed.</p>
            </div>
            <a href="#contact" class="button">Contact Jiji's Owner</a>
        </div>
        <footer>
            <p>&copy; 2024 Chowder. All rights reserved.</p>
        </footer>
    </body>
    </html>
    '''
    return render_template_string(jiji_page)

if __name__ == '__main__':
    app.run(debug=False)
