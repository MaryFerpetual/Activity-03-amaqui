import maria_stat as ma
import me_ev as mi

counter = 1
while counter == 1:
    print ("\n[1] Stat Calculator")
    print ("[2] EV Calculator")
    num0 = int(input("Choose number: "))

    BAS = int (input("\nBase STAT:"))
    LVL = int (input("LEVEL:"))
    EV = int (input("EVHP:"))
    IV = int (input("IVHP:"))
    STAT = int(input("Desired increase in stat:"))

    if num0 == 1:
        print ("\nHp = ", ma.mar.hpcal(BAS,IV,EV,LVL))
        print ("attack = ", ma.mar.otherstat(BAS,IV,EV,LVL))
        print ("def = ", ma.mar.otherstat(BAS,IV,EV,LVL))
        print ("SP attack = ", ma.mar.otherstat(BAS,IV,EV,LVL))
        print ("SP def = ", ma.mar.otherstat(BAS,IV,EV,LVL))
        print ("SPEED = ", ma.mar.otherstat(BAS,IV,EV,LVL))
        print ("\nThe needed Evs to increase stat is ", mi.mee.evneed(STAT,BAS,IV,EV,LVL))
    
    elif num0 == 2:
        print ("\n[1] Single stat")
        print ("[2] All stat")
        num1 = int (input("Choose a number:"))

        if num1 == 1:
            print ("\n[1] Attack")
            print ("[2] def")
            print ("[3] SP.attack")
            print ("[4] SP.def")
            print ("[5] Speed")
            print ("[6] HP")
            num20= int (input ("Choose Stat:"))

            if num20 == 1 or 2 or 3 or 4 or 5:
                print ("\nThe Stat is", ma.mar.otherstat(BAS,IV,EV,LVL))
            elif num20 == 6:
                print ("\nHp = ", ma.mar.hpcal(BAS,IV,EV,LVL))

        elif num1 == 2:
            print ("\nHp =", ma.mar.hpcal(BAS,IV,EV,LVL))
            print ("attack =", ma.mar.otherstat(BAS,IV,EV,LVL))
            print ("def =", ma.mar.otherstat(BAS,IV,EV,LVL))
            print ("SP. attack =", ma.mar.otherstat(BAS,IV,EV,LVL))
            print ("SP. def =", ma.mar.otherstat(BAS,IV,EV,LVL))
            print ("SPEED=", ma.mar.otherstat(BAS,IV,EV,LVL))
    
    print ("\n[1] Perform another calculation")
    print ("[2] End the program")
    num3 = int (input("choose a number:"))
    if num3 ==2:
        break
    elif num3 == 1:
        continue