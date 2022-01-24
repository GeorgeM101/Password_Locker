#!/usr/bin/env python3.8

from click import confirm
from user import User


def main():

    while True:
        print("Welcome to Password Locker")
        print("/n")
        print("Select code NA to create a new account,LI to login to your account or EX to exit the app")
        short_code = input()
        print("/n")

        if short_code == "NA":
            print("Create user name")
            created_username = input()

            print("Create password")
            created_password = input()

            print("Re-enter password")
            confirm_password = input()

            while confirm_password != created_password:
                print("Wrong password! Try again ")
                created_password = input()
                print("confirm your password")
                confirm_password = input()

            else:
                print(f"{created_username}) your account was successfully created")
            print("/n")
            print("Login to account")
            print("username")
            entered_username = input()
            print("input password")
            entered_password = input()

            while entered_username != created_username or entered_password != created_password:
                print("Invalid login details")
            print("username")
            entered_username = input()
            print("Enter password")
            entered_password = input()

        else:
            print(f"{entered_username}, welcome to your account")
            print("/n")

        print("input password")
        inserted_password = input()
