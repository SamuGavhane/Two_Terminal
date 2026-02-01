def receive_input():
    while True:
        text = input("Receiver (type message): ")
        if text == "":
            break
        print("received:", text)

if __name__ == "__main__":
    receive_input()