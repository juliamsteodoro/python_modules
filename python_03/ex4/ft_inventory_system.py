import sys

def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, qty_str = arg.split(":")
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            qty = int(qty_str)
            inventory[item] = qty
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for item, qty in inventory.items():
        percent = (qty/total) * 100
        print(f"Item {item} represents {percent:.1f}%")

    most_item = max(inventory, key=inventory.get)  
    most_qty = inventory[most_item] 
    print(f"Item most abundant: {most_item} with quantity {most_qty}")
    least_item = min(inventory, key=inventory.get)  
    least_qty = inventory[least_item] 
    print(f"Item least abundant: {least_item} with quantity {least_qty}")
    inventory.update({"magic_item" : 1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()
