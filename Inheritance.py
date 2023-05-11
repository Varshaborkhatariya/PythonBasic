class A:
    def displayA(self):
        print("Welocom to Wscubeteach A")

class B:
    def displayB(self):
         print("Welocom to Wscubeteach B")

class C(A,B):
    def displayC(self):
         print("Welocom to Wscubeteach C")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()

