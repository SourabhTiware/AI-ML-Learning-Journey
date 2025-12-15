# Mini Project - OOP chat system
# Let's create a Chat System using OOP's concepts. We have to create classes:
#       User
#       Message
#       ChatRoom
# And we have to implement functions:
#       sending messages
#       viewsing chat history
#       user joining and leaving the chatroom

# Message Class

class Message:
    message_counter = 1 # counter

    def __init__(self,sender,content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter +=1
    
    def __str__(self):
        return f"{self.id} {self.sender.username}:{self.content} \n"


# User class

class User:
    def __init__(self,username):
        self.username = username
        self.chatroom = None
    
    def join_chatroom(self,chatroom):
        self.chatroom = None
        if self.chatroom:
            print(f"{self.username} is already in a chatroom \n ")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name} \n ")
    
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom \n ")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name} \n ")
            self.chatroom = None
    
    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom) \n ")
        else:
            self.chatroom.broadcast(self,content)

# ChatRoom Class

class ChatRoom:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self,user):
        self.users.append(user)
    
    def remove_user(self,user):
        self.users.remove(user)
    
    def broadcast(self, sender, content):
        message = Message(sender,content)
        self.messages.append(message)
        print(message) # show message to all users
    
    def show_chat_history(self):
        print(f"\n Chat History of {self.name}:")
        for msg in self.messages:
            print(msg)
            print()


# Example Usage

if __name__ == "__main__":
    room = ChatRoom("Python Lounge ")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone")
    u2.send_message("Hi Alice !")

    u3.join_chatroom(room)
    u2.send_message("Hey guys, What's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u2.leave_chatroom()