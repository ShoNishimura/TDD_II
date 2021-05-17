#TODO
# # テストメソッドを呼び出す
# set upを最初に呼び出す
# tearDownを後で呼び出す
# テストメソッドが失敗したとしてもtearDownを呼び出す
# 複数のテストを走らせる
# 収集したテスト結果を出力する

class TestCase:
    def __init__(self, name):
        self.name = name  
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()  

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)
    def setUp(self):
        self.wasSetUp = 1
    def testMethod(self):
        self.wasRun = 1
    
    
# テストメソッドが呼ばれたらtrueを出力し、
# 呼ばれなかったらfalseを出力する
class TestCaseTest(TestCase):
    
    def testRunning(self):
        test =  WasRun("testMethod")
        assert(not test.wasRun) #false
        test.run()
        assert(test.wasRun) #true
    def testSetUp(Self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

