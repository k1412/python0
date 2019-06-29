def getpass(prompt='Password: ', stream=None):
    import msvcrt
    for c in prompt:
        msvcrt.putch(c)
    pw = ""
    while 1:
        c = msvcrt.getch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            pw = pw[:-1]
        else:
            pw = pw + c
    msvcrt.putch('\r')
    msvcrt.putch('\n')
    return pw
#如何自定义一个输入接受的函数？
password_text = getpass()
confirming_password_text = getpass('Confirm:')
while password_text != confirming_password_text:
    password_text = getpass()
    confirming_password_text = getpass('Confirm:')
assert password_text == confirming_password_text