# Author: Oladapo Okikiola
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print("True")
            exit()
        elif ok in ('n', 'no', 'nop', 'nope'):
            print("False")
            exit()
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok(prompt = "Okay?: ")