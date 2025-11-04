class A:
    def feature1(self):
        print("Feature 1 from Class A")

class B(A):
    def feature2(self):
        print("Feature 2 from Class B")

class C(B):
    def feature3(self):
        print("Feature 3 from Class C")

obj = C()
obj.feature1()
obj.feature2()
obj.feature3()
