from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Landing page
@app.route('/')
def index():
    description = "Welcome to our UMEP tool page. Select a tool:"
    return render_template('index.html', description=description)

# SOLWEIG
@app.route('/tool1')
def tool1():
    # Execute tool 1 script here
    result = "This is the result of Tool 1."
    return render_template('tool.html', result=result)

# Tool 2
@app.route('/tool2')
def tool2():
    # Execute tool 2 script here
    result = "This is the result of Tool 2."
    return render_template('tool.html', result=result)

# Tool 3
@app.route('/tool3')
def tool3():
    # Execute tool 3 script here
    result = "This is the result of Tool 3."
    return render_template('tool.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)