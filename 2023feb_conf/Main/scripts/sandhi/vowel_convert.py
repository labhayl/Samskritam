def get_vowels_diacritics(word):
  
    vowels = ['अ','आ', 'इ','ई', 'उ','ऊ', 'ऋ','ॠ', 'ऌ','ॡ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः']    
    diacritics = ['','ा','ि','ी', 'ु', 'ू', 'ृ','ॄ',' ॢ',' ॣ','े', 'ै','ो', 'ौ',' ं',' ः']
    
    
    consonants = ['क', 'ख', 'ग', 'घ', 'ङ','च', 'छ', 'ज', 'झ', 'ञ','ट', 'ठ', 'ड', 'ढ', 'ण','त', 'थ', 'द', 'ध', 'न','प', 'फ', 'ब', 'भ', 'म','य', 'र', 'ल', 'व','श', 'ष', 'स', 'ह']
    first_vowel = None
    last_vowel = None
    for i in range(len(word)):
        #print(word[i])
        # कवि or हरी or मही 
        
        if word[i] in consonants and word[i+1] in consonants: 
          first_vowel = "अ"
        if word[i] in vowels or word[i] in diacritics:
            if not first_vowel:
                first_vowel = word[i]
            last_vowel = word[i]
        else:
          last_vowel = "अ"
    return first_vowel, last_vowel
def vowel_conv(word):
    vowels = ['अ','आ', 'इ','ई', 'उ','ऊ', 'ऋ','ॠ', 'ऌ','ॡ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः']    
    diacritics = ['','ा','ि','ी', 'ु', 'ू', 'ृ','ॄ',' ॢ',' ॣ','े', 'ै','ो', 'ौ',' ं',' ः']

    first_vowel,last_vowel= get_vowels_diacritics(word.ljust(8,' ')) # reducing whitespaces results in string out of bounds error with complex words , ex - रुद्र
    
    #first_vowel,last_vowel=' '+first_vowel,' '+last_vowel
    if first_vowel in diacritics:
        first_vowel=vowels[diacritics.index(first_vowel)]
    if last_vowel in diacritics:
        last_vowel=vowels[diacritics.index(last_vowel)]
    return first_vowel,last_vowel
