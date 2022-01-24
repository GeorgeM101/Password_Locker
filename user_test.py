from user import User
import unittest


class TestAccount(unittest.TestCase):
    def tearDown(self):
        User.user_users = []

    def setUp(self):
        '''
        this test runs before every test occurs
        '''
        self.new_user = User("George", "Mboya", "Leroy" "2586")

    def test_init(self):
        '''
        a test to assert whether the values entered would appear when the roperty is called
        '''
        self.assertEqual(self.new_user.first_name, "George")
        self.assertEqual(self.new_user.last_name, "Mboya")
        self.assertEqual(self.new_user.user_name, "Leroy")
        self.assertEqual(self.new_user.password, "2586")

    def test_save_user(self):
        '''
        a test to check whether the save function works
        '''
        self.new_user.save_account()
        self.assertEqual(len(User.user_accounts), 1)

    def test_save_multiple_user(self):
        '''
        a test that checks whether both values appended to the array are actually present\ and returns the acount itself
        '''
        self.new_user.save_account()
        user_test = User('abcd', 'efgh', 'ijkl', 'mnop')
        user_test.save_account()
        self.assertEqual(len(User.user_accounts), 2)

    def test_del_user(self):
        '''
        test that check the delete function
        '''
        self.new_user.save_account()
        user_test = User('abcd', 'efgh', 'ijkl', 'mnop')
        user_test.save_account()
        self.new_user.delete_account()
        self.assertEqual(len(User.user_accounts), 1)

    def test_find_user_by_username(self):
        '''
        test to check whether the function used to find accounts really works
        '''
        self.new_user.save_user()
        user_test = User('abcd', 'efgh', 'ijkl', 'mnop')
        user_test.save_account()
        found_account = User.find_by_user_name('ijkl')
        self.assertEqual(found_account.user_name, user_test.user_name)

    def test_user_exists(self):
        '''
       returns a boolean if user profile exists
        '''
        self.new_user.save_user()
        user_test = User('abcd', 'efgh', 'ijkl', 'mnop')
        user_test.save_account()
        account_exists = User.user_exists('ijkl')
        self.assertTrue(account_exists)

    def test_display_profile(self):
        '''
        a test to check the display accounts function
        '''
        self.assertEqual(User.display_profile(),
                         User.user_profiles)


if __name__ == '__main__':
    unittest.main()
