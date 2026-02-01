def receiver():
    while True:
        f = open("data.txt", "r")
        text = f.read()
        f.close()

        if text:
            print("Receiver got:", text)


def receive_input():
    while True:
        text = input("Receiver (type message): ")
        if text == "":
            break
        print("received:", text)

if __name__ == "__main__":
    receiver()