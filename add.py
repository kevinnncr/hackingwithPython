with open('collaborators.txt', 'r') as file:
    collaborators = [line.strip() for line in file.readlines()]

print("The collaborators are:")
for i, collaborator in enumerate(collaborators[:5], start=1):
    print(f"{i}. {collaborator}")


new_collaborator = input("Enter new collaborator: ")
if new_collaborator:
    if len(collaborators) < 15:
            collaborators.append(new_collaborator)
            with open('collaborators.txt', 'w') as file:
                    file.write(f"{collaborator}\n")
            print(f"{new_collaborator} has been successfully added.")
    else:
        print("Cannot add more collaborators. The limit is 15.")
