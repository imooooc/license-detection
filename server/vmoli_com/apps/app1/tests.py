from django.test import TestCase

# Create your tests here.
data = {'user_name':'张三', 'email':'1@1.com', 'password':'123', 're_password':'123'}

class myclass():
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def disp(self):
        print(self.user_name)
        print(self.password)

c = myclass()
c.disp()