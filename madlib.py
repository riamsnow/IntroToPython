print("""Welcome to Madlibs!
You'll be asked for different nouns and verbs.
Try to keep them funny.
Have fun!""")
plural_noun = raw_input("Please provide a plural noun:")
noun1 = raw_input("Please provide a noun:")
noun2 = raw_input("Please provide a noun:")
song = raw_input("Please provide the title of a song:")
verb = raw_input("Please provide a present tense verb:")
madlibs = ("""Learning to drive is a tricky process. There are a few rules to follow.
1. Keep two %s on the steering wheel at all times.
2. Step on the %s to speed up and the %s to slow down.
3. Your parents will just LOVE it if you play %s on the radio.
4. Make sure you hong your horn when you see %s on a street sign.""")

print(madlibs %(plural_noun, noun1, noun2, song, verb))