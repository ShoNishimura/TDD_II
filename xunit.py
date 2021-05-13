#TODO
# # テストメソッドを呼び出す
# set upを最初に呼び出す
# tearDownを後で呼び出す
# テストメソッドが失敗したとしてもtearDownを呼び出す
# 複数のテストを走らせる
# 収集したテスト結果を出力する

# テストメソッドが呼ばれたらtrueを出力し、
# 呼ばれなかったらfalseを出力する
test =  WasRun("testMethod")
print(test.wasRun) #false
test.testMethod()
print(test.wasRun) #true

class WasRun:
    def __init__(self, name):
        pass
        #self.wasRun = None