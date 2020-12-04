from shared.run_me_lib import run_me, print_me

def test_run_me():
    # No exception
    run_me()

    #with exception
    run_me(0)

def test_print_me():
    print_me(user_id = 1)
    print_me(user_id = 2)
