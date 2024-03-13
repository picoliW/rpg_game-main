from store.armor_store import armor
from store.sword_store import sword
from store.potion_store import potion



def store():
    print('-------------------Store--------------------')
    store_selection = input('Select the section:\n 1- Armor store \n 2- Sword store \n 3- Potion Store \n 4- Go back to menu\n')
    
    match store_selection:
        case '1':
            armor()
        case '2':
            sword()
        case '3':
            potion()
        case '4':
            from mainMenu import menu
            menu()
