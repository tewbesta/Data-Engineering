# # Homework 1

# ## Q1

# Write a function to sum all the values in a dictionary.

# sumValues(dictionary) takes as input a dictionary (with integer values), and returns the sum of the
# values for all keys in the dictionary!
#
# Example:
#   print( sumValues({"a" : 7, "b" : 10}) ) # outputs 17

def sumValues(dictionary):

    ### BEGIN SOLUTION

    sum_value = 0;
    for key, value in dictionary.items():
        sum_value = sum_value + value;

    return sum_value

    ### END SOLUTION




# ## Q2

# Write a function to find the key corresponding to the maximum value in a dictionary.

# maxValue(dictionary) takes as input a dictionary (with integer values), and returns the key
# associated with the maximum value in the dictionary.
#
# Example:
#   print( maxValue({"a" : 7, "b" : 10}) ) # outputs b
def isPalindrome(string):
    
        newstring = string.lower()
        a = []
        b = []
    
        for elem in newstring:
            if elem != " ":
                a.append(elem)
        
        b = a.copy()
        b.reverse()
        
        #print(a)
        #print(b)
        
        if len(a) != 0:
            if len(b) != 0:
                return(a==b)


def maxValue(dictionary):

    ### BEGIN SOLUTION

    max_value = float('-inf')
    max_key = None

    for key, value in dictionary.items():
        if(value > max_value):
            max_value = value
            max_key = key

    return max_key

    ### END SOLUTION




# ## Q3

# Write a function to find the number of unique elements in a list of integers and characters.

# numberOfUniqueElements(listOfElements) takes as input a list, and returns the number of unique
# elements in the list.
#
# Example:
#   print( numberOfUniqueElements([1,2,2,'c']) ) # outputs 3

def numberOfUniqueElements(listOfElements):


    ### BEGIN SOLUTION

    #setL = set(listOfElements);
    #return len(setL);

    dic = {}
    for i in range(len(listOfElements)):
        key = listOfElements[i]
        dic[key] = 1

    num_unique_elements = len(list(dic.keys()))

    return num_unique_elements

    ### END SOLUTION




# ## Q4

# Write a function that splits a given sentence into words and counts the number of words. The
# sentence consists of alphanumeric characters, and the words are separated by spaces. You should
# use the split() function in python to split a string.

# For all the questions, assume that the words are separated by whitespace character, unless
# specified otherwise.

# splitStringCount(string) takes as input a sentence, splits the string into words and returns a
# count of the number words obtained

#
# Example:
#   print( splitStringCount('The train was late') ) # outputs 4

def splitStringCount(string):

    ### BEGIN SOLUTION

    tokens = string.split()
    return len(tokens)

    ### END SOLUTION



# ## Q5

# Write a function to check if a string is a palindrome.

# isPalindrome(string) takes as input a string, and returns a boolean value indicating whether the
# input string is a palindrome or not. The output should be case insensitive. Also, empty strings
# are not considered as palindromes.
#
# Example:
#   print( isPalindrome("banana") ) # outputs False
#   print( isPalindrome("madam") )  # outputs True
#   print( isPalindrome("Anna") )   # outputs True

def isPalindrome(string):
    ### BEGIN SOLUTION
    string = string.lower();
    check = True;
    n = len(string)
    if(n==0):
        return False;
    temp = n//2;
    for i in range(0, temp):
        if(string[i]!=string[n-i-1]):
            check = False;
            break;
    if(check == True):
        return True;
    else:
        return False;
    ### END SOLUTION

# ## Q6

# Write a function to find the unique palindromes in a given string.

# uniquePalindromes(string) takes as input a string delimited by whitespace characters, and returns
# a list of unique palindromes in the string. You should convert the given string to lowercase. The
# output list must be sorted in decreasing lexicographic order (reverse sorted order). You should
# return an empty list if the string doesn't contain any palindrome words. You can use your above
# defined function 'isPalindrome' to check if a word is palindrome or not.

#
# Example:
#   print( uniquePalindromes('Madam asked Anna to go out but Anna refused') ) # outputs ['madam', 'anna']
#   print( uniquePalindromes('Palindromes are also found in numbers and are studied in recreational mathematics') ) # outputs []


def uniquePalindromes(string):

    ### BEGIN SOLUTION
    string = string.lower()
    d = {}
    check = False
    tokens = string.split()
    for word in tokens:
        if(isPalindrome(word)==True):
            d[word] = 1
            check = True

    if(check==True):
        return sorted(list(d.keys()), reverse=True)
    else:
        return []


    ### END SOLUTION


# ## Q7

# Write a function to read in from a given file and count the number of words in each line.

# numWords(filename) takes as input the file to read the text from, and returns a list of number of
# words in each line. The words in the input file are separated by whitespace. The output should be
# in the order of lines in the file. You can use your code in Q4 above to split the lines into words
# and count the number of words.
#
# Example:
# print( numWords('raven-poem_demo.txt') ) # outputs [11, 10, 10, 11, 11, 5, 0, 10, 11, 12, 13, 12, 4, 0, 10, 11, 13, 10, 10, 6, 0,
# 9, 10, 13, 11, 16, 5, 0, 11, 10, 11, 11, 11, 5, 0, 11, 14, 13, 12, 13, 5, 0, 10, 12, 8, 12, 10, 2, 0, 11, 14, 10, 11,
# 11, 4, 0, 10, 12, 12, 10, 10, 5]
#

def numWords(filename):

    ### BEGIN SOLUTION

    output = []
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            output.append(len(words))
    # print (len(output))
    return output


    ### END SOLUTION

# ## Q8

# Write a function to calculate the average number of words in each line of a given file.

# averageWords(filename) takes as input the filename to read from, and returns the average number of
# words per line in that file.
#
# Example:
#     print( averageWords('raven-poem_demo.txt') ) # outputs 8.79...
#

def averageWords(filename):

    ### BEGIN SOLUTION
    output = numWords(filename)
    total = 0
    for item in output:
        total = total + item
    # print (len(output))
    average = (total * 1.0)/len(output)
    return average

#averageWords('raven-poem_demo.txt')

    ### END SOLUTION



# ## Q9:

# Write a function to count the number of lines in a file, containing the substring "ing".

# countLines(filename) takes as input the filename to read from, and returns the number of lines that
# contain the substring 'ing'. All occurrences of the given substring in a line are counted only once.
#
# Example:
#     print( countLines('raven-poem_demo.txt') ) # outputs 27
#

def countLines(filename):

    ### BEGIN SOLUTION

    count = 0;
    with open(filename, 'r') as f:
        for line in f:
            if ('ing' in line):
                count = count + 1;
    return count

#countLines('raven-poem_demo.txt')
    ### END SOLUTION




# ## Q10

# Write a function to read text from an input file, find all unique palindromes and return them in
# sorted order.

# findPalindromes(filename) takes as input the file to read the text from, and returns a list of the
# unique palindromes sorted in decreasing lexicographic order (reverse sorted order), in lower case.
# You can use your code above for checking if a string is a palindrome.

# For example,
# filename: palindrome_test.txt
# output: ['tattarrattat', 'redivider', 'detartrated', 'aibohphobia', 'a']


def findPalindromes(filename):

    ### BEGIN SOLUTION

    in_fd = open(filename , 'r')
    words = [];
    for line in in_fd:
        line = line.lower();
        tokens = line.split();
        words = words + tokens;
    uniqueWords = list(set(words));
    uniqueWords = list(sorted(uniqueWords, reverse=True))

    count = 0;
    palindromes = [];
    #out_fd = open(outputFile, 'a')
    for word in uniqueWords:
        if(isPalindrome(word)==True):
            #out_fd.write(word + '\n');
            count = count + 1;
            palindromes.append(word)


    #print(count)
    return palindromes

    ### END SOLUTION
