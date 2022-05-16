test_text = ""
class dynlib:
    def init(test):
        global test_text
        test_text = test

def print_it():
    print(test_text)