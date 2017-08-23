print "Let's get started!"
spy_name=raw_input("Provide your name here:")
spy_salutation=raw_input("What should we call you ? :")
#check whether user has input or not
if len(spy_name)>0:
    #code block if the condition is true
    #Concatination of salutation and name
    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    spy_age=raw_input("What is your name")
    print type(spy_age)


    spy_name= spy_salutation + "" + spy_name

    print  'Welcome' + "spy_name" + "Glad to back you with us"
    print "Alright" + "spy_name" + "i'd like to know more about you before you proceed further"
else:
    print "Invalid Name.Try again."