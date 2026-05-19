import math

def triangle_area():
    print("\n--- 1. Площа трикутника за трьома сторонами ---")
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("❌ Трикутник з такими сторонами неможливий!")
        return

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Площа трикутника = {area:.4f}")


def quadratic_equation():
    print("\n--- 2. Розв'язання квадратного рівняння ax² + bx + c = 0 ---")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a == 0:
        print("Це не квадратне рівняння!")
        return

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Два корені: x1 = {x1:.4f}, x2 = {x2:.4f}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Один корінь: x = {x:.4f}")
    else:
        print("Коренів немає (дискримінант від'ємний)")


def equilateral_triangle_side():
    print("\n--- 3. Сторона рівностороннього трикутника вписаного в коло ---")
    R = float(input("Радіус кола R = "))
    side = R * math.sqrt(3)
    print(f"Довжина сторони = {side:.4f}")


def polygon_area():
    print("\n--- 4. Площа многоугольника за координатами (формула шнурівки) ---")
    n = int(input("Кількість вершин: "))
    vertices = []
    print("Вводьте координати (x y) для кожної вершини:")
    for i in range(n):
        x, y = map(float, input(f"Вершина {i + 1}: ").split())
        vertices.append((x, y))

    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    print(f"Площа многоугольника = {abs(area) / 2:.4f}")


def matrix_multiply():
    print("\n--- 5. Множення двох матриць 2x2 ---")
    print("Введіть елементи першої матриці A:")
    a11 = float(input("a11 = "))
    a12 = float(input("a12 = "))
    a21 = float(input("a21 = "))
    a22 = float(input("a22 = "))

    print("Введіть елементи другої матриці B:")
    b11 = float(input("b11 = "))
    b12 = float(input("b12 = "))
    b21 = float(input("b21 = "))
    b22 = float(input("b22 = "))

    # Множення матриць
    c11 = a11 * b11 + a12 * b21
    c12 = a11 * b12 + a12 * b22
    c21 = a21 * b11 + a22 * b21
    c22 = a21 * b12 + a22 * b22

    print("\nРезультат (матриця C = A × B):")
    print(f"[ {c11:6.2f}  {c12:6.2f} ]")
    print(f"[ {c21:6.2f}  {c22:6.2f} ]")


# ====================== МЕНЮ ======================
def main():
    while True:
        print("\n" + "=" * 50)
        print("Оберіть задачу:")
        print("1. Площа трикутника за трьома сторонами")
        print("2. Розв'язання квадратного рівняння")
        print("3. Сторона рівностороннього трикутника в колі")
        print("4. Площа многоугольника за координатами")
        print("5. Множення матриць 2×2")
        print("0. Вихід")
        print("=" * 50)

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            triangle_area()
        elif choice == "2":
            quadratic_equation()
        elif choice == "3":
            equilateral_triangle_side()
        elif choice == "4":
            polygon_area()
        elif choice == "5":
            matrix_multiply()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()