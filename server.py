import sys
import dataChecks
import serversChecks


def main():
    dataChecks.initialisatie()
    if len(sys.argv) > 1:
        if sys.argv[1] == "-c" :
            serversChecks.execute()
            print("Check is gedaan!")
        elif sys.argv[1] == "-a":
            type_check = sys.argv[2]
            check_data = [sys.argv[3],sys.argv[4],sys.argv[5]]
            serversChecks.add(type_check,check_data)
        elif sys.argv[1] == "-d":
            serversChecks.detelte(sys.argv[2])
        elif sys.argv[1] == "-s":
            print(serversChecks.frame())
    else:
        antwoord = int(input("Kies :\n1.Check aan te maken.\n2.Check te verwijderen.\n3.Check op te lijsten.\n4.Check te checken.\n0.Om te stoppen."))
        while antwoord !=0:
            if antwoord == 1:
                type_check = input("Kies ping voor een ping-check :")
                host_name = input ("Naam van de host: ")
                teste = input("Hoeveel checks: ")
                perc = input("Percentage:")
                check_data = [host_name,teste,perc]
                serversChecks.add(type_check,check_data)
            elif antwoord == 2:
                print(serversChecks.frame())
                index = input("Geef index van de check die je wenst te verwijderen: ")
                serversChecks.detelte(index)
            elif antwoord == 3:
                print(serversChecks.frame())
            elif antwoord == 4:
                serversChecks.execute()
            antwoord = int(input("Kies :\n1.Check aan te maken.\n2.Check te verwijderen.\n3.Check op te lijsten.\n4.Check te checken.\n0.Om te stoppen."))
main()