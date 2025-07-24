num = int(input("Enter the number of messages: "))
messages = []
user_count = {}
for _ in range(num):
    messages.append(input())
chat_data = []
for line in messages:
    if ":" in line:
        name, msg = line.split(":", 1)
        chat_data.append((name.strip(), msg.strip()))
print(chat_data)

while True:
    print("1. Count total number of messages in the chat")
    print("2.Identify unique users in the chat")
    print("3.Count total words in the chat")
    print("4.Calculate average words per message")
    print("5.Find the longest message sent")
    print("6.Find the most active user")
    print("7.Get message count for a specific user")
    print("8.Find the most frequently used word by a specific user")
    print("9.Retrieve the first and last message sent by a user")
    print("10.Check if a user is present in the chat")
    print("11.Find commonly repeated words")
    print("12.Identify the user with the longest average message length")
    print("13.Count how many messages mention a specific user")
    print("14.Remove duplicate messages")
    print("15.Sort messages alphabetically")
    print("16.Extract all questions asked in the chat")
    print("17.Calculate the reply ratio between two users")
    print("18. Check for deleted messages")
    print("0.Exit")
    
    ch = int(input("Enter your choice:"))
    if ch==1:
        print(f"Count total number of messages in the chat :{len(chat_data)}")
    elif ch==2:
        users = sorted(set(name.strip() for name, _ in chat_data))
        print("Unique users in the chat:",users)
    elif ch==3:
        total_words = 0
        for _, msg in chat_data:
            total_words += len(msg.split())
        print(f"Count total words in the chat :{total_words}")
    elif ch==4:
        avg_words = total_words / len(chat_data) 
        print("Average words per message:", round(avg_words, 2))
    elif ch==5:
        longest_msg = ""
        for msg in messages:
            if len(msg.split()) > len(longest_msg.split()):
                longest_msg = msg
        print("Longest message:", longest_msg)
    elif ch==6:
        user_count = {}
        for name, _ in chat_data:
            if name in user_count:
                user_count[name] += 1
            else:
                user_count[name] = 1
        most_active_user = max(user_count, key=user_count.get)
        print("Most active user:", most_active_user)
    elif ch==7:
        user_name = input("Enter the user name to get message count: ")
        count = sum(1 for name, _ in chat_data if name == user_name)
        print(f"Message count for {user_name}: {count}")
    elif ch==8:
        user_name = input("Enter the user name to find most frequently used word: ")
        word_count = {}
        for name, msg in chat_data:
            if name == user_name:
                for word in msg.split():
                    word_count[word] = word_count.get(word, 0) + 1
        most_frequent_word = max(word_count, key=word_count.get, default=None)
        print(f"Most frequently used word by {user_name}: {most_frequent_word}")
    elif ch==9:
        user_name = input("Enter the user name to retrieve first and last message: ")
        first_msg = next((msg for name, msg in chat_data if name == user_name), None)
        last_msg = next((msg for name, msg in reversed(chat_data) if name == user_name), None)
        print(f"First message by {user_name}: {first_msg}")
        print(f"Last message by {user_name}: {last_msg}")
    elif ch==10:
        user_name = input("Enter the user name to check presence: ")
        is_present = any(name == user_name for name, _ in chat_data)
        print(f"Is {user_name} present in the chat? {'Yes' if is_present else 'No'}")
    elif ch==11:
        word_count = {}
        for _, msg in chat_data:
            for word in msg.lower().split():
                word_count[word] = word_count.get(word, 0) + 1
        repeated = [word for word in word_count if word_count[word] > 1]
        print("Common repeated words:", repeated)
    elif ch==12:
        avg_length = {}
        for name, msg in chat_data:
            avg_length[name] = avg_length.get(name, []) + [len(msg)]
        longest_avg_user = max(avg_length, key=lambda k: sum(avg_length[k]) / len(avg_length[k]))
        print(f"User with longest average message length: {longest_avg_user}")
    elif ch==13:
        specific_user = input("Enter the specific user to count mentions: ")
        mention_count = sum(1 for _, msg in chat_data if specific_user in msg)
        print("Count of messages mentioning", specific_user, ":", mention_count)
    elif ch==14:
        unique_messages = list(set(messages))
        print("Messages after removing duplicates:", unique_messages) 
    elif ch==15:
        sorted_messages = sorted(messages)
        print("Messages sorted alphabetically:", sorted_messages)
    elif ch==16:
        questions = [msg for _, msg in chat_data if msg.endswith('?')]
        print("Questions asked in the chat:", questions)
    elif ch==17:
        user1 = input("Enter the first user: ")
        user2 = input("Enter the second user: ")
        replies = sum(1 for name, msg in chat_data if name == user2 and msg.startswith(f"{user1}:"))
        total_messages = sum(1 for name, _ in chat_data if name == user1)
        reply_ratio = replies / total_messages if total_messages > 0 else 0
        print(f"Reply ratio of {user2} to {user1}: {reply_ratio:.2f}")
    elif ch==18:
        deleted_messages = [msg for msg in messages if msg.startswith("DELETED")]
        if deleted_messages:
            print("Deleted messages found:", deleted_messages)
        else:
            print("No deleted messages found.")
    elif ch==0:
        print("Exiting the chat analysis.")
        break
    else:
        print("Invalid choice, please try again.")  