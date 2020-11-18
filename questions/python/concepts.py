from enum import Enum
class AccountStatus(Enum):
    ACTIVE, CLOSED = 1, 0

class Account:
    def __init__(self, user_name, password, status=AccountStatus.ACTIVE):
        self.__user_name = user_name
        self.__password = password
        self. __status = status
    
    def get_user_name(self):
        self.__print_name()
        return self.__user_name
    
    def set_user_name(self, user_name):
        self.__user_name = user_name
    
    def get_passord(self):
        return self.__password

    def set_passord(self, password):
        self.__password = password
    
    def __print_name(self):
        print('name')

class Member(Account):
    def __init__(self, user_name, password, status=AccountStatus.ACTIVE, age=0):
        super().__init__(user_name, password, status)
        self.__age = age

    def get_age(self):
        return self.__age


def main():
    print(AccountStatus.ACTIVE)
    print(repr(AccountStatus.ACTIVE))

    member_1 = Member('suyash', 'suyash', AccountStatus.ACTIVE, 27)

    print(member_1.get_age())
    print(member_1.get_user_name())

    # member_1._print_name()

if __name__ == '__main__':
    main()
