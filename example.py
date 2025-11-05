from excusegen import get_excuse, get_excuses, add_excuse, list_excuses

def divider(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)

def main():
    # 1. get_excuse：
    divider("1. get_excuse")
    print("Default (general):", get_excuse())
    print("deadline:", get_excuse("deadline"))
    print("meeting:", get_excuse("meeting"))
    print("class:", get_excuse("class"))

    # 2. get_excuses
    divider("2. get_excuses")
    print("All from 'general':")
    for e in get_excuses("general"):
        print(" -", e)

    print("\nTwo random from 'deadline':")
    for e in get_excuses("deadline", count=2):
        print(" -", e)

    print("\nZero from 'meeting' (count=0):")
    print(get_excuses("meeting", count=0))

    print("\nFour random from 'class'")
    for e in get_excuses("class", count=4):
        print(" -", e)

    # 3. list_excuses
    divider("3. list_excuses")
    print("All from 'meeting':")
    for e in list_excuses("meeting"):
        print(" -", e)

    # 4. add_excuse
    divider("4. add_excuse")
    new_line = "My WiFi refused to cooperate."
    print("Adding to 'general':", new_line)
    added = add_excuse("general", new_line)
    print("Added ->", added)

    print("\nVerify new item exists in 'general':")
    print(new_line in list_excuses("general"))

    print("\nAdd the same line again:")
    again = add_excuse("general", new_line)

if __name__ == "__main__":
    main()