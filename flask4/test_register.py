import unittest
class test_password():
    def test_password():
        password='mish'
        repeatpassword='mish'
        self.assertTrue(password==repeatpassword)

class email_adress():
    def email_adress():
        email_adress1='milamish@live.com'
        email_adress2='milamish@live,com'
        self.assertTrue(email_adress1==email_adress2)

if __name__=='__main__':
    unittest.main()