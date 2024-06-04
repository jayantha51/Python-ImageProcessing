# zip (* iterables) = aggregates elements from two or more iterables (list, tuples, sets, etc.
#                   creates a zip objects with paris elements stored in tuples for each element


def main():
    user_names = ["Jayantha", "Ashwin", "Sayu"]
    passwords = ("P@ssword", "jshs&5GG", "GAH96+Gaa")
    last_log_in_dates = ["12/02/2021", "10/11/2022", "05/21/2020"]

    users = zip(user_names, passwords)
    print(type(users)) # let's see what user is
    for i in users:
        print(i)

    # Let's convert user into list
    users = list(users)
    print(type(users))

    # let's convert user into a dic
    users = dict(zip(user_names, passwords))
    print(type(users))
    print("Next___________")
    for key, value in users.items():
        print(key+" : "+ value)

    print("next__________")
    # one can create a zip with more than 2 elements
    user_all = zip(user_names, passwords, last_log_in_dates)
    for i in user_all:
        print(i)

if __name__ == '__main__':
    main()