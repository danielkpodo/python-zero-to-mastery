# lets say someone gives you a text file
# read thru translate the text file into japanese
# google python offline translate

# use translate-python package

from translate import Translator
translator = Translator(to_lang="fr")


file_path = "./sample_file.txt"
translated_path = "./french.txt"

try:
    with open(file_path, mode='r') as file_object:
        current_file = file_object.read()
        translation = translator.translate(current_file)
        with open(translated_path, mode='w') as file_object:
            file_object.write(translation)
except FileNotFoundError as err:
    print("File does not exist")
