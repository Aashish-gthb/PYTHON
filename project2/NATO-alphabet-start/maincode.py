import pandas

nato_file = pandas.read_csv("C:/Users/ashuj/Python/projects/project2/NATO-alphabet-start/natosymbol.csv")

nato_dict = {data.letter:data.code for (index,data) in nato_file.iterrows() }

# print(nato_dict)
def generate_phonetic():

    
    user_input = input("Enter a word: ").upper()
    try:
        new_list = [nato_dict[word] for word in user_input ]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)

generate_phonetic()
