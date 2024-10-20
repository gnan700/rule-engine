import ast

# Renamed from 'rules' to 'rule_list' to avoid conflicts
rule_list1 = "((user_data['age'] > 30 and user_data['department'] == 'Sales') or (user_data['age'] < 25 and user_data['department'] == 'Marketing')) and (user_data['salary'] > 50000 or user_data['experience'] > 5)"
rule_list2 = "((user_data['age'] > 30 and user_data['department'] == 'Marketing')) and (user_data['salary'] > 20000 or user_data['experience'] > 5)"

# Function to evaluate rules
def evaluate_rule(user_data, rule):
    try:
        return eval(rule)  # Dynamically evaluate the rule
    except Exception as e:
        print(f"Error evaluating rule: {e}")
        return False