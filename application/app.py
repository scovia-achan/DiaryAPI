from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"]=True


diaries = [
    {
        'name': 'The first',
        'event': 'High school meetup',
        'activities': ['games', 'sports']
    }
]

#this endpoint creates a new diary
@app.route('/diary', methods=['POST'])
def create_diary():
    request_data = request.get_json()
    new_diary = {
        'name': request_data['name'],
        'event': request_data['event'],
        'activities': []
    }
    diaries.append(new_diary)
    return jsonify(new_diary)



@app.route('/diary/<string:name>')
def get_diary(name):
    #iterate over diaries; if the name matches, return the it. if there is no match, return an error message
    for diary in diaries:
        if diary['name']==name:
            return jsonify(diary)
    
    return jsonify({'message': 'diary not found'})

#GET /diary
@app.route('/diary')
def get_diary_entry():
    return jsonify({'diaries': diaries})


#creating an activity in a diary
@app.route('/diary/<string:name>/activity', methods = ["POST"])
def create_activity_in_diary(name):
    request_data = request.get_json
    for diary in diaries:
        if diary['name']==name:
            new_activities = []
            diary['activities'].append(new_activities)
            return jsonify(new_activities) 
    return jsonify({'message': 'store not found'})


@app.route('/diary/<string:name>/activity')
def get_activities_in_diary(name):
    for diary in diaries:
        if diary['name']==name:
            return jsonify({'activities': diary['activities']})

    return jsonify({'message': 'diary not found'})

app.run(port=5000)
