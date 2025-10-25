def find_vowels_and_count(user_words):
    small_letters = user_words.lower()
    the_vowels = ['a', 'e', 'i', 'o', 'u']
    final_scorecard = [
        [vowel, small_letters.count(vowel)]
        for vowel in the_vowels
    ]
    return final_scorecard

if __name__ == "__main__":
    user_input = input("Enter the word: ")
    frequency_list = find_vowels_and_count(user_input)
    print(frequency_list)
