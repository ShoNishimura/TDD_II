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
    def tearDown(self):
        pass
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()  
        self.tearDown()
        return result

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "
    def testMethod(self):
        self.log = self.log + "testMethod "
    def tearDown(self):
        self.log = self.log + "tearDown "
    
# テストメソッドが呼ばれたらtrueを出力し、
# 呼ばれなかったらfalseを出力する
class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())
    
class TestResult:
    def __init__(self):
        self.runCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def summary(self):
            return "%d run, 0 failed" % self.runCount


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
