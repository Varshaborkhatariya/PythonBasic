class A:
    def ShowData(self):
        print("Im in A calss")

class B(A):
    def ShowData(self):
        print("Im in B calss")
obj=B()
obj.ShowData()
