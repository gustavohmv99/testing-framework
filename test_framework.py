class TestCase:
    
    def __init__(self, name):
        self.name = name

    def run(self):
        self.set_up()
        test_method = getattr(self, self.name)
        test_method()
        self.tear_down()

    def set_up(self):
        pass
    
    def tear_down(self):
        pass