from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# API
@app.route('/post', methods=["POST"])
def predict():
    input_json = request.get_json(force=True)
    check_key  = input_json['key']

    if('TVTSQT-eF7Vj6vXe8' == check_key):
        load_model = pickle.load(open('model.pkl','rb'))
        load_vectorizer = pickle.load(open('save_vectorizer.pkl','rb'))

        y_pred = load_model.predict(load_vectorizer.transform([input_json['text']]))
        result = {'y_pred' : str(y_pred)}

        return jsonify(result)
    else:
        return 'Key Error'

# Demo Predict
@app.route('/')
def main():
    return render_template('predict.html')

@app.route('/sub', methods = ['POST'])
def submit():
    if request.method == 'POST':
#         text = request.form['text']
#         key = request.form['key']
        text_key = request.get_json()
        text = text_key['text']
        key = text_key['key']

    if('TVTSQT-eF7Vj6vXe8' == key):
        load_model = pickle.load(open('model.pkl','rb'))
        load_vectorizer = pickle.load(open('save_vectorizer.pkl','rb'))

        y_pred = load_model.predict(load_vectorizer.transform([text]))
        
        return str(y_pred)
        # return render_template('sub.html', kq = str(y_pred))
    else:
        return 'Key Error'
        # return render_template('sub.html', kq = 'Key Error')

if __name__ == '__main__':
    app.run(debug=True)
