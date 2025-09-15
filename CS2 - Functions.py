#Reverse and Display
def name():
    name = input('What is your name?')
    reversed_name = reverse(name)
    print(f'Reversed Name: {reversed_name}')

#Make Initials
def initials():
    initial = input('What is your name?')
    
#Vowel Counting
def vowel_count(name):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for i in name:
        if i in vowels:
            vowel_count += 1
            print(vowel_count)

#Main
def main():
