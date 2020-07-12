from flask import Flask, render_template, request
import joblib
import numpy as np

## load the model
model = joblib.load('predict_score.pkl')

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

def venue_array(venueName):

    venue_list =[0]*34

    venu_map = {"Barabati":0,"Brabourne":1,"BuffaloPark":2,"DICS":3,"DYPSA":4,"DeBeersDiamond":5,"Eden":6,"FSK":7,"FSKG":8,
              "GeorgePark":9,"GreenPark":10,"HCS":11,"HPCAS":12,"JSCAISC":13,"Kingsmead":14,"MACS":15,"MCAS":16,"MCS":17,"NewWanderers":18,
               "Newlands":19,"OUTsurance":20,"PCAS":21,"RGIS":22,"SCAS":23,"SMS":24,"SPS":25,"SRSS":26,"SVNSIS":27,"SZS":28,"Sharjah":29,
               "SuperSport":30,"VCAS":31,"WS":32,"YSRACACS":33}

    venue_list[venu_map[venueName]] = 1

    return venue_list

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    data_array = []

    if request.method == 'POST' :
        
        ovrs = int(request.form['overs'])
        balls = int(request.form['balls'])
        curr_score = int(request.form['curr_score'])
        wkts = int(request.form['wickets'])
        last_runs = int(request.form['last5o_runs'])
        last_wkts = int(request.form['last5o_wkts'])

        data_array = [ovrs,balls,curr_score,wkts,last_runs,last_wkts]

        batting = request.form['batting_team']
        data_array = team_array(batting,data_array)
        
        bowling = request.form['bowling_team']
        data_array = team_array(bowling,data_array)
        
        venue_name = request.form['venue']
 
        data_array += venue_array(venue_name)

        ##Apply the new data on loaded model
        data_array = np.array([data_array])
        score = model.predict(data_array)[0]
        score = int(score)
    return render_template('result.html',lower_score=score-4,upper_score = score+4)


if __name__ == '__main__':
    app.run(port='2020',debug=True)