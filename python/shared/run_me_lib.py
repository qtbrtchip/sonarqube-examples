def run_me(rate = 100):
    try:
        count = 100 / rate
    except Exception as e:
        count = 0
        print('some error', e)
    print('count:', count)

def print_me(user_id):
    if user_id == 1:
        print('Hello, David')
    else:
        print('Hello, John')
