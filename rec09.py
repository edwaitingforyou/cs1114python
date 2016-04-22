#!C:\python27\Python.exe
'''
rec09-partI
programmer: Beihong Chen
programemr ID: 0493191

This program gets order from a family and then eliminate
unnesessary items and print it
'''
DISLIKE_ITEM_ONE = "bread"
DISLIKE_ITEM_TWO = "cake"
DISLIKE_ITEM_THREE = "orange"
DISLIKE_ITEM_FOUR = "pineapple"
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

def changeList(shopList):
    '''
    This function deletes the  those foods
    that the designated shopper doesn't like.
    '''
    for DISLIKE_ITEM_ONE in shopList:
        shopList.remove(DISLIKE_ITEM_ONE)
    for DISLIKE_ITEM_TWO in shopList:
        shopList.remove(DISLIKE_ITEM_TWO)
    for DISLIKE_ITEM_THREE in shopList:
        shopList.remove(DISLIKE_ITEM_THREE)
    for DISLIKE_ITEM_FOUR in shopList:
        shopList.remove(DISLIKE_ITEM_FOUR)
    return shopList

def printList(shopList):
    '''
    This function prints the shoplist
    '''
                print shopList


def main():
    shopList = getShopList()
    newShopList = changeList(shopList)
    printList(newShopList)

main()
