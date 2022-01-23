import unittest
from user import User


class TestContact(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()


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
