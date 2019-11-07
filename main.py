from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home_page():
    return render_template("index.html")
    # return "Hello world!"

# @app.route('/sufjan')
# def sufjan_is_a_liar():
#     return render_template("sufjan.html")

if __name__ == '__main__sx':
    app.run(debug= True)