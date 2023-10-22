# SUBTRACK
    #### Video Demo:  https://youtu.be/IQ3UfdIb_cM
    #### Description:

    The goal for SubTrack was to create a local, lightweight GUI applications in which users
    could track their current running subscription plans by utilising a SQLite3 database. They would be able to see the name
    of the subscriptions, the price , when it started, the renewal period and the next time it will
    be charged. For the initial approach I created a program which could be run only using the terminal window
    using user input to navigate different functions. It would utilize PrettyTables library to format
    the information in a more visual manner. After the program worked fully from the terminal I then
    began to implement the GUI using Tkinter. The functions were designed in a way that they could be implemented
    easily in the GUI but in the end, modifications did have to be made and additional functions created.

    Firstly, the Sub() class. Whilst not strictly neccesary I wanted to create a class representing a subscription.
    The variables of which would be name, price, start date, and the renewal period. I utilised a setter on price to
    ensure that the input could be cast to a float, rejecting other forms of input by raising a TypeError. I used
    another setter for the start date which included a RegEx search to check for the format of YYYY-MM-DD. This
    is the format that the datetime module produces so this setter ensured dates were being stored uniformly in the
    database. Another setter for renewal ensured integer input to avoid text inputs. I mainly used OOP route because I
    wanted to practice making a class, but it did become very practical for checking inputs in a concise manner and
    also helped when porting to the GUI.

    The main function takes user inputs in, add, delete, and view to perform the repsective tasks. View creates a table
    displaying all current subscriptions. Add will take you to adding a subscription and delete will prompt for a name to
    delete. Typing exit will end the program.

    View using DB functions to fetch a tuple of all current entries in the database. A for loop then iterates each row
    and adds it to the table initialised with PrettyTable. Once finished it returns the table which is then printed by
    main.

    Add() takes optional paramaters of name, price, start date and renewal. If not given the user is prompted to enter these
    from the terminal. This was created like this for the GUI and terminal models. the Sub() class is then called on these
    variables to create the instance and main performs the DB execution of adding and commiting it to the database.

    insert() was created for the GUI to be able to call a functions with a Sub() class and add it to the database.

    delete() calls view() to produce a table of currents subs and then prompts the user for the name they would like to delete
    before double checking they are sure, then deleting it from the database. If the name does not exist, checked by a for loop, the user is told this and taken back to main.

    calc_next() takes a date and an integer(x) as paramaters and will calculate using relativedelta functions from datetime the next date which is x months after the one given. This was created for adding the next charge date to the SQL database so the users can see when they will next be charged for a given subscriptions.

    check_over() is a function which takes all information from the database and compares the next charge dates against todays date. If the DB date is greater than todays date, the charge date has passed and needs to be calculated again. The calc_next functions is called a new date is generated and updated to the database. This is called when the program starts or after anything is added to ensure the database is up to date.

    format_view_dates() splits a database and rearranges it to a DD/MM/YYYY format for a slightly more user friendly way to view the dates.

    THE GUI

    The menu simply has four tkinter buttons view, add, delete each of which tied to commands to performs the respective functions.

    view() gets all subscriptions and creates a new window using labels for headers and a for loop to create disabled input boxes containing subscription informations. This I found from googling was the best way to create a table like appearance in Tkinter.
    The loop checks if the iterator has reached a date and if so uses format_view_dates to perform its job. If there are no subs it displays a message telling you so.

    add() using input boxes to collect user entry in variables and then a button which uses a lambda command to create a class Sub() of these variables and then insert them into the datebase before closing the window.

    delete() calls view straight away as the root for tkinter so that a table is displayed and input box is created for the user to input the name of the sub they would like to delete. A second box is created with yes or no buttons to make sure they know what they are deleting and if they are sure they would like to do it.


    Overall im very pleased with what I created. My commitment to making a GUI forced me to trawl through tkinter documentation figure out how to make different widgets and grid them on the page. I would like to make it more visually appealing but I think there are better frameworks for carrying out GUI implementation. In hindsight, I do wish I created the functions with the GUI more in mind. I had to add 3 or 4 functions to make the program work for the GUI which rendered some of the others ones redundant. I am also happy that I created a useful class for practice purposes and useability.
