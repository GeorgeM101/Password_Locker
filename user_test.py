from user import User
import unittest


class TestAccount(unittest.TestCase):
    def tearDown(self):
        User.user_accounts = []

    def setUp(self):
        '''
        this test runs before every test occurs
        '''
        self.new_account = User('george', 'mboya', 'leroy', '2568')

    def test_init(self):
        '''
        test to confirm whether entered values would return when called 
        '''
        self.assertEqual(self.new_account.first_name, 'george')
        self.assertEqual(self.new_account.last_name, 'mboya')
        self.assertEqual(self.new_account.user_name, 'Leroy')
        self.assertEqual(self.new_account.password, '2568')

    def test_save_account(self):
        '''
        a test to check whether the save function works
        '''
        self.new_account.save_account()
        self.assertEqual(len(User.user_accounts), 1)

    def test_save_multiple_accounts(self):
        '''
        a test that checks whether both values appended to the array are actually present\ and returns the acount itself
        '''
        self.new_account.save_account()
        test_account = User('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        self.assertEqual(len(User.user_accounts), 2)

    def test_del_account(self):
        '''
        tests the delete fuction 
        '''
        self.new_account.save_account()
        test_account = User('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(User.user_accounts), 1)

    def test_find_account_by_username(self):
        '''
        test to check whether the function used to find user really works
        '''
        self.new_account.save_account()
        test_account = User('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        found_account = User.find_by_user_name('ijkl')
        self.assertEqual(found_account.user_name, test_account.user_name)

    def test_account_exists(self):
        '''
    test that returns a boolean value on whether the account exists
        '''
        self.new_account.save_account()
        test_account = User('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        account_exists = User.account_exists('ijkl')
        self.assertTrue(account_exists)

    def test_display_accounts(self):
        '''
        a test to check the display user function
        '''
        self.assertEqual(User.display_accounts(),
                         User.user_accounts)


if __name__ == '__main__':
    unittest.main()
