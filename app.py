from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from rule_engine import create_ast, evaluate_node, Node
from models import db, Rule
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Changed to data.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule_string')
    try:
        # Save the rule to the database
        new_rule = Rule(rule_string=rule_string)
        db.session.add(new_rule)
        db.session.commit()

        ast_root = create_ast(rule_string)
        return jsonify(ast_root.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Error creating rule: {str(e)}"}), 400

@app.route('/get_rules', methods=['GET'])
def get_rules():
    rules = Rule.query.all()
    return jsonify([{"id": rule.id, "rule_string": rule.rule_string} for rule in rules]), 200

def dict_to_node(node_dict):
    """Convert a dictionary representation back to a Node object."""
    if node_dict['type'] == 'operator':
        left_node = dict_to_node(node_dict['left']) if 'left' in node_dict else None
        right_node = dict_to_node(node_dict['right']) if 'right' in node_dict else None
        return Node(type='operator', operator=node_dict['operator'], left=left_node, right=right_node)
    else:
        return Node(type='operand', attribute=node_dict['attribute'], operator=node_dict['operator'], value=node_dict['value'])

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    ast_data = request.json.get('ast')
    data = request.json.get('data')

    try:
        root_node = dict_to_node(ast_data)  # Convert AST dict back to Node
        is_eligible = evaluate_node(root_node, data)
        return jsonify({"eligible": is_eligible}), 200
    except Exception as e:
        return jsonify({"error": f"Error evaluating rule: {str(e)}"}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)
