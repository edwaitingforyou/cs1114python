def dictOfEng():
    '''
    This is a function to distinguish the type of words.
    '''
    
    wordByUser = raw_input("Enter a word:")
    if wordByUser == "a" or wordByUser == "an" or wordByUser == "the":
        print '\"'+wordByUser+'\"',"is an article."
    elif wordByUser == "another" or wordByUser == "both" or wordByUser == "ererything" or wordByUser == "noting":
        print '\"'+wordByUser+'\"',"is an indefinite pronoun."
    elif wordByUser == "this" or wordByUser == "that" or wordByUser == "these" or wordByUser == "those":
        print '\"'+wordByUser+'\"',"is a demonstrative pronoun."
    elif wordByUser == "I" or wordByUser == "i" or wordByUser == "you" or wordByUser == "she" or\
         wordByUser == "it" or wordByUser == "we" or wordByUser == "they":
        print '\"'+wordByUser+'\"',"is a subjective personal pronoun."
    else:
        print '\"'+wordByUser+'\"',"is not a part of speech we care about."
