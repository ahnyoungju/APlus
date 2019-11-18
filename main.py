import re
import webbrowser
import Youngju

def display_menu():
    print("############################################")
    print("            Home Automation System")
    print("############################################")
    print(" 1. Newspaper")
    print(" 2. Weather")
    print(" 3. Shopping List")
    print(" 4. Dashboard")
    print(" 5. Exit")

def error_check(ans):
    x = re.match(r"[12345]", ans)

    if x != None :
        return True
    else:
        print("You entered invalid number. ", ans)
        return False

def get_choice() :
    display_menu()
    ans = input("Enter a number : ")

    while( error_check(ans) == False ) :
        display_menu()
        ans = input("Enter a number again: ")

    return int(ans)

# Main Procedure
login = True

while( login ) :
    answer = get_choice()
    if answer == 1:
        import Tahir
    elif answer == 2:
        if Youngju.Youngju() == False :
            print("At the moment, you can't get weather information.")
            exit(-1)
    elif answer == 3:
        import Kumi
    elif answer == 4:
        webbrowser.open_new("https://google.com")
    else:
        exit(0)
