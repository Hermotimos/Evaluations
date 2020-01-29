from dataflow import Database


def question():
    answ = input("\nWould you like to continue (y or n) ?\n")
    if answ == 'y':
        return True
    elif answ == 'n':
        return False
    else:
        print("\nWrong value entered. Please choose again.\n")
        return question()


def do_action():
    db = choose_db()
    action = choose_action()
    action(db)


def choose_db():
    """Returns instance of Database"""

    def instantiate_db(db):
        if db == 1:
            db = Database("data_tvseries")
            return db
        elif db == 2:
            db = Database("data_movies")
            return db

    try:
        chosen_db = int(input("Which database would you like to browse?\n"
                              "1 - TV series database.\n"
                              "2 - movie database.\n"))
        options = [1, 2]
        assert 0 < chosen_db < options[-1] + 1
        chosen_db = instantiate_db(chosen_db)
        return chosen_db
    except Exception:
        print("Wrong value entered. Please choose again.\n")
        return choose_db()


def choose_action():
    """Returns function"""
    try:
        chosen_action = int(input("What would you like to do?\n"
                                  "1 - see whole database\n"
                                  "2 - see average evaluation for a title\n"
                                  "3 - see number of evaluations for a title\n"
                                  "4 - see all evaluations for a title\n"
                                  "5 - add new evaluation\n"))
        options = [1, 2, 3, 4, 5]
        assert 0 < chosen_action < options[-1] + 1

        if chosen_action == 1:
            return print
        elif chosen_action == 2:
            return print_avg_evals
        elif chosen_action == 3:
            return print_cnt_evals
        elif chosen_action == 4:
            return print_get_evals
        elif chosen_action == 5:
            return evaluate

    except Exception:
        print("Wrong value entered. Please choose again.\n")
        return choose_action()


def print_avg_evals(db):
    return print(db.avg_evals(input("Enter title: ")))


def print_cnt_evals(db):
    return print(db.cnt_evals(input("Enter title: ")))


def print_get_evals(db):
    return print(db.get_evals(input("Enter title: ")))


def evaluate(database):
    new_tit = ask_for_title()
    new_eval = ask_for_evaluation()
    database.insert_eval(new_tit, new_eval)
    print("You entered following evaluation: '{}': {} \nYour evaluation is much appreciated.".format(new_tit, new_eval))


def ask_for_title():
    new_title = input("Enter title: ")
    try:
        assert len(new_title) > 0
        return new_title
    except AssertionError:
        print("You haven't given any title. Try again.\n")
        return ask_for_title()


def ask_for_evaluation():
    new_evaluation = input("Enter evaluation 1-10: ")
    try:
        assert 0 < int(new_evaluation) < 11
        return new_evaluation
    except Exception:
        print("Entered value ({}) outside the scope of possible options (1-10). Try again.\n".format(new_evaluation))
        return ask_for_evaluation()
