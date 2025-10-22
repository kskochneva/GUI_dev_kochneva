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
    print("Найден максимум:",max_finder(array))