import socket as s
website = input("Enter url: ")
print("IP:",s.gethostbyname(website))