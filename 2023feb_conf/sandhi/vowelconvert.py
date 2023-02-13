from vowel_extract import get_vowels_diacritics
def vowel_conv(word):
    vowels = ['अ','आ', 'इ','ई', 'उ','ऊ', 'ऋ','ॠ', 'ऌ','ॡ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः']    
    diacritics = ['','ा','ि','ी', 'ु', 'ू', 'ृ','ॄ',' ॢ',' ॣ','े', 'ै','ो', 'ौ',' ं',' ः']

    first_vowel,last_vowel=get_vowels_diacritics(word.ljust(8,' ')) # reducing whitespaces results in string out of bounds error with complex words , ex - रुद्र
    
    #first_vowel,last_vowel=' '+first_vowel,' '+last_vowel
    if first_vowel in diacritics:
        first_vowel=vowels[diacritics.index(first_vowel)]
    if last_vowel in diacritics:
        last_vowel=vowels[diacritics.index(last_vowel)]
    return first_vowel,last_vowel
