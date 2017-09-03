import urllib

### Funtion to read the file
def read_text():
    quotes = open('sample.txt')
    contents = quotes.read()
    ### Print orignal content
    print(contents)
    quotes.close()
    check_profanity(contents)

### Function to check profanity
def check_profanity(check):
    ### Access Purgomalum Api for profanity words
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" + check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!! Check Your Document!")
        doted = urllib.urlopen("http://www.purgomalum.com/service/plain?text=" + check)
        doted_output = doted.read()
        ### Print dotted content
        print(doted_output)
        doted.close()
    if "false" in output:
        print("Success!! No Profanity!!")
read_text()
