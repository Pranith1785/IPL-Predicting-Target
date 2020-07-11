from flask import Flask, render_template, request
import joblib

## load the model
model = joblib.load('predict_score.sav','r')

def team_array(team_name,test_list):

    if team_name == 'CSK':
        test_list += [1,0,0,0,0,0,0,0]
    elif team_name == 'DC' :
        test_list += [0,1,0,0,0,0,0,0]
    elif team_name == 'KKR' :
        test_list += [0,0,1,0,0,0,0,0]
    elif team_name == 'KXIP' :
        test_list += [0,0,0,1,0,0,0,0]
    elif team_name == 'MI' :
        test_list += [0,0,0,0,1,0,0,0]
    elif team_name == 'RCB' :
        test_list += [0,0,0,0,0,1,0,0]
    elif team_name == 'RR' :
        test_list += [0,1,0,0,0,0,1,0]
    elif team_name == 'SRK' :
        test_list += [0,1,0,0,0,0,0,1]

    return test_list


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port='2020',debug=True)