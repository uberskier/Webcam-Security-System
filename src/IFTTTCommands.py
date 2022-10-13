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
                    self.peopleCommands[person] = {"test" : "test"}
                    newPerson = False
                #find new person command line
                elif command == "New Person":
                    newPerson = True
                #set commands for selected person
                else: 
                    key = command.split(':')
                    list = []
                    for l in range(1, len(key)):
                        list.append(key[l])
                    self.peopleCommands[person][key[0]] = list
            
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
                    #check that person in list has commands 
                    if key2 in self.peopleCommands.keys():
                        self.run(key2, numPeop)

        return

    #run commands for person
    def run(self, person, numPeop):
        #get persons conditions for commands 
        for key in self.peopleCommands[person]:
            #if statments based on conditions used
            if key == "Always":
                self.call((self.peopleCommands[person][key]))
            if key == "People":
                if numPeop > 1:
                    self.call((self.peopleCommands[person][key]))
        return


    #sending webhooks for each command
    def call(self, commands):
        #building webhook address for command
        for command in commands:
            url = 'https://maker.ifttt.com/trigger/{event_name}/with/key/{key}'
            url = url.format(event_name = command, key=self.api)
            #posting webhook address
            response = requests.post(url)

            #command line print saying it was processed
            info = "[INFO] Processed IFTTT command - "
            info += command
            print(info)
        return
