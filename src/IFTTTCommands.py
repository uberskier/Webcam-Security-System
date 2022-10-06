import requests

class ifttt():
    def __init__(self, commands):
        #save API key
        self.api = commands[0]
        #create dict of dict for people and all commands
        self.peopleCommands = {}

        #check for new person line in file to signal start of a persons commands
        if commands[1] == "New Person":
            #set working to know if there are any commands
            self.working = True
            newPerson = True
            person = ""
            #loop through commands starting with first person
            for command in commands[2:]:
                #set name for dict of person
                if newPerson == True:
                    person = command
                    newPerson = False
                #find new person command line
                elif command == "New Person":
                    newPerson = True
                #set commands for selected person
                else: 
                    key = command.split(':')
                    self.peopleCommands[person] = {key[0] : key[1]}
            
            print("[INFO] Commands loaded for:")
            for x in self.peopleCommands:
                print(x)
            pass
        else:
            print("[INFO] No commands found")
            self.working = False

    #function that is called by main file to process commands based on conditions
    def commands(self, people):
        if self.working == True:

            numPeop = len(people)

            for key in people:
                for key2 in people[key]:
                    print(key2)
                    if key2 in self.peopleCommands == True:
                        print(2)
                        self.run(key2, numPeop)

        return

    def run(self, person, numPeop):
        for key in self.peopleCommands[person]:
            print(key)
            if key == "Always":
                self.call((self.peopleCommands[person][key]))
        return



    def call(self, command):
        #building webhook address for command
        address = 'https://maker.ifttt.com/trigger/'
        address += command
        address += '/with/key/'
        address += self.api
        #posting webhook address
        requests.post(address)

        #command line print saying it was processed
        info = "[INFO] Processed IFTTT command - "
        info += command
        print(info)
        return
