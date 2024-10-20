from flask import Flask, request, jsonify, render_template
from rule_engine import evaluate_rule, rule_list1, rule_list2  # Import the rules and evaluation function
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/evaluate', methods=['POST'])
def evaluate():
    user_data = request.json  # Get user data from the request
    
    # Evaluate the two rules
    is_eligible_rule1 = evaluate_rule(user_data, rule_list1)
    is_eligible_rule2 = evaluate_rule(user_data, rule_list2)

    return jsonify({
        "rule1_eligible": is_eligible_rule1,
        "rule2_eligible": is_eligible_rule2
    })

if __name__ == '__main__':
    app.run(debug=True)