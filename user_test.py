import unittest
from user import User


class TestContact(unittest.TestCase):

    def tearDown(self):
        User.account_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("George", "Mboya", "3215", "george@ms.com")

    def test_init(self):

        self.assertEqual(self.new_user.first_name, "George")
        self.assertEqual(self.new_user.last_name, "Mboya")
        self.assertEqual(self.new_user.password, "3215")
        self.assertEqual(self.new_user.email, "george@ms.com")

        # to save user

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.account_list), 1)

        # to delete user

    def test_delete_user(self):
        self.new_User.save_user()
        test_user = User('test', '1234')
        test_user.save_user()

        self.new_User.delete_user()
        self.assertEqual(len(User.contact_list), 1)

    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_contact.save_contact()
        test_user = User("Test", "user", "0712345678",
                         "test@user.com")  # new contact
        test_user.save_contact()
        self.assertEqual(len(User.contact_list), 2)


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
