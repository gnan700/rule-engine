class Node:
    def __init__(self, type, left=None, right=None, operator=None, value=None, attribute=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # Reference to another Node (left child)
        self.right = right  # Reference to another Node (right child for operators)
        self.operator = operator  # For operator nodes (e.g., "AND", "OR")
        self.value = value  # For operand nodes (e.g., number for comparisons)
        self.attribute = attribute  # Attribute name for operand nodes

    def to_dict(self):
        """Convert Node to a dictionary for JSON serialization."""
        node_dict = {
            'type': self.type,
            'operator': self.operator,
            'value': self.value,
            'attribute': self.attribute,
        }
        if self.left is not None:
            node_dict['left'] = self.left.to_dict()  # Recursively convert left child
        if self.right is not None:
            node_dict['right'] = self.right.to_dict()  # Recursively convert right child
        return node_dict

def create_ast(rule_string):
    # Implement rule parsing logic here to create an AST from the rule_string
    if 'AND' in rule_string:
        parts = rule_string.split('AND')
        left = create_ast(parts[0].strip())
        right = create_ast(parts[1].strip())
        return Node(type='operator', operator='AND', left=left, right=right)
    elif 'OR' in rule_string:
        parts = rule_string.split('OR')
        left = create_ast(parts[0].strip())
        right = create_ast(parts[1].strip())
        return Node(type='operator', operator='OR', left=left, right=right)
    else:
        # Basic parsing for operands
        if '>' in rule_string:
            attribute, value = rule_string.split('>')
            return Node(type='operand', attribute=attribute.strip(), operator='>', value=int(value.strip()))
        elif '=' in rule_string:
            attribute, value = rule_string.split('=')
            return Node(type='operand', attribute=attribute.strip(), operator='=', value=value.strip().strip("'"))

def evaluate_node(node, data):
    """Evaluate the AST against the provided data."""
    if node.type == 'operator':
        left_value = evaluate_node(node.left, data)
        right_value = evaluate_node(node.right, data)
        if node.operator == 'AND':
            return left_value and right_value
        elif node.operator == 'OR':
            return left_value or right_value
    elif node.type == 'operand':
        attr_value = data.get(node.attribute)
        if node.operator == '>':
            return attr_value > node.value
        elif node.operator == '=':
            return attr_value == node.value
    return False
