from flask import Flask, render_template, request  # подключаем render_template, который включает функции для Jinja
import joblib

with open('model.pkl', 'rb') as f:
    model = joblib.load(f)


app = Flask(__name__)


@app.route("/")
def render_index():
    output = render_template("index.html")  # рендерим шаблон
    return output  # возвращаем то, что отрендерилось


@app.route("/predict/", methods=["POST"])
def render_predict():
    age = request.form["age"]
    fare = request.form["fare"]
    sex = request.form['sex']

    try:
        if float(age) and float(fare) and sex is not None:

            prediction = model.predict([[float(age), float(fare), float(sex)]])
        
            output = render_template("predict.html", prediction=prediction[0])
            return output
    except ValueError:
        output = render_template("error.html")
        return output


if __name__ == '__main__':
    #app.run(debug=True)  # ! while development
    app.run()  # production