#!/usr/bin/env python3.8
from user import User
from password import Password


def create_account(first_name, last_name, user_name, password):
    user = User(first_name, last_name, user_name, password)
    return user


def save_account(user):
    user.save_account()


def delete_account(user):
    user.delete_account()


def find_accounts(user_name):
    return User.find_by_user_name(user_name)


def isexist_accounts(user_name):
    return User.account_exists(user_name)


def display_accounts():
    return User.display_accounts()


def create_page(page, password):
    password = Password(page, password)
    return password


def save_page(password):
    password.save_page()


def find_page(pager):
    return Password.find_by_page(pager)


def isexist_page(pager):
    return Password.page_exists(pager)


def delete_page(password):
    password.delete_page()


def display_pages():
    return Password.display_page()


def main():
    print('Welcome to Password-Locker')
    print('Select an option to use the page')
    while True:

        print(" 1) LOGIN \n 2) CREATE AN ACCOUNT \n 3) DISPLAY ACCOUNTS \n 4) SIGN OUT")

        # To login

        choice = int(input())
        if choice == 1:
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()
            account = find_accounts(username)
            if account.user_name == username and account.password == password:

                print('logged in ')
                while True:

                    print(
                        f'{username}, Welcome! Choose an option to select a service')

                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                    log_choice = int(input())
                    if log_choice == 1:

                        print('Page name')
                        page = input()

                        print('password')
                        password = input()

                    # created and saved page
                        save_page(create_page(page, password))

                    elif log_choice == 2:
                        print("Enter the name of the page you want to delete")

                        page = input()
                        if isexist_page(page):
                            remove_page = (page)
                            delete_page(remove_page)

                        else:
                            print(f'{page} does not exist')

                    elif log_choice == 3:
                        if display_pages():
                            for keyword in display_pages():
                                print(
                                    f'{keyword.page}:{keyword.password}'
                                )
                        else:
                            print('PASSWORD LOCKER EMPTY')
                            print('\n')

                    elif log_choice == 4:
                        print('Thank you for using Password Locker')
                        break
            else:
                print('Invalid details')

        # To create new account

        if choice == 2:
            print('Create a new account')

            print('Enter your first name')
            first_name = input()

            print('Enter your last name')
            last_name = input()

            print('Enter preferred username')
            user_name = input()

            print('Enter a secure password')
            password = input()

            save_account(create_account(
                first_name, last_name, user_name, password))

            # create and save a new account

            print('YOUR ACCOUNT WAS SUCCESSFULLY CREATED!')
            while True:

                print(
                    f'Welcome {user_name}, what would you like to do')
                print(
                    ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                log_choice = int(input())
                if log_choice == 1:

                    print('Page name')
                    page = input()

                    print('password')
                    password = input()

                    # created and saved page
                    save_page(create_page(page, password))

                elif log_choice == 2:
                    print("Enter the name of the page you want to delete")

                    page = input()
                    if isexist_page(page):
                        remove_page = (page)
                        delete_page(remove_page)

                    else:
                        print(f'{page} does not exist')

                elif log_choice == 3:
                    if display_pages():
                        for keyword in display_pages():
                            print(
                                f'{keyword.page}:{keyword.password}'
                            )
                    else:
                        print('NO PASSWORD SAVED YET')

                elif log_choice == 4:
                    break

        elif choice == 4:
            if display_accounts():
                for account in display_accounts():
                    print(
                        f'{account.user_name}'
                    )
            else:
                print('Invalid')

        elif choice == 5:
            print('Thank you for choosing Password Locker....')
            break


if __name__ == '__main__':
    main()
