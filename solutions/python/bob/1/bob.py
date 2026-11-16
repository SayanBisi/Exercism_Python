def response(hey_bob):
    bob_reply = ""
    
    if (hey_bob.strip()).endswith('?'):
        if hey_bob.isupper():
            bob_reply = "Calm down, I know what I'm doing!"
        else:
            bob_reply = "Sure."
    else:
        if len(hey_bob.split()) == 0:
            bob_reply = "Fine. Be that way!"
        elif hey_bob.isupper():
            bob_reply = "Whoa, chill out!"
        else:
            bob_reply = "Whatever."
    
    return bob_reply