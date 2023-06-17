class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.current_character = ""

    def advance(self):
        self.position += 1
        if self.position < len(self.code):
            self.current_character = self.code[self.position]
        else:
            self.current_character = ""

    def tokenize(self):
        tokens = []
        self.advance()

        while self.current_character != "":
            if self.current_character.isspace():
                self.advance()
                continue

            if self.current_character.isdigit():
                number = self.get_number()
                tokens.append(("NUMERO", number))
                continue

            if self.current_character.isalpha():
                identifier = self.get_identifier()
                tokens.append(("IDENTIFICADOR", identifier))
                continue

            if self.current_character == "=":
                tokens.append(("ATRIBUICAO", "="))
                self.advance()
                continue

            if self.current_character == ";":
                tokens.append(("PONTO_VIRGULA", ";"))
                self.advance()
                continue

            if self.current_character == "{":
                tokens.append(("ABRE_CHAVE", "{"))
                self.advance()
                continue

            if self.current_character == "}":
                tokens.append(("FECHA_CHAVE", "}"))
                self.advance()
                continue

            if self.current_character == "(":
                tokens.append(("ABRE_PARENTESES", "("))
                self.advance()
                continue

            if self.current_character == ")":
                tokens.append(("FECHA_PARENTESES", ")"))
                self.advance()
                continue

            if self.current_character == ">":
                tokens.append(("MAIOR_QUE", ">"))
                self.advance()
                continue

            if self.current_character == "<":
                tokens.append(("MENOR_QUE", "<"))
                self.advance()
                continue

            if self.current_character == "+":
                tokens.append(("ADICAO", "+"))
                self.advance()
                continue

            if self.current_character == "-":
                tokens.append(("SUBTRACAO", "-"))
                self.advance()
                continue

            if self.current_character == "*":
                tokens.append(("MULTIPLICACAO", "*"))
                self.advance()
                continue

            if self.current_character == "/":
                tokens.append(("DIVISAO", "/"))
                self.advance()
                continue

            if self.current_character == "\"":
                string = self.get_string()
                tokens.append(("STRING", string))
                continue

            if self.current_character == "_":
                string = self.get_identifier()
                tokens.append(("_", string))
                continue

            raise SyntaxError(f"Token inválido: {self.current_character}")

        return tokens

    def get_number(self):
        number = ""
        while self.current_character.isdigit():
            number += self.current_character
            self.advance()
        return int(number)

    def get_identifier(self):
        identifier = ""
        while self.current_character.isalpha() or self.current_character.isdigit():
            identifier += self.current_character
            self.advance()
        return identifier

    def get_string(self):
        string = ""
        self.advance()  # Avança para o próximo caractere após a aspas iniciais
        while self.current_character != "\"":
            string += self.current_character
            self.advance()
            if self.current_character == "":
                raise SyntaxError("Cadeia de caracteres não fechada corretamente")
        self.advance()  # Avança para o próximo caractere após a aspas finais
        return string
