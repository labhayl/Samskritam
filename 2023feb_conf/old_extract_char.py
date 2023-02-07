def separate_characters(word):
  vowels = ['अ', 'आ', 'ऊ', 'ऋ', 'उ', 'इ', 'ऐ', 'ओ', 'ई', 'ए', 'औ']
  diacritics = ['ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो', 'ौ', 'ा', 'ि', 'ु', 'ू']
  characters = []
  for char in word:
      characters.append(char)
  return characters

def get_last_vowel_diacritic(word):
    vowels = ['अ', 'आ', 'ऊ', 'ऋ', 'उ', 'इ', 'ऐ', 'ओ', 'ई', 'ए', 'औ']
    diacritics = ['ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो', 'ौ', 'ा', 'ि', 'ु', 'ू']
    iast_vowel_diacritics = {'ी': 'ī', 'े': 'e', 'ॄ': 'ṝ', 'ृ': 'ṛ',
                            'ै': 'ai', 'ॢ': 'ḷ', 'ो': 'o', 'ौ': 'au',
                            'ा': 'ā', 'ि': 'i', 'ु': 'u', 'ू': 'ū'}
    char = str(word[-1])                        
    if char in vowels or char in diacritics:
            return char
    return "अ"
  
  
word = "पुष्प"
word_split = separate_characters(word)
get_last_vowel_diacritic(word_split)
