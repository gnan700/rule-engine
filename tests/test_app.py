import unittest
from rule_engine import create_ast,evaluate_node, Node

class TestRuleEngine(unittest.TestCase):
    
    def setUp(self):
        # Sample rules for testing
        self.rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        self.rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
        
    def test_create_rule(self):
        # Test the creation of individual rules
        ast1 = create_rule(self.rule1)
        ast2 = create_rule(self.rule2)
        
        # Check the structure of the AST
        self.assertIsInstance(ast1, Node)
        self.assertIsInstance(ast2, Node)
        self.assertEqual(ast1.value, 'AND')  # Check root operator
        self.assertEqual(ast2.value, 'AND')  # Check root operator
    
    def test_evaluate_rule(self):
        # Sample user data
        user_data = {
            "age": 35,
            "department": "Sales",
            "salary": 60000,
            "experience": 6
        }
        
        # Create rule AST
        ast1 = create_ast(self.rule1)
        
        # Evaluate rule against user data
        result = evaluate_rule(ast1, user_data)
        self.assertTrue(result)  # Expect True for this case

        user_data_invalid = {
            "age": 22,
            "department": "Marketing",
            "salary": 15000,
            "experience": 2
        }
        
        # Evaluate rule against invalid user data
        result_invalid = evaluate_rule(ast1, user_data_invalid)
        self.assertFalse(result_invalid)  # Expect False for this case
    
    def test_additional_combining(self):
        # Additional rules for testing
        rule3 = "age < 40 AND salary < 70000"
        
        # Combine all three rules
        combined_ast = combine_rules([self.rule1, self.rule2, rule3])
        
        # Check if the combined AST is still valid
        self.assertIsInstance(combined_ast, Node)
        
        # Sample user data
        user_data_combined = {
            "age": 32,
            "department": "Marketing",
            "salary": 65000,
            "experience": 7
        }
        
        # Evaluate against the combined rules
        result_combined = evaluate_rule(combined_ast, user_data_combined)
        self.assertTrue(result_combined)  # Expect True if combined logic is met
        
        user_data_combined_invalid = {
            "age": 40,
            "department": "Marketing",
            "salary": 80000,
            "experience": 5
        }
        
        # Evaluate against the combined rules with invalid data
        result_combined_invalid = evaluate_rule(combined_ast, user_data_combined_invalid)
        self.assertFalse(result_combined_invalid)  # Expect False if combined logic is not met


if __name__ == '__main__':
    unittest.main()
