<<<<<<< HEAD
def max_finder(array):
    if not array:
        return None
    return max(array)
    
if __name__ == "__main__":
    count = int(input("Введите количество элементов:"))
    array = []
    for i in range(count):
        k = float(input("Введите число:"))
        array.append(k)
=======
def max_finder(array):
    if not array:
        return None
    return max(array)
    
if __name__ == "__main__":
    count = int(input("Введите количество элементов:"))
    array = []
    for i in range(count):
        k = float(input("Введите число:"))
        array.append(k)
>>>>>>> 285ffe332c47ab37a846c6435f471c97dd9962d0
    print("Найден максимум:",max_finder(array))