#This Program generates a Username based on their first and last name

#Program
#   Get first and last name
#   concatenate name to generate a username
#   Output their generated username 
#End

def main():
    print("This program generates a username.\n")

    #get Users first and last name
    first = input("Enter your first name(all lowercase): ")
    last = input("Enter your last name(all lowercase): ")
    
    #concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]

    #output the username
    print("Your conputer generated username is: ", uname)

main()