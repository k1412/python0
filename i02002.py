password_text = 1
confirming_password_text = 2
enter_count = 0

while password_text != confirming_password_text:
    if enter_count != 0:
        print 'Inconsistent password, please enter again!'
    password_text = str(raw_input('input the password:'))
    confirming_password_text = str(raw_input('confirm the password:'))
    enter_count+=1
    
password_text == confirming_password_text
print 'Password setting is successful!'
