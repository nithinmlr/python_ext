from flask import Flask,render_template_string
from datetime import datetime
app = Flask(__name__)

@app.route('/')

def home():
    love = 'ILoveJew'
    # Define the start date
    start_date = datetime(2024, 10, 1)
    # Calculate the number of days from the start date to today
    days_since_start = (datetime.now() - start_date).days
    days_str = str(days_since_start).center(60)

    # Generate ASCII heart with countdown in the middle
    ascii_art = '\n'.join([''.join([
        (days_str if (x == 0 and y == 0) else (love[(x-y)%len(love)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else ' '))
        for x in range(-30, 30)]) for y in range(15, -15, -1)
    ])

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ASCII Art with Countdown</title>
        <style>
            body {
                font-family: monospace;
                white-space: pre;
                text-align: center;
            }
            #ascii-art {
                line-height: 1.1;
            }
        </style>
    </head>
    <body>
        <div id="ascii-art">{{ ascii_art }}</div>
    </body>
    </html>
    """
    return render_template_string(html_template, ascii_art=ascii_art)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
