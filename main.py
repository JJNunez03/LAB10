from bots import bot_clerk

if __name__ == "__main__":
    test_cases = [
        [],
        ['104'],
        ['106', '109', '102'],
        ['103', '108', '102', '110', '106'],
        ['106', '102', '108', '109', '103', '101', '110', '104', '107', '105']
    ]

    for items in test_cases:
        print(f"INPUT  : {items}")
        print(f"OUTPUT : {bot_clerk(items)}\n")
