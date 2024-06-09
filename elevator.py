arrayPressedFloors = []

def outputMessage(msg):
    print(msg)

def checkIfExists(theFloor):
    if theFloor in arrayPressedFloors:
        msgPressedAlready = "This floor is already pressed! Use the stairs!"
        outputMessage(msgPressedAlready)
    else:
        checkIfLOWAdjacentExists(theFloor)

def checkIfLOWAdjacentExists(theFloor):
    lowFloor = theFloor - 1
    if lowFloor in arrayPressedFloors:
        msgPressedAlready = "Floor " + str(theFloor) + " is just above Floor " + str(lowFloor) + ". Use the stairs from Floor " + str(lowFloor) + ", you lazy-ass!"
        outputMessage(msgPressedAlready)
    else:
        checkIfHIGHAdjacentExists(theFloor)

def checkIfHIGHAdjacentExists(theFloor):
    highFloor = theFloor + 1
    if highFloor in arrayPressedFloors:
        msgPressedAlready = "Floor " + str(theFloor) + " is just below Floor " + str(highFloor) + ". Use the stairs from Floor " + str(highFloor) + ", you lazy-ass!"
        outputMessage(msgPressedAlready)
    else:
        theMessage = "Floor " + str(theFloor) + " is free and is now pressed!"
        outputMessage(theMessage)
        storeToArray(theFloor)

def storeToArray(flr):
    arrayPressedFloors.append(flr)

while True:
    pressedFloor = int(input("Enter the desired floor (or type 'exit' to stop): "))
    if pressedFloor == "exit":
        break
    checkIfExists(pressedFloor)