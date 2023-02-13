def devn(src):
    vowels = {
        'a': ['अ', ''],
        'ā': ['आ', 'ा'],
        'i': ['इ', 'ि'],
        'ī': ['ई', 'ी'],
        'u': ['उ', 'ु'],
        'ū': ['ऊ', 'ू'],
        'ṛ': ['ऋ', 'ृ'],
        'ṝ': ['ॠ', 'ॄ'],
        'ḷ': ['ऌ', 'ॢ'],
        'ḹ': ['ॡ', 'ॣ'],
        'e': ['ए', 'े'],
        'ai': ['ऐ', 'ै'],
        'o': ['ओ', 'ो'],
        'au': ['औ', 'ौ']}
    consonants = {
        'k': 'क',
        'kh': 'ख',
        'g': 'ग',
        'gh': 'घ',
        'ṅ': 'ङ',
        'c': 'च',
        'ch': 'छ',
        'j': 'ज',
        'jh': 'झ',
        'ñ': 'ञ',
        'ṭ': 'ट',
        'ṭh': 'ठ',
        'ḍ': 'ड',
        'ḍh': 'ढ',
        'ṇ': 'ण',
        't': 'त',
        'th': 'थ',
        'd': 'द',
        'dh': 'ध',
        'n': 'न',
        'p': 'प',
        'ph': 'फ',
        'b': 'ब',
        'bh': 'भ',
        'm': 'म',
        'y': 'य',
        'r': 'र',
        'l': 'ल',
        'v': 'व',
        'ś': 'श',
        'ṣ': 'ष',
        's': 'स',
        'h': 'ह'}
        
    others = {
        'ṃ': 'ं',
        'ḥ': 'ः',
        'ṁ': 'ँ',
        "'": 'ऽ',
        '0': '०',
        '1': '१',
        '2': '२',
        '3': '३',
        '4': '४',
        '5': '५',
        '6': '६',
        '7': '७',
        '8': '८',
        '9': '९'}

    tgt = ''
    boo = False
    inc = 0
    while inc < len(src):
        pre = src[inc-1] if inc > 1 else ''
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        dnxt = src[inc+2] if inc < len(src) - 2 else ''
        if now+nxt in consonants:
            tgt += consonants[now+nxt]
            if dnxt == 'a':
                inc += 1
            elif dnxt in vowels:
                boo = True
            else:
                tgt += '्'
            inc += 1
        elif now+nxt in vowels:
            if boo:
                tgt += vowels[now+nxt][1]
                boo = False
            else:
                tgt += vowels[now+nxt][0]
            inc += 1
        elif now in consonants:
            tgt += consonants[now]
            if nxt == 'a':
                inc += 1
            elif nxt in vowels:
                boo = True
            else:
                tgt += '्'
        elif now in vowels:
            if boo:
                tgt += vowels[now][1]
                boo = False
            else:
                tgt += vowels[now][0]
        elif now == '\'':
            if not pre or not nxt:
                tgt += now
            elif ord(pre) in range(65, 123) and ord(nxt) in range(65, 123):
                tgt += 'ऽ'
            else:
                tgt += now
        elif now in others:
            tgt += others[now]
        elif now == '.':
            if nxt == '.':
                tgt += '॥'
                inc += 1
            else:
                tgt += '।'
        else:
            tgt += now
        inc += 1
    return tgt