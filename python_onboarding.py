import sentry_sdk

sentry_sdk.init(
    dsn="https://dab3fb6fde814a4e98500509f7ef1c9a@o4504016362930176.ingest.sentry.io/4504016378331136",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

error_options = [1, 2, 3]

def divide_by_zero():
    divide = 1/1

def undefined_var():
    var = 3
    if var == 6:
        print("var equals 6")

def illegal_concat():
    concat = 3 + '3'

def no_param(param):
    param = param + 7

if __name__ == "__main__":
    print("Choose an error to run: 1, 2, 3, or 4")
    response = int(input())

    if response == 1:
        divide_by_zero()
    elif response == 2:
        undefined_var()
    elif response == 3:
        illegal_concat()
    elif response == 4:
        no_param()
    else:
        print('Invalid input!')