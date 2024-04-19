from RBTree import RBTree


def load_dictionary(file_name):
    dictionary_tree = RBTree()
    # reading each word from the file, then inserting it into the red black tree (aka the dictionary)
    with open(file_name, 'r') as file:
        for word in file:
            word = word.strip()
            dictionary_tree.insert(word)
    return dictionary_tree


class Dictionary:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tree = load_dictionary(file_name)

    def insert_word(self, word):
        self.tree.insert(word)
        print("Word inserted successfully!")
        self.tree.getTreeSize(self.tree.root)
        self.tree.getTreeHeight(self.tree.root)
        self.tree.getBlackHeight()
        self.update_file(word)

    def update_file(self, word):
        with open(self.file_name, 'a') as file:
            file.write('\n' + word)


def main():
    dictionary = Dictionary("dictionary.txt")

    while True:
        print("\nDictionary Operations:")
        print("1. Insert Word")
        print("2. Look-up a Word")
        print("3. Print Tree Height")
        print("4. Print Black Height")
        print("5. Print Tree Size")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_word = input("Enter word: ")
            dictionary.insert_word(input_word)

        elif choice == "2":
            search_word = input("Enter word: ")
            dictionary.tree.searchTree(search_word)

        elif choice == "3":
            print(dictionary.tree.getTreeHeight(dictionary.tree.root))

        elif choice == "4":
            print(dictionary.tree.getBlackHeight())

        elif choice == "5":
            print(dictionary.tree.getTreeSize(dictionary.tree.root))

        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
