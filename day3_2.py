#Function
def print_name(name):
    print(name.title())
    return
print_name("adesh")


text="ababa"
def check_palindrome(text):
    '''Takes one string argument and checks wheather it is palindrome or not'''
    if text.lower() == text[::-1].lower():
        return True
    return False
if check_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
