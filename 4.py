class IntegerToRoman:
    def __init__(self):
        self.numeral_map = (
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        )
    def integer_to_roman(self, n: int) -> str:
        roman_numeral = ""
        i = 0
        while n > 0:
            while n >= self.numeral_map[i][1]:
                roman_numeral += self.numeral_map[i][0]
                n -= self.numeral_map[i][1]
            i += 1
        return roman_numeral
integer_to_roman = IntegerToRoman()
print(integer_to_roman.integer_to_roman(2023))

