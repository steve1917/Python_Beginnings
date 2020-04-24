#This program generates the Abbreiviation of the Month, given its number

def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n= eval(input("Enter a Month Number (1-12) : "))

    #compute the appropiate slice from months
    pos = (n-1) * 3

    monthAbbrev = months[pos:pos+3]

    #print the result
    print("The Month abbreviation is", monthAbbrev + ".")

main()



    

