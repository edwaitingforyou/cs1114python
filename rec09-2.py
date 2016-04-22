
def controlState():
    '''
    This function get the command from user.
    '''
    inputV = int(raw_input("Enter the choice you want.")
    return inputV

def addDislike():
    '''
    This function gets the unallowed items.
    '''
    dislike = raw_input("Enter the item you dislike:")
    return dislike

def getShopList():
    '''
    This function gets the order from user.
    '''
    shopList = []
    item = ""
    while item != "SHOP" :
        item = raw_input("What do you want:")
        shopList.append(item)
    shopList.remove("SHOP")        
    return shopList

def printList(shopList):
    '''
    This function prints the shoplist
    '''
                print shopList

def changeList(shopList,dislike):
    '''
    This function eliminate the dislike from shopList
    '''
    for dislike in shopList:
                       shopList.remove(dislike)
    return shopList

def main():
    controlState = controlState()
    while controlState != 3:
                 if controlState == 1:
                 shopList = getShopList()
                 controlState = controlState()
                 elif controlState == 2:
                 dislike = addDislike
                 controlState = controlState()
    newList = changeList(shopList,disLike)
    printList(newList)


main()
                    
