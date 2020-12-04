def run_me(rate = 100):
    try:
        count = 100 / rate
    except Exception as e:
        count = 0
        print('some error', e)
    print('count:', count)
