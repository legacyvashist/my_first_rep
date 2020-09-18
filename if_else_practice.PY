x = True
while x == True :
    print("you enter a dark room with two doors Do you go through door #1 or door #2")
    door = input(">")

    if door == "1":
     print("this room have window and balcony #1 to go to window #2 to go to balcony press #z to exit")
     door_one_choice = input(">")
     if door_one_choice == "1":
      print("you are looking out of window!")
     elif door_one_choice == "2" :
      print("you are in the balcony!")
     if door_one_choice == "z":
      x = False
    elif door == "2":
     print("this room is completely empty press #z to exit")
     return_command = input(">")
     if return_command == "z":
       print("the program have been exited")
       x = False
    else :
      print("you have pressed the wrong key!")


