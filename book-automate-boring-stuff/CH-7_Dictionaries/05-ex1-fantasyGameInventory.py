inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(items):
    print('Inventory:')
    total_number = 0
    for x, y in items.items():
        print(str(y) + ' ' + x)
        total_number += y
    print('Total number of items: ' + str(total_number))

def add_to_inventory(inv, dragon_loot):
    new_inventory = {}
    for k, v in inv.items():
        new_inventory[k] = v
    for k in dragon_loot:
        if k in new_inventory.keys():
            new_inventory[k] += 1
        elif k not in new_inventory.keys():
            new_inventory[k] = 1
    return new_inventory

display_inventory(add_to_inventory(inventory, dragon_loot))


