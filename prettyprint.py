TAX_RATE = 0.0846  # 8.46%

SEPARATOR_LINE = "================================================="

def main():

    # prettyprinting
    # formatting output is messy in every computer language
    # here's how in Python (it's comes from the C language)

    billToLastName = "Smythe"
    billToFirstName = "John"

    billBeforeTax = 13.28

    # calc amounts owed
    taxAmt = billBeforeTax * TAX_RATE
    amtOwed = billBeforeTax + taxAmt

    print SEPARATOR_LINE
    print "This is your bill %s, %s" % (billToLastName, billToFirstName)
    print SEPARATOR_LINE
    print "      Purchase amount: $%.2f" % billBeforeTax
    print "The government adds on $%.2f" % taxAmt
    print "               You owe $%.2f" % amtOwed
    print SEPARATOR_LINE
    
    # s for string
    # f for floating point
    # .2 for two decimal places
    # all the % places in the string must be filled in with
    # the data that follows the % after the string
    # there's also d for decimal
    
    # if there's are more than fill-in value, you need parentheses
    print "Look %s, I'm %d years old!" % ("Maw", 7)

    # don't spend too much time of formatting, though
    # there's usually a completely different set of programmers
    # who work on that aspect of things.


# are we being executed?
if __name__ == '__main__':
    main()
