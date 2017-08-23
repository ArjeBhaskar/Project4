print "Let's get started!"
spy_name = raw_input("Provide your name here :")

#check whether spy has input something or not
if len(spy_name) >0 :
    #code block if the condition is true.
    # concatination of salutation and name
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
    spy_salutation = raw_input("What should we call you ?  : ")

    spy_age = int(raw_input(" Enter your age. ? "))


    spy_name = spy_salutation + " " + spy_name


    print 'Welcome ' + spy_name + " Glad to have you back with us."
    print "Alright " + spy_name + " i'd like to know more about you before we proceed."
    spy_rating = float(raw_input("Spy rating ? :"))
    spy_is_online = True
    print "Authentication Complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of:" + str(spy_rating) + " Proud to have you on board"
else:
    print  "Invalid name. Try Again."