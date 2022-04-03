'''
how encryption works:
    it replaces each letter to it's number in alphabet and between each number it inserts "39"
'''

from os import system


system("title Encrypter")



def encrypter(text):

    low_letter_text = text.lower()

    encrypted_text = low_letter_text

    letters = " abcdefghijklmnoprstuwyzqxv"

    for index, value in enumerate(letters):
        encrypted_text = encrypted_text.replace(value, str(index) + str(39))

    return encrypted_text


def decrypter(text):

    encrypted_text = text

    letters = " abcdefghijklmnoprstuwyzqxv"

    str_tekst_s = str(encrypted_text)

    str_tekst_s = str_tekst_s.replace("39", " ")
    str_tekst_s = str_tekst_s.split()

    end_value = []

    for number in str_tekst_s:
        end_value.append(letters[int(number)])

    str_end_value = str(end_value)
    str_end_value = str_end_value.replace("[", "")
    str_end_value = str_end_value.replace("]", "")
    str_end_value = str_end_value.replace("'", "")
    str_end_value = str_end_value.replace(",", "")
    str_end_value = str_end_value.replace("  ", "_")
    str_end_value = str_end_value.replace(" ", "")
    str_end_value = str_end_value.replace("_", " ")


    return str_end_value



while True:
    try:
        user_choose = int(input("Choose what do you want to do?: \n 1.encrypt text \n 2.decrypt text \n 3.quit application(you can click ctrl + c too if you want to quit)?: "))
        if user_choose not in range(1, 4):
            print("Choose number from 1 to 3 please.")
            
    except ValueError:
        print("Choose number from 1 to 3 please.")
        continue


    if user_choose == 1:
        text = input("Enter a string?: ")
        print(encrypter(text))


    if user_choose == 2:
        is_that_integer = False

        while is_that_integer == False:
            try:
                integer = int(input("Enter an Integer?: "))
                print(decrypter(integer))
                is_that_integer = True
            except ValueError:
                print("Please enter an integer.")
            except IndexError:
                print("Invalid text to decrypt.")


    if user_choose == 3:
        quit()
