# File: phonetic_map.py
PHONETIC_CONFUSION_MAP = {
    'clean_character_1': ['noisy_substitute_1', 'noisy_substitute_2'],
    'ក': ['គ'],
    'ខ': ['ឃ'],        # khâ – aspirated k
    'គ': ['ក'],        # ko – similar to kâ
    'ឃ': ['ខ'],        # kho – similar to khâ

    'ច': ['ឆ', 'ជ', 'ឈ'],        # châ – unaspirated ch
    'ឆ': ['ច', 'ជ', 'ឈ'],        # chhâ – aspirated ch
    'ជ': ['ច', 'ឆ', 'ឈ'],        # cho – similar to châ
    'ឈ': ['ច', 'ឆ', 'ជ'],        # chho – similar to chhâ
    'ញ': ['ជ'],        # ño – nasal sound

    'ដ': ['ឌ', 'ត', 'ទ'],        # dâ – unaspirated d
    'ឋ': ['ឍ', 'ថ', 'ធ'],        # thâ – aspirated t
    'ឌ': ['ដ', 'ទ', 'ធ'],        # do – similar to dâ
    'ឍ': ['ឋ', 'ថ'],        # tho – similar to thâ
    'ណ': ['ន'],        # nâ – nasal alveolar

    'ត': ['ទ', 'ដ', 'ឌ'],        # tâ – unaspirated t
    'ថ': ['ធ', 'ឋ', 'ឍ'],        # thâ – aspirated t
    'ទ': ['ត', 'ដ', 'ឌ'],        # to – similar to tâ
    'ធ': ['ថ', 'ឋ', 'ឍ'],        # tho – similar to thâ
    'ន': ['ណ'],        # nô – nasal alveolar

    'ប': ['ព', 'ផ', 'ភ'],        # bâ – unaspirated b/p
    'ផ': ['ភ', 'ប', 'ព'],        # phâ – aspirated p
    'ព': ['ប', 'ផ', 'ភ'],        # po – similar to bâ
    'ភ': ['ផ', 'ប', 'ព'],        # pho – similar to phâ
    'ម': ['ប', 'ព'],        # mô – nasal m

    'យ': ['យ', 'ញ'],        # yô
    'រ': ['ល', 'ឡ'],        # rô – similar to lô
    'ល': ['រ', 'ឡ'],        # lô – similar to rô
    'វ': ['ប', 'ព'],        # vô – w/v sound

    'ស': ['ហ'],        # sâ – sometimes close to hâ
    'ហ': ['ស'],        # hâ – similar friction sound
    'ឡ': ['ល', 'រ', 'អ'],        # lâ – similar to lô
    'អ': ['អ', 'ឡ'],         # ’â – glottal, base consonant

# 23 vowels 
    'ា': ['ោ', 'ៀ'],        # aa – long vowel
    'ិ': ['ឺ', 'ី', 'ឹ'],        # i – short vowel
    'ី': ['ឺ', 'ិ', 'ឹ'],        # ii – long vowel  
    'ឹ': ['ឺ', 'ី', 'ិ'],        # ê – short vowel
    'ឺ': ['ិ', 'ី', 'ឹ'],        # êe – long vowel
    'ុ': ['ូ'],        # u – short vowel
    'ូ': ['ុ'],        # uu – long vowel
    'ួ': ['ុ', 'ូ'],      # ua – diphthong
    'ើ': ['ឿ', 'ៀ'],     # oe – diphthong
    'ឿ': ['ើ', 'ៀ'],     # oee – diphth
    'ៀ': ['ើ', 'ឿ'],     # iee – diphthong
    'េ': ['ែ', 'ៃ'],        # e – short vowel
    'ែ': ['េ', 'ៃ'],        # ae – long vowel
    'ៃ': ['េ', 'ែ'],      # ai – diphthong
    'ោ': ['ៅ'],        # o – long vowel
    'ៅ': ['ោ'],        # ao – diphthong
    'ុំ': ['ះ'],     # om – nasal final
    'ំ': ['ះ', 'ាំ', 'ុំ'],      # am – nasal final
    'ាំ': ['ះ'],     # aam – nasal final long
    'ះ': ['ុះ','ោះ', 'េះ'],     # h – final consonant
    'ុះ': ['ះ','ោះ', 'េះ'],    # uh – final vowel
    'េះ': ['ុះ', 'ះ', 'ោះ'],    # eh – final vowel
    'ោះ': ['ុះ', 'ះ', 'េះ']    # oh – final vowel

}