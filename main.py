from flask import Flask, render_template
app = Flask(__name__, template_folder='79m/79m/templates')

@app.route('/')
def home_page():
    return render_template("templates/index.html")
    # return "Hello world!"

@app.route('/sufjan')
def sufjan_is_a_liar():
    return render_template("templates/sufjan.html")

if __name__ == '__main__':
    app.run(debug= True)