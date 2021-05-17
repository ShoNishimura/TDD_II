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
    def setUp(self):
        self.wasRun = None
        self.log = "setUp"
    def testMethod(self):
        self.wasRun = 1
    
# テストメソッドが呼ばれたらtrueを出力し、
# 呼ばれなかったらfalseを出力する
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun) #true
    def testSetUp(self):
        self.test.run()
        assert("setUp" == self.test.log)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

