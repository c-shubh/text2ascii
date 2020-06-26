import fonts # Contains all the fonts.

# Prints the menu to select font.
print('Fonts:')
for index, font_name in enumerate(fonts.font_list, 1):
    print(f"{index}. {font_name[0]}")
selected_num = int(input('Select a font: '))
selected_font = fonts.font_list[selected_num-1][1]
not_allowed = fonts.font_list[selected_num-1][2]

text = input('Enter text: ')

# Converts the input text to upper case if the font doesn't support lowercase characters.
for char in text:
    if char.islower():
        try: 
            selected_font[char]
        except KeyError:
            text = text.upper()

# Prints the text.
for i in range(len(selected_font['A'])):
    for letter in text:
            if letter in not_allowed:
                continue
            print(selected_font[letter][i], end='')
    print()


# Just to check whether a given font has all the characters ordered correctly.
# for char, l in selected_font.items():
    # print(*l, sep='\n')
