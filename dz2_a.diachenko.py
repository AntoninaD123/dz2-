
#task 1

from queue import Queue
import time

# Створюємо чергу
request_queue = Queue()
request_id = 1  # лічильник заявок

def generate_request():
    global request_id
    request = f"Request-{request_id}"
    print(f"Створено: {request}")
    request_queue.put(request)
    request_id += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється: {request}")
    else:
        print("Черга пуста, немає що обробляти.")

def main():
    print("Система обробки заявок запущена. Натисніть Ctrl+C для зупинки.")
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(1)  # затримка для наочності
    except KeyboardInterrupt:
        print("\n Програма завершена.")

if __name__ == "__main__":
    main()


#task 2

from collections import deque

def is_palindrome(text: str) -> bool:
    # прибираємо пробіли та регістр
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    
    dq = deque(cleaned)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


# приклади:
s1 = "A man a plan a canal Panama"
s2 = "Hello"

print(f'"{s1}" →', "паліндром" if is_palindrome(s1) else "не паліндром")
print(f'"{s2}" →', "паліндром" if is_palindrome(s2) else "не паліндром")
