class ExpressionSolver:
    def __init__ (self, expression):
        self.expression = expression
        
    def solve_expression(self):
        try:
            
            result = eval(self.expression)
            return result
        except Exception as e:
            
            return f"Error:{e}"
        
    def print_result(self):
        
        result = self.solve_expression()
        print(f"The result of'{self.expression}' is: {result}")
        
        
        
expression = input("Enter a mathematical expression:")
solver = ExpressionSolver(expression)
solver.print_result()