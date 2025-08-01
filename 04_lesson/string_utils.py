class StringUtils:
    def reverse(self, s):
        #Возвращает строку в обратном порядке.
        return s[::-1]
    
    def uppercase(self, s):
        #Преобразует строку в верхний регистр.
        return s.upper()
    
    def lowercase(self, s):
        #Преобразует строку в нижний регистр.
        return s.lower()
    
    def trim(self, s):
        #Удаляет лишние пробелы слева и справа строки.
        return s.strip()