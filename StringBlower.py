def blowUp(input):
    output = "" # Define empty output string
    
    for count in range(len(input)): # Goes through all the characters in input

        charNow = str(input[count]) # finds what character the index is and puts it into "charNow"
        

        if charNow.isdigit(): # Checks if the character is a number
            #print ("dig found") # Notifies that the char is a digit

            try:
                charNext = str(input[count+1]) # for more convenience :D

                if not charNext.isdigit() and charNext != ' ': # If the next character is not a digit and not space
                    #print ("next not dig") # Notifies that the next character is not a digit

                    for counter in range(int(charNow)): # for int(charNow) times, adds the next character to the output
                        #if counter < 1: print (" *detected* ==> " + charNext + " <== replication process begins") # Notifies that the repeating process has started
                        
                        output = output + charNext # It will be added to the output
                        

                    
                elif charNext.isdigit() or charNext == ' ': 

                    output = output + charNow

            except IndexError:
                
                
                
                output = output + charNow # this makes sure that the last character is added to the output as well! :)
                
        else: # If the character is not a digit:

            output = output + charNow # It will be added to the output

    return output

userinput = input("Hello! what do you want to blow up today?! :) \n\n")
print(blowUp(userinput))