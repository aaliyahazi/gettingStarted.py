### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.
### aaliyah
def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.

    #1
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    #2
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    #3
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    #4
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    #5
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    #6
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    #7
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = '7c80a071b2fb1a5e0dc4af36d3d7b6d61468d6cd87284f0b46da4a1cd7e27b92'
    #8
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    #9
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else:
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
