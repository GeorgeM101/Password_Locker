class User:

    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    user_accounts = []

    def save_account(self):
        '''
        this is a save function that adds new users to array (append)
        '''
        User.user_accounts.append(self)

    def delete_account(self):
        '''
        to delete an account
        '''
        User.user_accounts.remove(self)

    @classmethod
    def find_by_user_name(cls, user_name):
        '''

        checks if user account exists
        '''
        for account in cls.user_accounts:
            if account.user_name == user_name:
                return account

    @classmethod
    def account_exists(cls, user_name):
        '''
        returns a boolean value if searched account exists
        '''
        for account in cls.user_accounts:
            if account.user_name == user_name:
                return True
        return False

    @classmethod
    def display_accounts(cls):
        return cls.user_accounts
