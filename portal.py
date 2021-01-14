import sys
import os.path
import json

if sys.argv[1] == 'AddUser':
    #Check if there is 4 arguments
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        exit()
    #Check if username is not empty string
    if sys.argv[2] == "":
        print("Error: Username is missing")
        exit()

    username = sys.argv[2]
    password = sys.argv[3]
    #Check if user exists

    #Check if file exists and see if username doesn't already exist
    if os.path.exists("users.json"):
        users_file = open("users.json", 'r')
        users = json.load(users_file)
        if username in users:
            print("Error: User already exists")
            exit()
        else:
            users[username] = {"username": username, "password": password, "domains": []}
            users_file = open("users.json", 'w')
            json.dump(users, users_file, indent=4)
    else:
        users_file = open("users.json", 'w')
        users = {username: {"username": username, "password": password, "domains": []}}
        json.dump(users, users_file, indent=4)

    print("Success")


#For authenticating a user that already exists in the user.json file
elif sys.argv[1] == 'Authenticate':
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        exit()

    username = sys.argv[2]
    password = sys.argv[3]

    #Check if users file exists and try to find user and verify the credentials
    if os.path.exists("users.json"):
        users_file = open("users.json", 'r')
        users = json.load(users_file)
        if username in users:
            if users[username]["password"] != password:
                print("Error: Invalid password")
                exit()
            else:
                print("Success")
        else:
            print("Error: User does not exist")
            exit()
    else:
        print("Error: User does not exist")


elif sys.argv[1] == 'SetDomain':
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        exit()
    elif sys.argv[3] == "":
        print("Error: Missing domain name")
        exit()

    username = sys.argv[2]
    domainName = sys.argv[3]

    #Check if user exists
    if os.path.exists("users.json"):
        users_file = open("users.json", 'r')
        users = json.load(users_file)
        if username in users:
            #if the user exists => check if domain exists
            if os.path.exists("domains.json"):
                #I want to go through the list and add user to the domain and add in user list that its part of the domain
                domains_file = open("domains.json", 'r')
                domains = json.load(domains_file)
                #check if domain exists in the file
                if domainName not in domains:
                    #adding domain name to the table
                    domains[domainName] = {"users": [username]}
                    #Add domain to user's domain list
                    users[username]["domains"].append(domainName)
                    users_file = open("users.json", 'w')
                    json.dump(users, users_file, indent=4)

                    domains_file = open("domains.json", 'w')
                    json.dump(domains, domains_file, indent=4)
                #If the domain exists, append to domain list users
                else:
                    if username not in domains[domainName]["users"]:
                        #add domain to users
                        if domainName not in users[username]["domains"]:
                            users[username]["domains"].append(domainName)
                            users_file = open("users.json", 'w')
                            json.dump(users, users_file, indent=4)

                            domains[domainName]["users"].append(username)
                            domains_file = open("domains.json", 'w')
                            json.dump(domains, domains_file, indent=4)
                        else:
                            print("Error: User already exists in domain")
                            exit()
                    else:
                        print("Error: User already exists in domain")
                        exit()

            else:
                #if the file doesnt exist
                domains = {domainName: {"users": [username]}}
                #add to user domain list
                users[username]["domains"].append(domainName)
                users_file = open("users.json", 'w')
                json.dump(users, users_file, indent=4)

                domains_file = open("domains.json", 'w')
                json.dump(domains, domains_file, indent=4)
        else:
            print("Error: User does not exist")
            exit()
    else:
        #file doesnt exist - No users
        print("Error: User does not exist")

    print("Success")


elif sys.argv[1] == "DomainInfo":
    if len(sys.argv) != 3:
        print("Error: Invalid arguments")
        exit()
    elif sys.argv[2] == "":
        print("Error: Missing domain name")
        exit()
    domainName = sys.argv[2]
    #Check if domain exists in domain file
    if os.path.exists("domains.json"):
        domains_file = open("domains.json", 'r')
        domains = json.load(domains_file)
        if domainName in domains:
            for user in domains[domainName]["users"]:
                print(user)
        else:
            print("Error: Domain does not exist")
            exit()
    else:
        print("Error: Domain does not exist")
        exit()


elif sys.argv[1] == "SetType":
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        exit()

    obj = sys.argv[2]
    type = sys.argv[3]

    if obj == "":
        print("Error: Object can't be null")
        exit()
    if type == "":
        print("Error: Type name can't be null")
        exit()

    #Check if file exists
    if os.path.exists("types.json"):
        types_file = open("types.json", 'r')
        types = json.load(types_file)
        #If type already exists, add to objects list
        if type in types:
           #check if object exists already
            if obj in types[type]["objects"]:
                print("Error: Object already exists")
                exit()
            else:
                types[type]["objects"].append(obj)
                types_file = open("types.json", 'w')
                json.dump(types, types_file, indent=4)
        #Else, create the type and add the object
        else:
            types[type] = {"objects": [obj]}
            types_file = open("types.json", 'w')
            json.dump(types, types_file, indent=4)
     #if the file doesn't exist
    else:
        types = {type: {"objects" : [obj]}}
        types_file = open("types.json", 'w')
        json.dump(types, types_file, indent=4)

    print("Success")



elif sys.argv[1] == "TypeInfo":
    if len(sys.argv) != 3:
        print("Error: Invalid arguments")
        exit()

    type = sys.argv[2]

    if type == "":
        print("Error: Type argument is required")
        exit()

    if os.path.exists("types.json"):
        types_file = open("types.json", 'r')
        types = json.load(types_file)

        if type in types:
            for obj in types[type]["objects"]:
                print(obj)
    else:
        print("Error: Type doesn't exist")


#Defines access permission of a domain to an object
elif sys.argv[1] == "AddAccess":
    if len(sys.argv) != 5:
        print("Error: Invalid arguments")
        exit()

    op = sys.argv[2]
    domain = sys.argv[3]
    type = sys.argv[4]

    if op == "":
        print("Error: Missing operation")
        exit()
    elif domain == "":
        print("Error: Missing domain")
        exit()
    elif type == "":
        print("Error: Missing type")
        exit()

    #Check if domain exists, if not add it
    if os.path.exists("domains.json"):
        domains_file = open("domains.json", 'r')
        domains = json.load(domains_file)
        #if the domain isn't in the list, add it
        if domain not in domains:
            domains[domain] = {"users": []}
            domains_file = open("domains.json", 'w')
            json.dump(domains, domains_file, indent=4)
    #Else file doesn't exist, so we have to create the domain dictionary and write the file
    else:
        domains = {domain: {"users": []}}
        domains_file = open("domains.json", 'w')
        json.dump(domains, domains_file, indent=4)


    #Check if type exists, if not add it
    if os.path.exists("types.json"):
        types_file = open("types.json", 'r')
        types = json.load(types_file)
        #if type isn't in types.json, we will add
        if type not in types:
            types[type] = {"objects": []}
            types_file = open("types.json", 'w')
            json.dump(types, types_file, indent=4)

    else:
        types = {type: {"objects": []}}
        types_file = open("types.json", 'w')
        json.dump(types, types_file, indent=4)


    #Check if permissions file exists
    if os.path.exists("permissions.json"):
        perms_file = open("permissions.json", 'r')
        perms = json.load(perms_file)
        #if the operation doesn't exist, add to permissions
        if op not in perms:
            perms[op] = {"domains": {domain: [type]}}
            perms_file = open("permissions.json", 'w')
            json.dump(perms, perms_file, indent=4)
        #else, the operation exists and we add permission for the domain to access what type
        else:
            if domain in perms[op]["domains"]:
                if type not in perms[op]["domains"][domain]:
                    perms[op]["domains"][domain].append(type)
                    perms_file = open("permissions.json", 'w')
                    json.dump(perms, perms_file, indent=4)
            #else domain isn't in permissions, so add it
            else:
                perms[op]["domains"][domain] = [type]
                perms_file = open("permissions.json", 'w')
                json.dump(perms, perms_file, indent=4)
    #if file doesn't exist, create and add permissions
    else:
        perms = {op: {"domains": {domain: [type]}}}
        perms_file = open("permissions.json", 'w')
        json.dump(perms, perms_file, indent=4)

    print("Success")


#The CanAccess Argument
elif sys.argv[1] == "CanAccess":
    if len(sys.argv) != 5:
        print("Error: Invalid arguments")
        exit()

    op = sys.argv[2]
    user = sys.argv[3]
    obj = sys.argv[4]

    userDomains = []
    opDomains = []
    commonDomains = []
    commonTypes = []

    if op == "":
        print("Error: Operation not specified")
        exit()
    if user == "":
        print("Error: Username is required")
        exit()
    if obj == "":
        print("Error: Object is required")
        exit()

    #Check if user exists
    if os.path.exists("users.json"):
        users_file = open("users.json", 'r')
        users = json.load(users_file)
        if user not in users:
            print("Error: Username does not exist")
            exit()
        else:
            #Storing the domain values of user locally
            userDomains = users[user]["domains"]
    else:
        print("Error: Username does not exist")
        exit()

    #Check if permissions exists
    if os.path.exists("permissions.json"):
        perms_file = open("permissions.json", 'r')
        perms = json.load(perms_file)
        if op not in perms:
            print("Error: Operation isn't valid")
            exit()
        else:
            opDomains = perms[op]["domains"]
    else:
        print("Error: Operation isn't valid")
        exit()

    #find common domains between users and operations
    for userDomain in userDomains:
        if userDomain in opDomains:
            commonDomains.append(userDomain)

    #find the types for the commonDomain
    for dom in commonDomains:
        for typeVal in opDomains[dom]:
            if typeVal not in commonTypes:
                commonTypes.append(typeVal)


    if os.path.exists("types.json"):
        types_file = open("types.json", 'r')
        types = json.load(types_file)

        for typeVal in commonTypes:
            if obj in types[typeVal]["objects"]:
                print("Success")
                exit()
            else:
                print("Error: Access Denied")
    else:
         print("Error: Access Denied")
         exit()


