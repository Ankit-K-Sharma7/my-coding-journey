class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")
        
    def valid(self):
        if len(self.card_num) <= 1:
            return False

        if not self.card_num.isdigit():
            return False

        total = 0

        for index , digit in enumerate(self.card_num[::-1]):
            num = int(digit)
            if index % 2 == 1:
                num *= 2
                if num > 9:
                    num -= 9

            total += num
        return total % 10 == 0
