from mars_rover import MarsRover

def main():
    rover = MarsRover()
    print("Mars Rover iniciado na posição 0:0:N")
    while True:
        command = input("Digite um comando (L, R, M) ou 'sair' para encerrar: ").strip().upper()
        if command == 'SAIR':
            break
        
        if not all(c in ['L', 'R', 'M'] for c in command):
            print("Comando inválido. Use apenas L, R, M.")
            continue

        final_position = rover.execute(command)
        print(f"Posição final: {final_position}")

if __name__ == "__main__":
    main()


