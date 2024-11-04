def calculate_rectangle_area(base: int, height: int) -> int:
    return base * height

def run():
    try:
        print("Bienvenido al programa de calculo de area de rectangulo. Por favor indique:")
        input_base = int(input("Base del rectangulo: "))
        input_height = int(input("Altura del rectangulo: "))

        if input_base <= 0 or input_height <= 0:
            print("Ha ingresado un valor igual o menor a 0 como base o altura. Intente nuevamente")
            run()
        result = calculate_rectangle_area(input_base, input_height)
        print(f"El area del rectangulo de base {input_base} y altura {input_height} es {result}")
    except ValueError:
        print("Entrada invalida, porfavor, solo ingrese numeros enteros positivos.")
        run()


if __name__ == "__main__":
    run()
