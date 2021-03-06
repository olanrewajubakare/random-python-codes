verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse)), "\n")
print("The first occurrence of the word 'and' occurs at the {}th index.".format(verse.find('and')), "\n")
print("The last occurrence of 'you' is at the {}th index.".format(verse.rfind('you')), "\n")
print("the word 'can' occurs {} time in the verse".format(verse.count('can')))