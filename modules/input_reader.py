import sys
from modules import health
from modules import colors

def printDict(title: str, dict: dict, initial_spacing: int):
    # initial spacing in tabs (4 spaces)

    # title spacing
    tab = "    "
    currentTitleTab = "" ; currentTitleTab += tab * initial_spacing
    #

    # title bar
    titleBar = "" ; titleBar += "-" * len(title)
    #
    print(title)
    print(titleBar)
    
    for dictKey,dictValue in dict.items():

        dictCompiled = f"{dictKey} -> {dictValue}"

        # create bars seperating items in the terminal
        dictBar = "" ; dictBar += "-" * len(dictCompiled)
        # create spacing for items in the terminal
        dictSpacing = "" ; dictSpacing += tab * (initial_spacing + 1)
        #
        
        print(f"{dictSpacing}{dictCompiled}")
        print(f"{dictSpacing}{dictBar}")
        

        

class reader:
    #simple input reader
    def decompileText(text: str): # use to split text up by spaces
        text = text.lower()
        return text.split()
    # recombine decombiled text(list) either entirely
    # or starting at a certain index as well as returning the remaining list
    def compileList(list: list, index: int | None):
        if index >= 0: return list[0:index]," ".join(list[index:])
        elif index == None: return "".join(list)
    
    #do command based on input
    def executeInput(request: dict):
        if len(request) == 0: return

        # the first command identifier (e.g. walk ... , go ... , check ... , etc)
        rootCommand = request[0]

        # switch statement to cycle through different commands
        match rootCommand:
            case "quit":
                response = input(f"Are you sure? {colors.bcolors.WARNING}Y/N{colors.bcolors.ENDC} : ").lower()
                if response == "y":
                    sys.exit()
                elif response == "n":
                    return
                else:
                    reader.executeInput(["quit"])
            case "check":
                limbs = health.limbs
                organs = health.organs

                r,requested = reader.compileList(request,1)
                requested = requested.lower()
                requested_T = requested.title()

                # check limbs and organs
                if requested == "all limbs":
                    for limbName,limbDict in limbs.items():
                        printDict(limbName,limbDict,0)
                    return
                if requested == "all organs":
                    for organName,organDict in organs.items():
                        printDict(organName,organDict,0)
                
                if requested_T in limbs:
                    limb = limbs[requested_T]
                    printDict(requested_T,limb,0)

                if requested_T in organs:
                    organ = organs[requested_T]
                    printDict(requested_T,organ,0)
                #
            case _: return

