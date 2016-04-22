def main():
    count = 0
    my_string = raw_input("Enter a sentence:")
    for ch in my_string:
        if ch == "T" or ch == "t":
            count += 1
    print "The letter T appears", count, "time."

main()
