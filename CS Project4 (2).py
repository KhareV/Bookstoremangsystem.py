import matplotlib.pyplot as plt
import numpy as np
import random
from prettytable import PrettyTable, from_csv
from datetime import timedelta, date
import csv
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

admin_data = open('admin_proj.txt', 'r')
admin_info = admin_data.readline().rstrip('\n').split(',')
admin_id = admin_data.readline().rstrip('\n').split(',')
admin_pass = admin_data.readline().rstrip('\n').split(',')
admin_des = admin_data.readline().rstrip('\n').split(',')
admin_goals = admin_data.readline().rstrip('\n').split(',')
admin_sales = admin_data.readline().rstrip('\n').split(',')
admin_data.readline()
admin_data.close()

print("WELCOME!!")
print("_" * 60)
print("BOOKUT Bookstore wishes a lot of happiness, knowledge and prosperity for you.")
print("_" * 60)
iden = input("Are you an admin or a customer?:")

if iden == "admin" or iden == "ADMIN" or iden == "Admin":

    Id = input("Enter the Admin ID:")

    Pass = input("Enter your password:")
    if (Id in admin_id) and (Pass in admin_pass):
        if admin_id.index(Id) == admin_pass.index(Pass):
            print("ADMIN details verified. WELCOME aboard.")
            name = admin_info[admin_id.index(Id)]
            desg = admin_des[admin_id.index(Id)]
            print("Welcome,", name, ", designation:", desg)

            while True:
                print("What do you want to do? (Monthwise Data)")
                print("1. Check Inventory and add books.")
                print("2. Check memberships.")
                print("3. My Monthly goals.")
                print("4. My Sales")
                print("5. Revenue generated (Overall past year)")

                print("6. Add new employee.")
                print("7. Remove Member.")
                print("8. Exit.")
                opt = int(input("Enter your choice:"))
                if opt == 1:
                    print("Inventory:")
                    try:
                        con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                      password='Yogesh@34125')
                        if con.is_connected():
                            db_info = con.get_server_info()
                            print("Connected to MYSQL server", db_info)
                            cursor = con.cursor()
                            query1 = "select * from books1"
                            cursor.execute(query1)
                            rows = cursor.fetchall()

                            print(tabulate(rows, headers=["Sr no", "Books", "Qty", "HSN No", "Price"], tablefmt='psql'))
                            con.close()


                    except Error as e:
                        print("Error")

                    ans21 = input('Do you want to increase the qty of books?:')
                    if ans21 == "yes" or ans21 == "Yes" or ans21 == "YES":

                        try:
                            con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                          password='Yogesh@34125')
                            if con.is_connected():
                                db_info = con.get_server_info()
                                print("Connected to MYSQL server", db_info)
                                cursor = con.cursor()
                                Books = input("Enter the name of the book:")
                                try:
                                    Qty = int(input("Enter the new quantity:"))
                                    print("Quantity:", Qty)
                                except ValueError:
                                    print("Please input integer only...")

                                while True:

                                    if Books in ["Jurassic Park", "Dune", "Nineteen Eighty Four",
                                                 "The Name of the Wind", "The Way of Kings", "The Fifth Season",
                                                 "Pride and Prejudice", "Red White and Royal Blue", "Jane Eyre",
                                                 "Vicious", "Vengeful", "Wolf Hall", "HHhH", "I, Claudius",
                                                 "Frankenstein", "Dracula", "The Shining", "In Cold Blood",
                                                 "Murder On the Orient Express", "Silence of the lambs"]:
                                        query2 = "UPDATE books1 SET Qty=%s WHERE Books=%s"

                                        cursor.execute(query2, (Qty, Books))
                                        con.commit()
                                        print("Columns Updated")
                                        query3 = "select * from books1"
                                        cursor.execute(query3)
                                        break
                                    else:
                                        print("Enter a valid book.")
                                        break




                        except mysql.connector.Error as e:
                            print("Error", format(e))
                    else:
                        print("No problem")

                    continue
                elif opt == 2:
                    print("The list of members:")
                    file_path = "C:/Users/Hp/Downloads/members.txt"
                    csv_file = open(file_path)
                    x = from_csv(csv_file)
                    print(x)

                    while True:
                        ans11 = input('Do you want to add new members?:')
                        if ans11 == "yes" or ans11 == "Yes" or ans11 == "YES":
                            ans12 = "yes"
                            while ans12 == "yes":

                                while True:
                                    try:
                                        srno = int(input("Enter the Unique code:"))
                                        break
                                    except ValueError:
                                        print("Please input integer only...")
                                        continue
                                print("Unique Code:", srno)

                                namez = input("Enter the member name:")
                                while True:
                                    try:
                                        dura = int(input("Enter the duration:"))
                                        break
                                    except ValueError:
                                        print("Please input integer only...")
                                        continue

                                print("Duration:", dura)

                                stat = input("Enter the state of the member:")
                                val33 = True
                                while True:
                                    gender = input("Enter the gender of the member:")

                                    if gender == "Male" or gender == "male" or gender == "Female" or gender == "female" or gender == "Others" or gender == "others":
                                        print(
                                            "Trust us, your privacy is of utmost importance for us and, no information about you about will ever "
                                            "be "
                                            "made public without your consent.")
                                        val33 = True
                                        break

                                    elif gender != "Male" or gender != "male" or gender != "Female" or gender != "female" or gender != "Others" or gender != "others":
                                        print("Error! Enter an eligible gender.")
                                        val33 = False

                                while True:
                                    try:
                                        age = int(input("Enter the age:"))
                                        break
                                    except ValueError:
                                        print("Please input integer only...")
                                        continue

                                print("Age:", age)

                                while True:
                                    try:
                                        dela = int(input("Enter the delay:"))
                                        break
                                    except ValueError:
                                        print("Please input integer only...")
                                        continue

                                print("Delay:", dela)

                                Email = input(
                                    "Enter the member's email ID:")
                                domain = "@gmail.com"
                                if domain in Email:
                                    print("The email entered is:", Email)
                                elif domain not in Email:
                                    print("The email entered is:", Email + domain)

                                while True:

                                    DOBi = input("Enter the DOB (dd/mm):")
                                    if len(DOBi.split("/")) == 1 or DOBi.split("/")[1] not in ["01", "02", "03", "04",
                                                                                               "05", "06", "07", "08",
                                                                                               "09",
                                                                                               "10", "11", "12"] or \
                                            DOBi.split("/")[0] not in ["01", "02", "03", "04", "05", "06", "07", "08",
                                                                       "09",
                                                                       "10", "11", "12", "13", "14", "15", "16", "17",
                                                                       "18", "19", "20", "21", "22", "23", "24", "25",
                                                                       "26", "27", "28", "30", "31"]:
                                        print("Enter a valid value.")
                                        continue
                                    else:
                                        break

                                print("DOB:", DOBi)

                                ans12 = input("Do you want to enter more members?:")
                                file_object = open('members.txt', 'a+', newline='')
                                ewriter = csv.writer(file_object, delimiter=',')
                                ewriter.writerow([srno, namez, dura, stat, gender, age, dela, Email, DOBi])
                                file_object.close()


                            else:
                                print("No problem.")
                                break
                        else:
                            break
                    ans921 = input('Do you want to edit the delay in return of books?:')
                    if ans921 == "yes" or ans921 == "Yes" or ans921 == "YES":

                        file1 = open('members.txt', 'r')
                        Reader = csv.reader(file1)
                        L = []

                        while True:
                            try:
                                ans923 = int(input("Enter the unique code of the member:"))
                                break
                            except ValueError:
                                print("Please input integer only...")
                                continue
                        print("Unique Code:", ans923)
                        ans924 = input("Enter the name of the member:")

                        found = False
                        for Row in Reader:
                            if Row[0] == str(ans923) and Row[1] == ans924:
                                found = True

                                while True:
                                    try:
                                        ans25 = int(input("Enter the new value for the field <'Delay'>:"))
                                        break
                                    except ValueError:
                                        print("Please input integer only...")
                                        continue

                                print("Delay:", ans25)

                                Row[6] = ans25
                            L.append(Row)
                        file1.close()
                        if found == False:
                            print("Member not found.")
                        else:
                            file1 = open('members.txt', 'w+', newline='')
                            Writer = csv.writer(file1)
                            Writer.writerows(L)
                            file1.seek(0)
                            Reader = csv.reader(file1)
                            file1.close()
                        print("The sought field value has been edited.")

                    continue
                elif opt == 3:
                    print("Monthly goals:")
                    try:
                        con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                      password='Yogesh@34125')
                        if con.is_connected():
                            db_info = con.get_server_info()
                            print("Connected to MYSQL server", db_info)
                            cursor = con.cursor()
                            query1 = "select * from books3"
                            cursor.execute(query1)
                            rows = cursor.fetchall()

                            print(tabulate(rows, headers=["Sr no", "Months", "Sales", "Membership Buy-Ins"],
                                           tablefmt='psql'))
                            ans21 = input('Do you want to increase the sales number?:')
                            if ans21 == "yes" or ans21 == "Yes" or ans21 == "YES":

                                try:
                                    con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                                  password='Yogesh@34125')
                                    if con.is_connected():
                                        db_info = con.get_server_info()
                                        print("Connected to MYSQL server", db_info)
                                        cursor = con.cursor()
                                        month = input("Enter the month:")

                                        while True:
                                            try:
                                                sales = int(input("Enter the new value for the field Sales:"))
                                                break
                                            except ValueError:
                                                print("Please input integer only...")
                                                continue

                                        print("New Sales:", sales)
                                        while True:
                                            if month in ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                                         'August', 'September', 'October', 'November', 'December']:
                                                query2 = "UPDATE books3 SET Sales=%s WHERE Months=%s"

                                                cursor.execute(query2, (sales, month))
                                                con.commit()
                                                print("Columns Updated")
                                                query3 = "select * from books3"
                                                cursor.execute(query3)
                                            else:
                                                print("Enter a valid month.")
                                                break


                                except mysql.connector.Error as e:
                                    print("Error", format(e))


                    except Error as e:

                        print("Error")

                    continue
                elif opt == 4:
                    print("Previous Year Sales:")
                    try:
                        con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                      password='Yogesh@34125')
                        if con.is_connected():
                            db_info = con.get_server_info()
                            print("Connected to MYSQL server", db_info)
                            cursor = con.cursor()
                            query1 = "select * from books4"
                            cursor.execute(query1)
                            rows = cursor.fetchall()

                            print(tabulate(rows,
                                           headers=["Sr no", "Months", "Sales", "Membership Buy-Ins", "Merchandise"],
                                           tablefmt='psql'))
                            con.close()
                            ans21 = input('Do you want to increase the sales number?:')
                            if ans21 == "yes" or ans21 == "Yes" or ans21 == "YES":

                                try:
                                    con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                                  password='Yogesh@34125')
                                    if con.is_connected():
                                        db_info = con.get_server_info()
                                        print("Connected to MYSQL server", db_info)
                                        cursor = con.cursor()
                                        month = input("Enter the month:")
                                        while True:
                                            try:
                                                sales = int(input("Enter the new value for the field Sales:"))
                                                break
                                            except ValueError:
                                                print("Please input integer only...")
                                                continue

                                        print("New Sales:", sales)

                                        query2 = "UPDATE books4 SET Sales=%s WHERE Months=%s"

                                        cursor.execute(query2, (sales, month))
                                        con.commit()
                                        print("Columns Updated")
                                        query3 = "select * from books4"
                                        cursor.execute(query3)


                                except mysql.connector.Error as e:
                                    print("Error", format(e))


                    except Error as e:
                        print("Error")

                    continue
                elif opt == 5:
                    print(" Check out the Revenue collections by months (in lacs):")

                    try:
                        con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                      password='Yogesh@34125')
                        if con.is_connected():
                            db_info = con.get_server_info()
                            print("Connected to MYSQL server", db_info)
                            cursor = con.cursor()
                            query1 = "select * from score"
                            cursor.execute(query1)
                            rows = cursor.fetchall()

                            print(tabulate(rows,
                                           headers=["Months", "Vedant Khare", "Mohit Soni", "Pritam Rana", "Parv Dhar",
                                                    "Garima Dua", "Aparna Mittal"], tablefmt='psql'))
                            con.close()



                    except Error as e:
                        print("Error")

                    continue
                elif opt == 6:
                    ans55 = input("Enter the name of the new employee:")
                    ans56 = input("Enter the user ID:")

                    val = True
                    while True:
                        ans57 = input("Enter the user password:")
                        SpecialSym = ['$', '@', '#', '%']

                        if len(ans57) < 6:
                            print('length should be at least 6.')
                            val = False

                        if len(ans57) > 20:
                            print('length should be not be greater than 8.')
                            val = False

                        if not any(char.isdigit() for char in ans57):
                            print('Password should have at least one numeral.')
                            val = False

                        if not any(char.isupper() for char in ans57):
                            print('Password should have at least one uppercase letter.')
                            val = False

                        if not any(char.islower() for char in ans57):
                            print('Password should have at least one lowercase letter.')
                            val = False

                        if not any(char in SpecialSym for char in ans57):
                            print('Password should have at least one of the symbols $@#.')
                            val = False
                        else:
                            print("Password is valid")
                            break

                    ans58 = input("Enter the user designation:")
                    ans551 = ans55.split()
                    ans561 = ans56.split()
                    ans571 = ans57.split()
                    ans581 = ans58.split()

                    with open('admin_proj.txt', 'w') as admin_data:
                        admin_info += ans551
                        admin_id += ans561
                        admin_pass += ans571
                        admin_des += ans581

                        admin_data.write(','.join(map(str, admin_info)) + '\n')
                        admin_data.write(','.join(map(str, admin_id)) + '\n')
                        admin_data.write(','.join(map(str, admin_pass)) + '\n')
                        admin_data.write(','.join(map(str, admin_des)) + '\n')

                    print("Welcome ", ans55, ", we look forward towards working with you.")
                    continue
                elif opt == 7:
                    file1 = open('members.txt', 'r')
                    Reader = csv.reader(file1)
                    L1 = []

                    while True:
                        try:
                            ans236 = int(input("Enter the unique code of the member to be deleted:"))
                            break
                        except ValueError:
                            print("Please input integer only...")
                            continue
                    print("Unique Code:", ans236)
                    ans237 = input("Enter the name of the member:")

                    found = False
                    for Row in Reader:
                        if Row[0] == str(ans236) and Row[1] == ans237:
                            print("Membership removed for ", Row[1])
                            found = True
                        else:
                            L1.append(Row)
                    file1.close()
                    if found == False:
                        print("Member not found.")
                    else:
                        file1 = open('members.txt', 'w+', newline='')
                        Writer = csv.writer(file1)
                        Writer.writerows(L1)
                        file1.seek(0)
                        Reader = csv.reader(file1)
                        file1.close()

                    continue




                elif opt == 8:
                    print("I hope you got what you were looking for. Have a nice day.")
                    break
    else:
        print("Incorrect ID or password.")


elif iden == "customer" or iden == "CUSTOMER" or iden == "Customer":

    while True:
        ch23 = input("Are you a member?:")
        if ch23 == "yes" or ch23 == "YES" or ch23 == "Yes":
            name = input("Can you provide us with a name?:")
            
            while True:
                try:
                    unique_cde = int(input("Enter your Code:"))
                    break
                except ValueError:
                    print("Please input integer only...")
                    continue

            
            unique_cde1 = str(unique_cde)
            emai = input("Enter the email:")
            file1 = open('members.txt', 'r')
            Reader = csv.reader(file1)

            for Row in Reader:
                if Row[0] == unique_cde1 and Row[1] == str(name) and Row[7] == str(emai):
                    print("Welcome,", name, ", State:", Row[3], ", Gender:", Row[4], ", Age:", Row[5])
                    print("CONFIRMING you are not a bot")
                    captcha = random.randrange(0, 10000000)
                    print("The unique code is:", captcha)
                    
                    
                    while True:
                        try:
                            capent = int(input("Enter the unique code displayed on your screen:"))
                            break
                        except ValueError:
                            print("Please input integer only...")
                            continue
                    if capent == captcha:

                        print("Success! WELCOME TO OUR SITE")
                        print(
                            '''This season genre of book does not decide the cost. As we believe in equality! Hence, 
equal cost on all books as a gesture of gratitude for supporting us even during the 
pandemic''')
                        print("What can we do for you", name, "?")
                        ch = 0

                        while ch < 2:
                            print("1. WELL help me with a book.")
                            print("2. Leave me in peace so I can order an icecream.")
                            print("*" * 60)
                            ch = int(input("Enter your choice:"))
                            if ch == 1:

                                print("Tell me what kind of you like. WE have a truckload of knowledge for you:")
                                print("a. Action, marked Rs. 299, Rent Rs. 99")
                                print("b. Fantasy, marked Rs. 299, Rent Rs. 99")
                                print("c. Romance, marked Rs. 299, Rent Rs. 99")
                                print("d. Superhero, marked Rs. 299, Rent Rs. 99")

                                print("e. History, marked Rs. 299, Rent Rs. 99")
                                print("f. Horror, marked Rs. 299, Rent Rs. 99")

                                print("g. Crime, marked Rs. 299, Rent Rs. 99")
                                print(
                                    "The various perks with the books will include exclusive book marks, wristbands "
                                    "and mugs (cost "
                                    "included)")
                                print("*" * 60)

                                ans = "yes"
                                books = []

                                while ans == "yes" and ans != "":
                                    ans1 = input("Enter the serial alphabet of your genre:")
                                    print("WE JUST HAVE THE BOOKS FOR YOU.")
                                    print(
                                        "Our choice of books are placed for your just and thorough approval. We sincerely hope you "
                                        "like "
                                        "them.")
                                    print("\n" * 1)
                                    if ans1 == "a":
                                        print("The three select books are the following:")
                                        print("\n" * 2)

                                        print('''I. Jurassic Park: Jurassic Park is a 1990 science fiction novel written by Michael 
Crichton. A cautionary tale about genetic engineering, it presents the collapse of an 
amusement park showcasing genetically re-created dinosaurs to illustrate the mathematical 
concept of chaos theory and its real-world implications. A sequel titled The Lost World, 
also written by Crichton, was published in 1995. In 1997, both novels were re-published as 
a single book titled Michael Crichton's Jurassic World.''')
                                        print("\n" * 2)

                                        print('''II. Dune: Dune is a 1965 science fiction novel by American author Frank Herbert, 
originally published as two separate serials in Analog magazine. It tied with Roger 
Zelazny's This Immortal for the Hugo Award in 1966 and it won the inaugural Nebula Award 
for Best Novel. It is the first installment of the Dune saga. In 2003, it was described as 
the world's best-selling science fiction novel.''')
                                        print("\n" * 2)
                                        print('''III. Nineteen Eighty-Four: Nineteen Eighty-Four (also stylised as 1984) is a dystopian 
social science fiction novel and cautionary tale written by English writer George Orwell. 
It was published on 8 June 1949 by Secker & Warburg as Orwell's ninth and final book 
completed in his lifetime. Thematically, it centres on the consequences of 
totalitarianism, mass surveillance and repressive regimentation of people and behaviours 
within society. Orwell, a democratic socialist, modelled the totalitarian government in 
the novel after Stalinist Russia and Nazi Germany. More broadly, 
the novel examines the role of truth and facts within politics and the ways in which they 
are manipulated.''')

                                        print("*" * 60)
                                    if ans1 == "b":
                                        print('''I. The Name of the Wind: he Kingkiller Chronicle takes place in the fictional world of 
Temerant, a large continent of which the known part, called the Four Corners of 
Civilization, is divided into several distinct nations and cultures. Much of the world 
follows a religion similar, though not identical, to medieval Christianity. Coexisting 
alongside the mortal world is the realm of The Fae, a parallel universe inhabited by 
supernatural creatures which can move between the two realms only when the moon is full. 
Magic exists in Temerant, too, but obeys a well-defined set of rules and principles that 
can only be exploited by those who have trained in its professional and scientific use.As 
the novel begins, the reader hears an old storyteller speaking of a famous old wizard 
called Taborlin the Great, who was captured by evil beings called the Chandrian. Escaping 
them, Taborlin fell from a great height—but since he knew the 'Name of the Wind', 
he called it and the Wind came and set him down safely. In later parts of the book, 
characters are often skeptical of such stories. Some kinds of magic are taught in the 
University as academic disciplines and have daily-life applications.''')
                                        print("\n" * 2)
                                        print('''II. The Way of Kings: The story rotates between the points of view of Kaladin, Shallan 
Davar, Szeth-son-son-Vallano, Dalinar Kholin, Adolin Kholin, and several other minor 
characters, who lead seemingly unconnected lives. Szeth, a Shin man cast out by his people 
and condemned to obey his constantly changing masters, is sent to assassinate the king of 
one of the world's most powerful nations, Alethkar. As the story progresses, 
he continuously changes hands, doing his best to hide the fact that he possesses an 
Honorblade, a mythical blade used by the Heralds that can cut through any material.''')
                                        print("\n" * 2)
                                        print('''III. The Fifth season: The Fifth Season takes place on a planet with a single 
supercontinent called the Stillness. Every few centuries, its inhabitants endure what they 
call a 'Fifth Season' of catastrophic climate change.''')

                                        print("*" * 60)
                                    if ans1 == "c":
                                        print('''I. Pride and Prejudice: Pride and Prejudice is an 1813 novel of manners written by Jane 
Austen. Though it is mostly called a romantic novel, it is also a satire. The novel 
follows the character development of Elizabeth Bennet, the dynamic protagonist of the book 
who learns about the repercussions of hasty judgments and comes to appreciate the 
difference between superficial goodness and actual goodness. Mr. Bennet, owner of the 
Longbourn estate in Hertfordshire, has five daughters, but his property is entailed and 
can only be passed to a male heir. His wife also lacks an inheritance, so his family faces 
becoming very poor upon his death. Thus, it is imperative that at least one of the girls 
marry well to support the others, which is a motivation that drives the plot. Pride and 
Prejudice has consistently appeared near the top of lists of 'most-loved books' among 
literary scholars and the reading public. It has become one of the most popular novels in 
English literature, with over 20 million copies sold, and has inspired many derivatives in 
modern literature. For more than a century, dramatic adaptations, reprints, 
unofficial sequels, films, and TV versions of Pride and Prejudice have portrayed the 
memorable characters and themes of the novel, reaching mass audiences.''')
                                        print("\n" * 2)
                                        print('''II. Red, White and Royal Blue: Red, White & Royal Blue is a 2019 LGBT romance novel by 
Casey McQuiston. The novel centres around the character of Alex Claremont-Diaz, 
the First Son of the United States, and his relationship with Prince Henry, 
a British prince.''')
                                        print("\n" * 2)
                                        print('''III. Jane Eyre: The novel revolutionised prose fiction by being the first to focus 
on its protagonist's moral and spiritual development through an intimate first-person 
narrative, where actions and events are coloured by a psychological intensity. Charlotte 
Brontë has been called the 'first historian of the private consciousness', and the literary 
ancestor of writers like Proust and Joyce. The book contains elements of social criticism 
with a strong sense of Christian morality at its core, and it is considered by many to be 
ahead of its time because of Jane's individualistic character and how the novel approaches 
the topics of class, sexuality, religion, and feminism. It, along with Jane Austen's Pride 
and Prejudice, is one of the most famous romance novels of all time.''')
                                        print("*" * 60)
                                    if ans1 == "d":
                                        print('''I. Vicious: Vicious is a fantasy novel by American author V. E. Schwab published by Tor 
Books in 2013, focused around two college students who learn how to create superhuman 
abilities and later become archenemies.''')
                                        print("\n" * 2)
                                        print('''II. Renegade: Renegades follows Nova (anarchist alias: Nightmare), the niece of the 
Anarchist leader, Alec Artino (alias: Ace Anarchy). Alec takes Nova in after her parents 
are viciously murdered by another villain gang before the civil war, and was raised by the 
Anarchists. She can put people to sleep with skin-to-skin contact, and since her parents'
murder, she has not slept at all. She wants revenge on the Renegades for not protecting 
her parents as promised, and leads an infiltration into their headquarters by posing as a 
Renegade-in-training. It also follows Adrian, the son of the leaders of the Renegades, 
Hugh Everhart and Simon Westwood. He was adopted by the two leaders after his mother, 
another member of the core-Renegades, was killed. He brings Nova onto his team at 
Renegades headquarters as she poses as 'Insomnia'.''')
                                        print("\n" * 2)
                                        print('''III. Vengeful: The sequel to VICIOUS, V.E. Schwab's first adult novel. Sydney once had 
Serena—beloved sister, betrayed enemy, powerful ally. But now she is alone, except for her 
thrice-dead dog, Dol, and then there's Victor, who thinks Sydney doesn't know about his 
most recent act of vengeance. Victor himself is under the radar these days—being buried 
and re-animated can strike concern even if one has superhuman powers. But despite his own 
worries, his anger remains. And Eli Ever still has yet to pay for the evil he has done.''')
                                        print("*" * 60)
                                    if ans1 == "e":
                                        print('''I. Wolf Hall: Wolf Hall is a 2009 historical novel by English author Hilary Mantel, 
published by Fourth Estate, named after the Seymour family's seat of Wolfhall, 
or Wulfhall, in Wiltshire. Set in the period from 1500 to 1535, Wolf Hall is a sympathetic 
fictionalised biography documenting the rapid rise to power of Thomas Cromwell in the 
court of Henry VIII through to the death of Sir Thomas More. The novel won both the Man 
Booker Prize and the National Book Critics Circle Award. In 2012, The Observer named 
it as one of 'The 10 best historical novels'.''')
                                        print("\n" * 2)
                                        print('''II. HHhH: HHhH is the debut novel of French author Laurent Binet, published in 2010 by 
Grasset & Fasquelle. The book recounts Operation Anthropoid, the assassination of Nazi 
leader Reinhard Heydrich in Prague during World War II. The novel was awarded the 2010 
Prix Goncourt du Premier Roman.''')
                                        print("\n" * 2)
                                        print('''III. I, Claudius: I, Claudius is a historical novel by English writer Robert Graves, 
published in 1934. Written in the form of an autobiography of the Roman Emperor Claudius, 
it tells the history of the Julio-Claudian dynasty and the early years of the Roman 
Empire, from Julius Caesar's assassination in 44 BC to Caligula's assassination in AD 41. 
Though the narrative is largely fictionalized, most of the events depicted are drawn from 
historical accounts of the same time period by the Roman historians Suetonius and Tacitus.''')
                                        print("*" * 60)
                                    if ans1 == "f":
                                        print('''I. Frankenstein: Frankenstein; or, The Modern Prometheus is an 1818 novel written by 
English author Mary Shelley. Frankenstein tells the story of Victor Frankenstein, 
a young scientist who creates a sapient creature in an unorthodox scientific experiment. 
Shelley started writing the story when she was 18, and the first edition was published 
anonymously in London on 1 January 1818, when she was 20. Her name first appeared in the 
second edition, which was published in Paris in 1821. Shelley travelled through Europe in 
1815 along the river Rhine in Germany, stopping in Gernsheim, 17 kilometres (11 mi) away 
from Frankenstein Castle, where two centuries before, an alchemist engaged in experiments. 
She then journeyed to the region of Geneva, Switzerland, where much of the story takes 
place. Galvanism and occult ideas were topics of conversation among her companions, 
particularly her lover and future husband Percy B. Shelley. In 1816, Mary, Percy and Lord 
Byron had a competition to see who could write the best horror story. After thinking 
for days, Shelley was inspired to write Frankenstein after imagining a scientist who 
created life and was horrified by what he had made''')
                                        print("\n" * 2)
                                        print('''II. Dracula: Dracula is a novel by Bram Stoker, published in 1897. As an epistolary novel, 
the narrative is related through letters, diary entries, and newspaper articles. It has no 
single protagonist, but opens with solicitor Jonathan Harker taking a business trip to 
stay at the castle of a Transylvanian noble, Count Dracula. Harker escapes the castle 
after discovering that Dracula is a vampire, and the Count moves to England and plagues 
the seaside town of Whitby. A small group, led by Abraham Van Helsing, hunt Dracula and, 
in the end, kill him. Dracula was mostly written in the 1890s. Stoker produced over a 
hundred pages of notes for the novel, drawing extensively from Transylvanian folklore and 
history. Some scholars have suggested that the character of Dracula was inspired by 
historical figures like the Wallachian prince Vlad the Impaler or the countess Elizabeth 
Báthory, but there is widespread disagreement. Stoker's notes mention neither figure. He 
found the name Dracula in Whitby's public library while holidaying there, picking it 
because he thought it meant devil in Romanian.''')
                                        print("\n" * 2)
                                        print('''III. The Shining: The Shining is a 1977 horror novel by American author Stephen King. It 
is King's third published novel and first hardback bestseller; its success firmly 
established King as a preeminent author in the horror genre. The setting and characters 
are influenced by King's personal experiences, including both his visit to The Stanley 
Hotel in 1974 and his struggle with alcoholism. The novel was adapted into a 1980 film of 
the same name. The book was followed by a sequel, Doctor Sleep, published in 2013, 
which was adapted into a film of the same name. The Shining centers on the life of Jack 
Torrance, a struggling writer and recovering alcoholic who accepts a position as the 
off-season caretaker of the historic Overlook Hotel in the Colorado Rockies. His family 
accompanies him on this job, including his young son Danny Torrance, who possesses 'the 
shining', an array of psychic abilities that allow Danny to see the hotel's horrific past. 
Soon, after a winter storm leaves them snowbound, the supernatural forces inhabiting the 
hotel influence Jack's sanity, leaving his wife and son in incredible danger.''')
                                        print("*" * 60)
                                    if ans1 == "g":
                                        print('''I. In Cold Blood: In Cold Blood is a non-fiction novel by American author Truman Capote, 
first published in 1966. It details the 1959 murders of four members of the Herbert 
Clutter family in the small farming community of Holcomb, Kansas. Capote learned of the 
quadruple murder before the killers were captured, and he traveled to Kansas to write 
about the crime. He was accompanied by his childhood friend and fellow author Harper Lee, 
and they interviewed residents and investigators assigned to the case and took thousands 
of pages of notes. Killers Richard Hickock and Perry Smith were arrested six weeks after
the murders and later executed by the state of Kansas. Capote ultimately spent six years 
working on the book. In Cold Blood was an instant success and is the second-best-selling
true crime book in history, behind Vincent Bugliosi's Helter Skelter (1974) about the 
Charles Manson murders.''')
                                        print("\n" * 2)
                                        print('''II. Murder on the Orient Express: The elegant train of the 1960s, the Orient Express, 
is stopped by heavy snowfall. A murder is discovered, and Poirot's trip home to London 
from the Middle East is interrupted to solve the case. The opening chapters of the novel 
take place in Istanbul. The rest of the novel takes place in Yugoslavia, with the train 
trapped between Vinkovci and Brod.''')
                                        print("\n" * 2)
                                        print('''III. Silence of the lambs: The Silence of the Lambs is a psychological horror novel by 
Thomas Harris. First published in 1988, it is the sequel to Harris's 1981 novel Red 
Dragon. Both novels feature the cannibalistic serial killer Dr. Hannibal Lecter, 
this time pitted against FBI Special Agent Clarice Starling. Its film adaptation directed 
by Jonathan Demme was released in 1991 to widespread critical acclaim and box office 
success. It won the Academy Award for Best Picture.''')
                                        print("*" * 60)
                                        print("\n" * 2)
                                    if ans1 == "":
                                        print("You have not filled the field. Kindly enter a valid choice.")
                                        continue

                                    books1 = []
                                    n1 = int(input("Enter the number of books:"))
                                    if n1 > 3:
                                        print("Enter a valid value")
                                    else:
                                        for a in range(n1):
                                            elem1 = input(
                                                "Enter the book you have chosen, in the way they are mentioned above:")
                                            elem2 = list(elem1)
                                            books1.append(elem1)
                                        print("The books you have chosen are:", books1)
                                        books += books1

                                        ans = input("WANT to enter books from other genres. Type yes or no:")
                                else:
                                    print("The books you have developed a liking upon are:", books)
                                    ans2 = input("Are these your final books. Type yes or no:")
                                    if ans2 == "yes":
                                        print("Let's cut you on some costs.")
                                    if ans2 == "no":
                                        ch1 = input("DO you want to restart? Type yes or no:")
                                        if ch1 == "yes":
                                            print("Last chance, alright? Just kidding! Shop all you want!")
                                            print("\n" * 4)
                                            continue
                                        else:

                                            print("Let's help you delete some books!")

                                            ans3 = "yes"
                                            while ans3 == "yes":

                                                item0 = int(input("Enter the position of the book to be removed:"))
                                                item = item0 - 1
                                                books.pop(item)
                                                print("The new list of books is:", books)
                                                ans3 = input("DO you want to delete some more books?. Type yes or no")




                                            else:
                                                print("The new order of books is:", books)
                                                print("*" * 60)
                                                print("\n" * 4)
                                                print("*" * 60)

                                # Cost analysis

                                print(
                                    "The total cost of your past time and hour of solitude will be appearing as fast as one of Harvey "
                                    "Spector's cocky, yet iconic quotes")

                                print("*" * 60)
                                print("\n" * 2)
                                ans4 = input("DO you want to buy or rent books?:")

                                if ans4 == "BUY" or ans4 == "Buy" or ans4 == "buy":

                                    tax = (len(books) * 299) / 11

                                    perks = len(books) * 299 / 23
                                    memded = int(len(books) * 4)

                                    cost = int(len(books) * 299 + tax + perks)
                                    cost -= memded
                                elif ans4 == "RENT" or ans4 == "Rent" or ans4 == "rent":
                                    tmeper = int(input("Enter the time period for renting (in number of days):"))
                                    tax = (len(books) * 99) / 11
                                    perks = len(books) * 99 / 15
                                    bookcare = len(books) * 2
                                    memded = int(len(books) * 12)
                                    date1 = date.today() + timedelta(days=tmeper)
                                    print("Starting Date:", date.today())
                                    print("Rental till:", date1)

                                    cost = int(len(books) * 99 + tax + perks + bookcare)
                                    cost -= memded
                                    print("*" * 60)

                                print("\n" * 2)
                                print("Your delay is:", Row[6])
                                addcost = (int(Row[6]) * 2.5)
                                cost += addcost
                                print("\n" * 1)
                                try:
                                    con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                                  password='Yogesh@34125')
                                    if con.is_connected():
                                        db_info = con.get_server_info()
                                        print("Connected to MYSQL server", db_info)
                                        cursor = con.cursor()
                                        for i in books:
                                            query2 = "UPDATE books1 SET Qty=Qty-1 WHERE Books='{}'".format(i)

                                            cursor.execute(query2)
                                            con.commit()
                                        print("Columns Updated")
                                        query3 = "select * from books1"
                                        cursor.execute(query3)


                                except mysql.connector.Error as e:
                                    print("Error", format(e))

                                print(
                                    "(THE costs of any delays will be added to any future rents or purchases from our "
                                    "store) ")
                                print("The cost will be: Rs ", cost)
                                add = input("Kindly enter the address:")

                                print("Your unique book code for the order will be:", random.randrange(0, 12000))
                                code = random.randrange(0, 340)
                                print("You can track and inquire about the order with the help of the store code:",
                                      code)

                                print("Your email is:", Row[7])

                                print("*" * 60)
                                print("\n" * 2)
                                print("Your DOB is:", Row[8])
                                while True:
                                    try:
                                        cont = int(input("Enter the mobile number:"))
                                    except ValueError:
                                        print("Please enter a number.")
                                        continue
                                    if len(str(cont)) > int(10) or len(str(cont)) < int(10):
                                        print("Please enter a valid number contining 10-digits.")
                                    else:
                                        break
                                if len(str(cont)) == int(10):
                                    print("The number entered is valid.")

                                print(
                                    "----------------------------------------RECEIPT---------------------------------------------")
                                print("\n" * 3)

                                print('----------------------Welcome To Bookut----------------------')
                                print('-----------BOOKUT PVT. LIM., BOSTON, MASSACHUSETTS-----------')

                                print('----------------------Order Code:', random.randrange(0, 360),
                                      "-----------------------")
                                print('-----------------------Mobile: 123XXX -----------------------')
                                x = PrettyTable()
                                x.field_names = ['Books', 'Price (excluding taxes and deductions)', 'Taxes']
                                for z in range(0, len(books)):
                                    taxesz = int(tax) / 2
                                    x.add_row([books[z], 'Rs 299', taxesz])

                                print(x)

                                print("\n" * 1)
                                print("The total cost is: Rs ", cost)
                                print("\n" * 1)

                                print(
                                    "Thanks for ordering from us and making ours, as well as a child's day,in Africa battling hunger "
                                    "as "
                                    "we donate 10 percent of what we earn for helping the poor and needy.")
                                print("*" * 60)
                                print("\n" * 5)
                                print("*" * 60)
                                print(" Check out the POPULARITY BY BOOKS:")
                                height = [23, 12, 15, 18, 45, 32, 32, 21, 32, 22, 12, 29, 35, 22, 10, 35, 43, 19, 32,
                                          43, 41]
                                bars = ('Jurassic Park', 'Dune', 'Nineteen Eighty-Four', 'The Name of the Wind',
                                        'The Way of Kings',
                                        'The Fifth season',
                                        'Pride and Prejudice', 'Red, White and Royal Blue', 'Jane Eyre', 'Vicious',
                                        'Renegade',
                                        'Vengeful',
                                        'Wolf Hall',
                                        'HHhH', 'I, Claudius', 'Frankenstein', 'Dracula', 'The Shining',
                                        'In Cold Blood',
                                        'Murder on the Orient Express', 'Silence of the lambs')

                                x_pos = np.arange(len(bars))

                                # Create bars
                                plt.bar(x_pos, height, color=(0.5, 0.1, 0.5, 0.6))
                                plt.title('POPULARITY BY BOOKS')
                                plt.xlabel('Books')
                                plt.ylabel('Popularity')

                                # Create names on the x-axis
                                plt.xticks(x_pos, bars, rotation=90)
                                plt.subplots_adjust(bottom=0.4, top=0.99)

                                # Show graphic
                                plt.show()

                                break
                            else:
                                print("Thanks for visiting our site and giving us a chance to prove us.")
                                print("*" * 60)
                                print("\n" * 5)
                                print("*" * 60)
                    else:
                        print("Your request has been denied. Please try again later.")
                        print("*" * 60)
                        print("\n" * 5)
                        print("*" * 60)
                        break



            else:
                print("Details could not be verified.")
                break

        elif ch23 == "no" or ch23 == "NO" or ch23 == "No":
            print("A membership will be an important addition to how to you buy and read books, and make you "
                  "entitled to various offers that we provide.")
            name = input("Can you provide us with a name?")
            
            
            while True:
                try:
                    age = int(input("It would be great if we would have your age:"))
                    break
                except ValueError:
                    print("Please input integer only...")
                    continue
            invalid_input = True


            def start():
                global invalid_input
                gender = input("Gender surely plays a part in your choice of books (Male, Female and Others):) :-")
                if gender == "Male" or gender == "male" or gender == "Female" or gender == "female" or gender == "Others" or gender == "others":
                    print(
                        "Trust us, your privacy is of utmost importance for us and, no information about you about will ever "
                        "be "
                        "made public without your consent.")
                    invalid_input = False
                else:
                    print("Error! Enter an eligible gender.")


            while invalid_input:
                start()

            print("CONFIRMING you are not a bot")
            captcha = random.randrange(0, 10000000)
            print("The unique code is:", captcha)
            
            while True:
                try:
                    capent = int(input("Enter the unique code displayed on your screen:"))
                    break
                except ValueError:
                    print("Please input integer only...")
                    continue
            if capent == captcha:

                print("Success! WELCOME TO OUR SITE")
                print(
                    '''This season genre of book does not decide the cost. As we believe in equality! Hence, equal cost on all 
books as a gesture of gratitude for supporting us even during the pandemic''')
                print("What can we do for you", name, "?")
                ch = 0

                while ch < 2:
                    print("1. WELL help me with a book.")
                    print("2. Leave me in peace so I can order an icecream.")
                    print("*" * 60)
                    ch = int(input("Enter your choice:"))
                    if ch == 1:

                        print("Tell me what kind of you like. WE have a truckload of knowledge for you:")
                        print("a. Action, marked Rs. 299, Rent Rs. 99")
                        print("b. Fantasy, marked Rs. 299, Rent Rs. 99")
                        print("c. Romance, marked Rs. 299, Rent Rs. 99")
                        print("d. Superhero, marked Rs. 299, Rent Rs. 99")

                        print("e. History, marked Rs. 299, Rent Rs. 99")
                        print("f. Horror, marked Rs. 299, Rent Rs. 99")

                        print("g. Crime, marked Rs. 299, Rent Rs. 99")
                        print(
                            "The various perks with the books will include exclusive book marks, wristbands and mugs (cost "
                            "included)")
                        print("*" * 60)

                        ans = "yes"
                        books = []

                        while ans == "yes" and ans != "":
                            ans1 = input("Enter the serial alphabet of your genre:")
                            print("WE JUST HAVE THE BOOKS FOR YOU.")
                            print(
                                "Our choice of books are placed for your just and thorough approval. We sincerely hope you "
                                "like "
                                "them.")
                            print("\n" * 1)
                            if ans1 == "a":
                                print("The three select books are the following:")
                                print("\n" * 2)

                                print('''I. Jurassic Park: Jurassic Park is a 1990 science fiction novel written by Michael 
Crichton. A cautionary tale about genetic engineering, it presents the collapse of an 
amusement park showcasing genetically re-created dinosaurs to illustrate the mathematical 
concept of chaos theory and its real-world implications. A sequel titled The Lost World, 
also written by Crichton, was published in 1995. In 1997, both novels were re-published as 
a single book titled Michael Crichton's Jurassic World.''')
                                print("\n" * 2)

                                print('''II. Dune: Dune is a 1965 science fiction novel by American author Frank Herbert, 
originally published as two separate serials in Analog magazine. It tied with Roger 
Zelazny's This Immortal for the Hugo Award in 1966 and it won the inaugural Nebula Award 
for Best Novel. It is the first installment of the Dune saga. In 2003, it was described as 
the world's best-selling science fiction novel.''')
                                print("\n" * 2)
                                print('''III. Nineteen Eighty-Four: Nineteen Eighty-Four (also stylised as 1984) is a dystopian 
social science fiction novel and cautionary tale written by English writer George Orwell. 
It was published on 8 June 1949 by Secker & Warburg as Orwell's ninth and final book 
completed in his lifetime. Thematically, it centres on the consequences of 
totalitarianism, mass surveillance and repressive regimentation of people and behaviours 
within society. Orwell, a democratic socialist, modelled the totalitarian government in 
the novel after Stalinist Russia and Nazi Germany. More broadly, 
the novel examines the role of truth and facts within politics and the ways in which they 
are manipulated.''')

                                print("*" * 60)
                            if ans1 == "b":
                                print('''I. The Name of the Wind: he Kingkiller Chronicle takes place in the fictional world of 
Temerant, a large continent of which the known part, called the Four Corners of 
Civilization, is divided into several distinct nations and cultures. Much of the world 
follows a religion similar, though not identical, to medieval Christianity. Coexisting 
alongside the mortal world is the realm of The Fae, a parallel universe inhabited by 
supernatural creatures which can move between the two realms only when the moon is full. 
Magic exists in Temerant, too, but obeys a well-defined set of rules and principles that 
can only be exploited by those who have trained in its professional and scientific use.As 
the novel begins, the reader hears an old storyteller speaking of a famous old wizard 
called Taborlin the Great, who was captured by evil beings called the Chandrian. Escaping 
them, Taborlin fell from a great height—but since he knew the 'Name of the Wind', 
he called it and the Wind came and set him down safely. In later parts of the book, 
characters are often skeptical of such stories. Some kinds of magic are taught in the 
University as academic disciplines and have daily-life applications.''')
                                print("\n" * 2)
                                print('''II. The Way of Kings: The story rotates between the points of view of Kaladin, Shallan 
Davar, Szeth-son-son-Vallano, Dalinar Kholin, Adolin Kholin, and several other minor 
characters, who lead seemingly unconnected lives. Szeth, a Shin man cast out by his people 
and condemned to obey his constantly changing masters, is sent to assassinate the king of 
one of the world's most powerful nations, Alethkar. As the story progresses, 
he continuously changes hands, doing his best to hide the fact that he possesses an 
Honorblade, a mythical blade used by the Heralds that can cut through any material.''')
                                print("\n" * 2)
                                print('''III. The Fifth season: The Fifth Season takes place on a planet with a single 
supercontinent called the Stillness. Every few centuries, its inhabitants endure what they 
call a 'Fifth Season' of catastrophic climate change.''')

                                print("*" * 60)
                            if ans1 == "c":
                                print('''I. Pride and Prejudice: Pride and Prejudice is an 1813 novel of manners written by Jane 
Austen. Though it is mostly called a romantic novel, it is also a satire. The novel 
follows the character development of Elizabeth Bennet, the dynamic protagonist of the book 
who learns about the repercussions of hasty judgments and comes to appreciate the 
difference between superficial goodness and actual goodness. Mr. Bennet, owner of the 
Longbourn estate in Hertfordshire, has five daughters, but his property is entailed and 
can only be passed to a male heir. His wife also lacks an inheritance, so his family faces 
becoming very poor upon his death. Thus, it is imperative that at least one of the girls 
marry well to support the others, which is a motivation that drives the plot. Pride and 
Prejudice has consistently appeared near the top of lists of 'most-loved books' among 
literary scholars and the reading public. It has become one of the most popular novels in 
English literature, with over 20 million copies sold, and has inspired many derivatives in 
modern literature. For more than a century, dramatic adaptations, reprints, 
unofficial sequels, films, and TV versions of Pride and Prejudice have portrayed the 
memorable characters and themes of the novel, reaching mass audiences.''')
                                print("\n" * 2)
                                print('''II. Red, White and Royal Blue: Red, White & Royal Blue is a 2019 LGBT romance novel by 
Casey McQuiston. The novel centres around the character of Alex Claremont-Diaz, 
the First Son of the United States, and his relationship with Prince Henry, 
a British prince.''')
                                print("\n" * 2)
                                print('''III. Jane Eyre: The novel revolutionised prose fiction by being the first to focus 
on its protagonist's moral and spiritual development through an intimate first-person 
narrative, where actions and events are coloured by a psychological intensity. Charlotte 
Brontë has been called the 'first historian of the private consciousness', and the literary 
ancestor of writers like Proust and Joyce. The book contains elements of social criticism 
with a strong sense of Christian morality at its core, and it is considered by many to be 
ahead of its time because of Jane's individualistic character and how the novel approaches 
the topics of class, sexuality, religion, and feminism. It, along with Jane Austen's Pride 
and Prejudice, is one of the most famous romance novels of all time.''')
                                print("*" * 60)
                            if ans1 == "d":
                                print('''I. Vicious: Vicious is a fantasy novel by American author V. E. Schwab published by Tor 
Books in 2013, focused around two college students who learn how to create superhuman 
abilities and later become archenemies.''')
                                print("\n" * 2)
                                print('''II. Renegade: Renegades follows Nova (anarchist alias: Nightmare), the niece of the 
Anarchist leader, Alec Artino (alias: Ace Anarchy). Alec takes Nova in after her parents 
are viciously murdered by another villain gang before the civil war, and was raised by the 
Anarchists. She can put people to sleep with skin-to-skin contact, and since her parents'
murder, she has not slept at all. She wants revenge on the Renegades for not protecting 
her parents as promised, and leads an infiltration into their headquarters by posing as a 
Renegade-in-training. It also follows Adrian, the son of the leaders of the Renegades, 
Hugh Everhart and Simon Westwood. He was adopted by the two leaders after his mother, 
another member of the core-Renegades, was killed. He brings Nova onto his team at 
Renegades headquarters as she poses as 'Insomnia'.''')
                                print("\n" * 2)
                                print('''III. Vengeful: The sequel to VICIOUS, V.E. Schwab's first adult novel. Sydney once had 
Serena—beloved sister, betrayed enemy, powerful ally. But now she is alone, except for her 
thrice-dead dog, Dol, and then there's Victor, who thinks Sydney doesn't know about his 
most recent act of vengeance. Victor himself is under the radar these days—being buried 
and re-animated can strike concern even if one has superhuman powers. But despite his own 
worries, his anger remains. And Eli Ever still has yet to pay for the evil he has done.''')
                                print("*" * 60)
                            if ans1 == "e":
                                print('''I. Wolf Hall: Wolf Hall is a 2009 historical novel by English author Hilary Mantel, 
published by Fourth Estate, named after the Seymour family's seat of Wolfhall, 
or Wulfhall, in Wiltshire. Set in the period from 1500 to 1535, Wolf Hall is a sympathetic 
fictionalised biography documenting the rapid rise to power of Thomas Cromwell in the 
court of Henry VIII through to the death of Sir Thomas More. The novel won both the Man 
Booker Prize and the National Book Critics Circle Award. In 2012, The Observer named 
it as one of 'The 10 best historical novels'.''')
                                print("\n" * 2)
                                print('''II. HHhH: HHhH is the debut novel of French author Laurent Binet, published in 2010 by 
Grasset & Fasquelle. The book recounts Operation Anthropoid, the assassination of Nazi 
leader Reinhard Heydrich in Prague during World War II. The novel was awarded the 2010 
Prix Goncourt du Premier Roman.''')
                                print("\n" * 2)
                                print('''III. I, Claudius: I, Claudius is a historical novel by English writer Robert Graves, 
published in 1934. Written in the form of an autobiography of the Roman Emperor Claudius, 
it tells the history of the Julio-Claudian dynasty and the early years of the Roman 
Empire, from Julius Caesar's assassination in 44 BC to Caligula's assassination in AD 41. 
Though the narrative is largely fictionalized, most of the events depicted are drawn from 
historical accounts of the same time period by the Roman historians Suetonius and Tacitus.''')
                                print("*" * 60)
                            if ans1 == "f":
                                print('''I. Frankenstein: Frankenstein; or, The Modern Prometheus is an 1818 novel written by 
English author Mary Shelley. Frankenstein tells the story of Victor Frankenstein, 
a young scientist who creates a sapient creature in an unorthodox scientific experiment. 
Shelley started writing the story when she was 18, and the first edition was published 
anonymously in London on 1 January 1818, when she was 20. Her name first appeared in the 
second edition, which was published in Paris in 1821. Shelley travelled through Europe in 
1815 along the river Rhine in Germany, stopping in Gernsheim, 17 kilometres (11 mi) away 
from Frankenstein Castle, where two centuries before, an alchemist engaged in experiments. 
She then journeyed to the region of Geneva, Switzerland, where much of the story takes 
place. Galvanism and occult ideas were topics of conversation among her companions, 
particularly her lover and future husband Percy B. Shelley. In 1816, Mary, Percy and Lord 
Byron had a competition to see who could write the best horror story. After thinking 
for days, Shelley was inspired to write Frankenstein after imagining a scientist who 
created life and was horrified by what he had made''')
                                print("\n" * 2)
                                print('''II. Dracula: Dracula is a novel by Bram Stoker, published in 1897. As an epistolary novel, 
the narrative is related through letters, diary entries, and newspaper articles. It has no 
single protagonist, but opens with solicitor Jonathan Harker taking a business trip to 
stay at the castle of a Transylvanian noble, Count Dracula. Harker escapes the castle 
after discovering that Dracula is a vampire, and the Count moves to England and plagues 
the seaside town of Whitby. A small group, led by Abraham Van Helsing, hunt Dracula and, 
in the end, kill him. Dracula was mostly written in the 1890s. Stoker produced over a 
hundred pages of notes for the novel, drawing extensively from Transylvanian folklore and 
history. Some scholars have suggested that the character of Dracula was inspired by 
historical figures like the Wallachian prince Vlad the Impaler or the countess Elizabeth 
Báthory, but there is widespread disagreement. Stoker's notes mention neither figure. He 
found the name Dracula in Whitby's public library while holidaying there, picking it 
because he thought it meant devil in Romanian.''')
                                print("\n" * 2)
                                print('''III. The Shining: The Shining is a 1977 horror novel by American author Stephen King. It 
is King's third published novel and first hardback bestseller; its success firmly 
established King as a preeminent author in the horror genre. The setting and characters 
are influenced by King's personal experiences, including both his visit to The Stanley 
Hotel in 1974 and his struggle with alcoholism. The novel was adapted into a 1980 film of 
the same name. The book was followed by a sequel, Doctor Sleep, published in 2013, 
which was adapted into a film of the same name. The Shining centers on the life of Jack 
Torrance, a struggling writer and recovering alcoholic who accepts a position as the 
off-season caretaker of the historic Overlook Hotel in the Colorado Rockies. His family 
accompanies him on this job, including his young son Danny Torrance, who possesses 'the 
shining', an array of psychic abilities that allow Danny to see the hotel's horrific past. 
Soon, after a winter storm leaves them snowbound, the supernatural forces inhabiting the 
hotel influence Jack's sanity, leaving his wife and son in incredible danger.''')
                                print("*" * 60)
                            if ans1 == "g":
                                print('''I. In Cold Blood: In Cold Blood is a non-fiction novel by American author Truman Capote, 
first published in 1966. It details the 1959 murders of four members of the Herbert 
Clutter family in the small farming community of Holcomb, Kansas. Capote learned of the 
quadruple murder before the killers were captured, and he traveled to Kansas to write 
about the crime. He was accompanied by his childhood friend and fellow author Harper Lee, 
and they interviewed residents and investigators assigned to the case and took thousands 
of pages of notes. Killers Richard Hickock and Perry Smith were arrested six weeks after
the murders and later executed by the state of Kansas. Capote ultimately spent six years 
working on the book. In Cold Blood was an instant success and is the second-best-selling
true crime book in history, behind Vincent Bugliosi's Helter Skelter (1974) about the 
Charles Manson murders.''')
                                print("\n" * 2)
                                print('''II. Murder on the Orient Express: The elegant train of the 1960s, the Orient Express, 
is stopped by heavy snowfall. A murder is discovered, and Poirot's trip home to London 
from the Middle East is interrupted to solve the case. The opening chapters of the novel 
take place in Istanbul. The rest of the novel takes place in Yugoslavia, with the train 
trapped between Vinkovci and Brod.''')
                                print("\n" * 2)
                                print('''III. Silence of the lambs: The Silence of the Lambs is a psychological horror novel by 
Thomas Harris. First published in 1988, it is the sequel to Harris's 1981 novel Red 
Dragon. Both novels feature the cannibalistic serial killer Dr. Hannibal Lecter, 
this time pitted against FBI Special Agent Clarice Starling. Its film adaptation directed 
by Jonathan Demme was released in 1991 to widespread critical acclaim and box office 
success. It won the Academy Award for Best Picture.''')
                                print("*" * 60)
                                print("\n" * 2)
                            if ans1 == "":
                                print("You have not filled the field. Kindly enter a valid choice.")
                                continue

                            books1 = []
                            n1 = int(input("Enter the number of books:"))
                            if n1 > 3:
                                print("Enter a valid value")
                            else:
                                for a in range(n1):
                                    elem1 = input(
                                        "Enter the book you have chosen, in the way they are mentioned above:")

                                    books1.append(elem1)
                                print("The books you have chosen are:", books1)
                                books += books1

                                ans = input("WANT to enter books from other genres. Type yes or no:")
                        else:
                            print("The books you have developed a liking upon are:", books)
                            ans2 = input("Are these your final books. Type yes or no:")
                            if ans2 == "yes":
                                print("Let's cut you on some costs.")
                            if ans2 == "no":
                                ch1 = input("DO you want to restart? Type yes or no")
                                if ch1 == "yes":
                                    print("Last chance, alright? Just kidding! Shop all you want!")
                                    print("\n" * 4)
                                    continue
                                else:

                                    print("Let's help you delete some books!")

                                    ans3 = "yes"
                                    while ans3 == "yes":

                                        item0 = int(input("Enter the position of the book to be removed:"))
                                        item = item0 - 1
                                        books.pop(item)
                                        print("The new list of books is:", books)
                                        ans3 = input("DO you want to delete some more books?. Type yes or no")




                                    else:
                                        print("The new order of books is:", books)
                                        print("*" * 60)
                                        print("\n" * 4)
                                        print("*" * 60)

                        # Cost analysis

                        print(
                            "The total cost of your past time and hour of solitude will be appearing as fast as one of Harvey "
                            "Spector's cocky, yet iconic quotes")

                        print("*" * 60)
                        print("\n" * 2)

                        tax = (len(books) * 299) / 11

                        perks = len(books) * 299 / 23

                        cost = int(len(books) * 299 + tax + perks)

                        print("*" * 60)

                        print("\n" * 2)
                        print("The cost will be: Rs", cost)
                        add = input("Kindly enter the address:")
                        try:
                            con = mysql.connector.connect(host='localhost', database='mystudentdb', user='root',
                                                          password='Yogesh@34125')
                            if con.is_connected():
                                db_info = con.get_server_info()
                                print("Connected to MYSQL server", db_info)
                                cursor = con.cursor()
                                for i in books:
                                    query2 = "UPDATE books1 SET Qty=Qty-1 WHERE Books='{}'".format(i)

                                    cursor.execute(query2)
                                    con.commit()
                                print("Columns Updated")
                                query3 = "select * from books1"
                                cursor.execute(query3)


                        except mysql.connector.Error as e:
                            print("Error", format(e))

                        print("Your unique book code for the order will be:", random.randrange(0, 12000))
                        code = random.randrange(0, 340)
                        print("You can track and inquire about the order with the help of the store code:", code)

                        email = input(
                            "Enter your email for updates for your order as well as various offers and discounts:")
                        domain = "@gmail.com"
                        if domain in email:
                            print("The email entered is:", email)
                        elif domain not in email:
                            print("The email entered is:", email + domain)

                        print("*" * 60)
                        print("\n" * 2)
                        dob = input("Let the records show the date of birth of our benefactor(dd/mm//yy):")
                        while True:
                            try:
                                cont = int(input("Enter the mobile number:"))
                            except ValueError:
                                print("Please enter a number.")
                                continue
                            if len(str(cont)) > int(10) or len(str(cont)) < int(10):
                                print("Please enter a valid number.")
                            else:
                                break
                        if len(str(cont)) == int(10):
                            print("The number entered is valid.")

                        print(
                            "----------------------------------------RECEIPT---------------------------------------------")
                        print("\n" * 3)

                        print('----------------------Welcome To Bookut----------------------')
                        print('-----------BOOKUT PVT. LIM., BOSTON, MASSACHUSETTS-----------')

                        print('----------------------Order Code:', random.randrange(0, 360), "-----------------------")
                        print('-----------------------Mobile: 123XXX -----------------------')
                        x = PrettyTable()
                        x.field_names = ['Books', 'Price (excluding taxes and deductions)', 'Taxes']
                        for z in range(0, len(books)):
                            taxesz = int(tax) / 2
                            x.add_row([books[z], 'Rs 299', taxesz])

                        print(x)

                        print("\n" * 1)
                        print("The total cost is: Rs ", cost)
                        print("\n" * 1)

                        print(
                            "Thanks for ordering from us and making ours, as well as a child's day,in Africa battling hunger "
                            "as "
                            "we donate 10 percent of what we earn for helping the poor and needy.")
                        print("*" * 60)
                        print("\n" * 5)

                        print("*" * 60)
                        print(" Check out the POPULARITY BY BOOKS:")
                        height = [23, 12, 15, 18, 45, 32, 32, 21, 32, 22, 12, 29, 35, 22, 10, 35, 43, 19, 32, 43, 41]
                        bars = (
                            'Jurassic Park', 'Dune', 'Nineteen Eighty-Four', 'The Name of the Wind', 'The Way of Kings',
                            'The Fifth season',
                            'Pride and Prejudice', 'Red, White and Royal Blue', 'Jane Eyre', 'Vicious', 'Renegade',
                            'Vengeful',
                            'Wolf Hall',
                            'HHhH', 'I, Claudius', 'Frankenstein', 'Dracula', 'The Shining', 'In Cold Blood',
                            'Murder on the Orient Express', 'Silence of the lambs')

                        x_pos = np.arange(len(bars))

                        # Create bars
                        plt.bar(x_pos, height, color=(0.5, 0.1, 0.5, 0.6))
                        plt.title('POPULARITY BY BOOKS')
                        plt.xlabel('Books')
                        plt.ylabel('Popularity')

                        # Create names on the x-axis
                        plt.xticks(x_pos, bars, rotation=90)
                        plt.subplots_adjust(bottom=0.4, top=0.99)

                        # Show graphic
                        plt.show()

                        break
                    else:
                        print("Thanks for visiting our site and giving us a chance to prove us.")
                        print("*" * 60)
                        print("\n" * 5)
                        print("*" * 60)


            else:
                print("Your request has been denied. Please try again later.")
                print("*" * 60)
                print("\n" * 5)
                print("*" * 60)
                break
        else:
            print("Enter a valid answer.")
            continue








else:
    print("Enter an appropriate role while logging in")
