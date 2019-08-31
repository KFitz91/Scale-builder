def user_in():
    global x
    x = input("Enter the root note: ")
    return(x)

checkmark = False
notes = ['a','a#','bb','b','c','c#','db','d','d#','eb','e','f','f#','gb','g','g#','ab']

def check(x):

    def check1(x):
        if x[0] in notes:
            global checkmark
            checkmark = True
            build(x)
        else:
            print("Invalid input, try again")
            user_in()

    def check2(x):
        if x[1]=='#':
            check1(x)
        elif x[1]=='b':
            check1(x)
        elif x[1]=='m':
            check1(x)
        else:
            print("Invalid input, try again")
            user_in()

    def check3(x):
        if x[2]=='m':
            check2(x)
        else:
            print("Invalid input, try again")
            user_in()

    if len(x)==1:
        check1(x)
    elif len(x)==2:
        check2(x)
    elif len(x)==3:
        check3(x)
    else:
        print("Invalid input, try again")
        user_in()



def build(x):
    num_to_note = {1:"a",2:"a#",3:"b",4:"c",5:"c#",6:"d",7:"d#",8:"e",9:"f",10:"f#",11:"g",12:"g#"}
    note_to_num = {"a":1,"a#":2,"b":3,"c":4,"c#":5,"d":6,"d#":7,"e":8,"f":9,"f#":10,"g":11,"g#":12}
    num_to_note_b = {1:"a",2:"bb",3:"b",4:"c",5:"db",6:"d",7:"eb",8:"e",9:"f",10:"gb",11:"g",12:"ab"}
    note_to_num_b = {"a":1,"bb":2,"b":3,"c":4,"db":5,"d":6,"eb":7,"e":8,"f":9,"gb":10,"g":11,"ab":12}


    
    if len(x)==1:
        root = note_to_num[x[0]]
    elif len(x)==2:
        if x[-1]=='#':
            root = note_to_num[x]
        elif x[-1]=='b':
            root = note_to_num_b[x]
        elif x[-1]=='m':
            root = note_to_num[x[0]]
    elif len(x)==3:
        if x[1]=='#':
            root = note_to_num[x[:2]]
        elif x[1]=='b':
            root = note_to_num_b[x[:2]]

    maj_template = [root,root+2,root+4,root+5,root+7,root+9,root+11,root]
    min_template = [root,root+2,root+3,root+5,root+7,root+8,root+10,root]
    nums = []

    if len(x)==1:
        for e in maj_template:
            if e>12:
                nums.append(e-12)
            else:
                nums.append(e)
    elif len(x)==2:
        if x[1]=='m':
            for e in min_template:
                if e>12:
                    nums.append(e-12)
                else:
                    nums.append(e)
        else:
            for e in maj_template:
                if e>12:
                    nums.append(e-12)
                else:
                    nums.append(e)
    elif len(x)==3:
        for e in min_template:
            if e>12:
                nums.append(e-12)
            else:
                nums.append(e)

    scale = []

    if len(x)==1:
        for e in nums:
            scale.append(num_to_note[e])
    if len(x)==2:
        if x[1]=='#' or x[1]=='m':
            for e in nums:
                scale.append(num_to_note[e])
        elif x[1]=='b':
            for e in nums:
                scale.append(num_to_note_b[e])
    if len(x)==3:
        if x[1]=='#':
            for e in nums:
                scale.append(num_to_note[e])
        elif x[1]=='b':
            for e in nums:
                scale.append(num_to_note_b[e])

    print("Notes in",x,":",scale)
                


user_in()

while checkmark == False:
    check(x)

