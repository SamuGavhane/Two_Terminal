def send_input():
    while True:
        text = input("Sender: ")
        if text == "":
            break
        print("sent:", text)

if __name__ == "__main__":
    send_input()