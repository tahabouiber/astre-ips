from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

with open('./MyData.json', 'r', encoding='utf-8') as d_file:
    data = json.load(d_file)

with open('./hypotheses.json', 'r', encoding='utf-8') as h_file:
    hypos = json.load(h_file)

def calculate_score(student, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    score_ips = 0
    score_astre = 0
    question_scores = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    total_ips = q1 + q2 + q3 + q4 + q5
    total_astre = q6 + q7 + q8 + q9 + q10
    hypo_num = 0
    for hypo in hypos:
        split_hypo = hypo["reponse"].split(", ")
        for rep in split_hypo:
            if rep in student.get(hypo["question"], ""):
                if hypo["filiere"] == "IPS":
                    score_ips += question_scores[hypo_num]
                if hypo["filiere"] == "ASTRE":
                    score_astre += question_scores[hypo_num]
                break
        hypo_num += 1
    final_ips_score = 0
    if total_ips != 0:
        final_ips_score = (score_ips * 100) / total_ips
    final_astre_score = 0  
    if total_astre != 0:
        final_astre_score = (score_astre * 100) / total_astre   
    return (final_ips_score, final_astre_score)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_hypotheses', methods=['GET'])
def get_hypotheses():
    return jsonify(hypos)

@app.route('/update_scores')
def update_scores():
    q1 = int(request.args.get('q1'))
    q2 = int(request.args.get('q2'))
    q3 = int(request.args.get('q3'))
    q4 = int(request.args.get('q4'))
    q5 = int(request.args.get('q5'))
    q6 = int(request.args.get('q6'))
    q7 = int(request.args.get('q7'))
    q8 = int(request.args.get('q8'))
    q9 = int(request.args.get('q9'))
    q10 = int(request.args.get('q10'))

    highcharts_data = []
    for student in data:
        ips_score, astre_score = calculate_score(student, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
        highcharts_data.append({
            "name": student["Numero etudiant "],
            "data": [ips_score, astre_score]
        })

    return jsonify(highcharts_data)

if __name__ == '__main__':
    app.run(debug=True)
