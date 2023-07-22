### --- OOP Email Simulator --- ###

# --- Email Class --- #

class Email():
    
    # Create Class variable with default False for unread e-mails.
    _has_been_read = False
    
    # Construct class variables.
    def __init__(self,email_address,subject_line,email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def show_subject(self):
        '''Only returns the subject line'''
        return self.subject_line
    
    def mark_as_read(self):
        '''Change the class variable to True if e-mail is read.'''
        self._has_been_read = True
        return self._has_been_read  
    
    def read_mail(self):
        '''Prints sender, subject and body text information'''
        print(f"From: \t\t {self.email_address}")
        print(f"Subject: \t {self.subject_line}")
        print(f"Body: \t\t {self.email_content}")

# --- Lists --- #
# Define empty inbox list.
print("Changes")
inbox = []

# --- Functions --- #

def populate_inbox(list_item):
    ''' Add sample mails to inbox and initialise objects.''' 
     
    mail_1 = Email("deist@oimgroup.com", "Hurry up!", "Hi Heino, Frobnicate the Python OOP section to within an inch of it's life.")
    mail_2 = Email("grrtzgrrtz@gmail.com", "Last chance", "I am a prince and your name is on the title deed to royal inheritance")
    mail_3 = Email("angelina.jolie@gmail.com", "Also last chance", "I miss you and I apologise for all my mistakes")
        
    list_item.append(mail_1)
    list_item.append(mail_2)
    list_item.append(mail_3)
    
    return list_item

def list_emails(inbox):
    '''Print mail subject line with corresponding number'''
    
    # https://www.webucator.com/article/how-to-use-enumerate-to-print-a-numbered-list-in-p/
    # Accessed 7 June 2023. Needed more help on using the enumerator function.
    for mail_num, item in enumerate(inbox,0):
        print(f"{mail_num} {inbox[mail_num].show_subject()}")
    
def read_email(index):
    '''Call the inbox object from list and pass to read_mail method, and mark_as_read method'''
    
    inbox[index].read_mail()
    print(inbox[index].mark_as_read())
    #inbox[index]._has_been_read = True
    print(f"\nEmail from {inbox[index].email_address} has been marked as read. ")
    

# --- Email Program --- #

# Call the function populate_inbox to populate the Inbox for further use.

inbox = populate_inbox(inbox)
print("Current Mails in you inbox:")
list_emails(inbox)

# User selects menu options. 

menu = True

while True:
    user_choice = int(input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: '''))

    if user_choice == 1:
        select_mail = int(input("Select mail item number to read: "))
        read_email(select_mail)

    elif user_choice == 2:
        print("You have the following unread mails: ")
        for mail, item in enumerate(inbox,0):
            if inbox[mail]._has_been_read != True:
                print(f"{mail} {inbox[mail].show_subject()}")
               
    elif user_choice == 3:
        exit()
        
    else:
        print("Oops - incorrect input.")
    
