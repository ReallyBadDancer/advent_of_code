
def main():
    with open("puzzle_input_01.txt", mode='r') as ifile:
        snack_list = ifile.read().split('\n')

    print(snack_list)
    elf_inventories = []
    elf_cals = 0
    for snack in snack_list:
        if snack:
            elf_cals += int(snack)
        else:
            elf_inventories.append(elf_cals)
            elf_cals = 0


    top_three = 0
    for i in range(3):
        print(max(elf_inventories))
        top_three += max(elf_inventories)
        elf_inventories.remove(max(elf_inventories))

    print(top_three)


if __name__ == "__main__":
    main()
