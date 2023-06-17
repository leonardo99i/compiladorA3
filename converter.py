class Converter:
    def __init__(self, tokens):
        self.tokens = tokens

    def convert(self):
        converted_code = ""
        indent_level = 0

        for token in self.tokens:
            token_type, token_value = token

            if token_type == "PROGRAMA":
                converted_code += "def main():\n"
                indent_level += 1
            elif token_type == "FIM_PROGRAMA":
                indent_level -= 1
            elif token_type == "IDENTIFICADOR":
                converted_code += f"{'    ' * indent_level}{token_value} = "
            elif token_type == "NUMERO":
                converted_code += f"{token_value}\n"
            elif token_type == "ATRIBUICAO":
                converted_code += f"{'    ' * indent_level}{token_value} "
            elif token_type == "OPERADOR":
                if token_value == "+":
                    converted_code += "+ "
                elif token_value == "-":
                    converted_code += "- "
                elif token_value == "*":
                    converted_code += "* "
                elif token_value == "/":
                    converted_code += "/ "
            elif token_type == "PONTO_VIRGULA":
                converted_code += "\n"
        
        return converted_code


