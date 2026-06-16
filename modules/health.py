limbs = {
    "Left Arm":{
        "Skin Health":100,
        "Infection Progression":0,
        "Infection Rate":0
    },
    "Right Arm":{
        "Skin-Health":100,
        "Infection Progression":0,
        "Infection Rate":0        
    },
    "Left Leg":{
        "Skin Health":100,
        "Infection Progression":0,
        "Infection Rate":0
    },
    "Right Leg":{
        "Skin Health":100,
        "Infection Progression":0,
        "Infection Rate":0        
    },
    "Torso":{
        "Skin Health":100,
        "Infection Progression":0,
        "Infection Rate":0
    },
    "Head":{
        "Skin Health":100,
        "Infection Progression":0,
        "Infection Rate":0
    }
}

organs = {
    "Brain": {
        "Health":100
    },
    "Heart": {
        "Heart Rate":120,
        "Blood Count":"5L"
    },
    "Lungs": {
        
    }
}

thirst = 100
thirstRate = 1
hunger = 100
hungerRate = 1


class checkHealth:
    def limb(name: str):
        if name not in limbs:
            print("err: health.py > health.limb(name)")
            print("                             ^^^^ ")
            print(f"{name} does not exist in dictionary health.limbs")
        else:
            for key,value in limbs[name].items():
                bar = ""
                i = 1
                while i < len(key):
                    bar += "-"
                print(key)
                print(bar)
                

    def checkAll():
        return
