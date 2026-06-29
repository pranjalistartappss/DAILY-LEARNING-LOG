is_logged_in = True

def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access Denied")
    return wrapper

@login_required
def profile():
    print("Welcome")

profile()