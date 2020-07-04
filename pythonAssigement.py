
import re
import csv
import json
##########


para = '''
"Python is great language!", said Fred. "I don't ever remember having this much fun before."
'''
print('''Create a variable, paragraph, that has the following content: "Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')
print(para)

# 2) Write an if statement to determine whether a variable holding a year is a leap year.


def leapYear(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return str(year)+' is a leap year'
            else:
                return str(year)+' not a leap year'
        else:
            return str(year)+' is a leap year'
    else:
        return str(year)+' not a leap year'


year = input('Enter input a year to check is a leap year or not >> ')
print()
print(leapYear(year))


# 3) Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.

def anagram_word(word_list):
    anagram_list = []
    for word_1 in word_list:
        for word_2 in word_list:
            if word_1 != word_2 and (sorted(word_1) == sorted(word_2)):
                anagram_list.append(word_1)
    return anagram_list


print()
print(anagram_word(["percussion", "supersonic",
                    "car", "tree", "boy", "girl", "arc"]))

# 4) Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list. What is the first item on the list? What is the second item on the list?


def listCheck():
    word = []
    print(id(word))
    word.append('prayag')
    word.append('Ruby')
    word.append('Aayush')
    word.append('stefen')
    print(id(word))
    word.sort()
    print(word[0])
    print(word[1])


print()
listCheck()

# 5) Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to it. Make more tuples with the corresponding information from your friends and append them to the list. Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age.


def sortOnFirst(elem):
    return elem[2]


def sortValue():
    info = ('prayag', 'piya', 20)
    people = []
    people.append(info)
    info = ('Sandhya', 'Gurung', 18)
    people.append(info)
    info = ('Shrijan', 'shresth', 16)
    people.append(info)
    people.sort(key=sortOnFirst)
    return people


print(5)
print(sortValue())

# 6) Create a list with the names of friends and colleagues. Search for the name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


def searchList():
    searchCase = False
    person = ['riya', 'prayag', 'sandhya', 'Jhon']
    for i in person:
        if i == 'Jhon':
            searchCase = True
            break
        else:
            searchCase = False

    if searchCase:
        print("Found")
    else:
        print('Not Found')


print()
searchList()

# 7) Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young if they are above or below the average age.


def avgeAge():
    people = [('prayag', 'piya', 20), ('Ruby', 'Gurung', None),
              ('Sandhya', 'Gurung', 19), ('Umesh', 'Piya', 42)]
    AVGAGE = 25
    for i in people:
        if i[2] != None and i[2] < AVGAGE:
            print(i[0] + " is a young person who's age is " + str(i[2]))
        elif i[2] != None and i[2] > AVGAGE:
            print(i[0] + " is a old person who's age is " + str(i[2]))
        else:
            print(i[0] + "'s age is not catagorise")


print()
avgeAge()


# 8) Write a function, is_prime, that takes an integer and returns True if the number is prime and False if the number is not prime.

def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count > 2:
        print('Not a Prime')
    else:
        print('Is Prime')


print()
num = int(input('Enter a number to check weather is a prime or not  >>'))
is_prime(num)


# 9) Write a binary search function. It should take a sorted sequence and the item it is looking for. It should return the index of the item if found. It should return -1 if the item is not found.


# 10) Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well.

def caseString(string, camelCase='_'):
    char = ''
    var = re.findall('[A-Z][^A-Z]*', string)
    return camelCase.join(var)


print()
print(caseString('PrayagGoodBoy'))
print(caseString('PrayagGoodBoy', '-'))


# 11) Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, find the extension. For README.txt, the extension should be txt. Write code using slice operations that will give the name without the extension. Does your code work on filenames of arbitrary length?

def sliceExtension(filename):
    value = filename.split('.')
    return value[0]


print()
print(sliceExtension('README.txt'))

# 12) Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.


def is_palindrome(string):
    ans = string == string[::-1]
    if ans:
        return 'Is Palindrome'
    else:
        return 'Not a Palindrome'


print()
print(is_palindrome('Prayag'))

# 13) Write a function to write a comma-separated value (CSV) file. It should accept a filename and a list of tuples as parameters. The tuples should have a name, address, and age. The file should create a header row followed by a row for each tuple.


def write_into_CSV(filename, value):
    file = open(filename+'.csv', 'w', newline='')
    writer = csv.writer(file)

    writer.writerow(['Name', 'Address', 'Age'])
    for i in value:
        writer.writerow(i)


write_into_CSV('person', [('prayag', 'chitwan', 20),
                          ('Jon', 'Winter', 30), ('Araya', 'Winter', 20)])


def read_from_CSV(filename):
    file = open(filename+'.csv', 'r')
    read = csv.reader(file)
    info = []
    finalData = []
    for rows in read:
        info.append(rows)

    for i in range(1, len(info)):
        a = {}
        for j in range(len(info[i])):
            a[info[0][j]] = info[i][j]

        finalData.append(a)
    print(finalData)


read_from_CSV('person')

# 15) Imagine you are designing a banking application. What would a customer look like? What attributes would she have? What methods would she have?


class Bank:
    def customer(self, name, number, email, address):
        self.name = name
        self.email = email
        self.number = number
        self.address = address

    def bankAccount(self, accountNumber, amount):
        self.accountNumber = accountNumber
        self.amount = int(amount)

    def display(self):
        print('Hello {},'.format(self.name))
        print('Your Personal Info {} number {} address {}'.format(
            self.email, self.number, self.address))
        print('Your bank account {} amount {}'. format(
            self.accountNumber, self.amount))

    def withDraw(self, withDrawamount):
        self.withDrawamount = int(withDrawamount)

        if self.amount < self.withDrawamount:
            print('You dont have sufficient amount')
        else:
            self.amount = self.amount - self.withDrawamount
            print('Withdraw sucessful')
            print('Your total amount is {}'.format(self.amount))

    def Desposit(self, depositAmt):
        self.depositAmt = int(depositAmt)
        self.amount = self.amount + self.depositAmt
        print('Deposit Sucessful')
        print('Your total amount is {}'.format(self.amount))


print()
obj = Bank()
obj.customer('prayag', '98455667', 'test@gmail.com', 'chitwan')
obj.bankAccount('234567ABC', 200000)
obj.display()
obj.withDraw(20000)


# 16) Imagine you are creating a Super Mario game. You need to definea class to represent Mario. What would it look like? If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.

class GTA:
    def player(self, playerHandel, money, guns, friends):
        self.playerHandel = playerHandel
        self.money = money
        self.guns = guns
        self.friends = friends

    def display(self):
        print('Hello {}'.format(self.playerHandel))
        print('Your balance is {}'.format(self.money))
        print('Your weapons {} and your friends {}'.format(
            self.guns, self.friends))


print()
obj1 = GTA()
obj1.playerHandel('@Kerbrose-2001', 2000000000, ['NK-14', 'M416', 'AKM'], 20)
obj1.display()


# 17) Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator. Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.

def Calculator:
    def add(self, num, num1):
        try:
            return int(num)+int(num1)
        except:
            return 'Not int'

    def sub(self, num, num1):
        try:
            return int(num)-int(num1)
        except:
            return 'Not int'

    def divide(self, num, num1):
        try:
            return int(num)/int(num1)
        except Exception as e:
            return e

    def multiply(self, num, num1):
        try:
            return int(num)*int(num1)
        except:
            return 'Not int'


print()
obj2 = Calculator()
print(obj2.add(5, 10))


def jsonConverstion():
    person = '{"name":"Prayag", "age":20}'
    x = json.loads(person)
    print(x['name'], x['age'])

    b = json.dumps(x)
    print(b)


print()
jsonConverstion()


class Brackets:
    def check(self, string):
        stack = []
        pchar = {'(': ')', '{': '}', '[': ']'}
        for para in string:
            if para in pchar:
                stack.append(para)
            elif len(stack) == 0 or pchar[stack.pop()] != para:
                return False
        return len(stack) == 0


obj3 = Brackets()
print(obj3.check("(){}[]"))


class py_solution:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
