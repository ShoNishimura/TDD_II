#TODO
# # テストメソッドを呼び出す
# set upを最初に呼び出す
# tearDownを後で呼び出す
# テストメソッドが失敗したとしてもtearDownを呼び出す
# 複数のテストを走らせる
# 収集したテスト結果を出力する

# テストメソッドが呼ばれたらtrueを出力し、
# 呼ばれなかったらfalseを出力する
class WasRun:
    def __init__(self, name):
        self.wasRun = None
    def run(self):
        self.testMethod()
    def testMethod(self):
        self.wasRun = 1

test =  WasRun("testMethod")
print(test.wasRun) #false
test.run()
print(test.wasRun) #true

