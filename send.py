def sender():
    while True:
        text = input("Sender: ")
        if text == "":
            break

        f = open("data.txt", "w")
        f.write(text)
        f.close()



def send_input():
    while True:
        text = input("Sender: ")
        if text == "":
            break
        print("sent:", text)

if __name__ == "__main__":
    send_input()