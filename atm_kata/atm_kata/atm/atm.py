class ATM:
    def __init__(self):
        self.denominations_available = {
            500: 2,
            200: 3,
            100: 5,
            50: 12,
            20: 20,
            10: 50,
            5: 100,
            2: 250,
            1: 500
        }
        self.denominations_values = sorted(self.denominations_available.keys(), reverse=True)

    def withdraw(self, quantity):
        if quantity <= 0:
            raise ValueError("A quantidade a ser sacada deve ser positiva.")

        total_available_money = sum(value * count for value, count in self.denominations_available.items())
        if quantity > total_available_money:
            raise ValueError("El cajero automático no dispone de dinero suficiente, por favor acuda al cajero automático más cercano")

        temp_denominations = self.denominations_available.copy()
        result = []
        remaining_quantity = quantity

        for denom in self.denominations_values:
            if remaining_quantity >= denom and temp_denominations[denom] > 0:
                count_needed = remaining_quantity // denom
                count_to_take = min(count_needed, temp_denominations[denom])

                if count_to_take > 0:
                    remaining_quantity -= count_to_take * denom
                    temp_denominations[denom] -= count_to_take

                    note_type = "billete" if denom >= 5 else "moneda"
                    if count_to_take == 1:
                        result.append(f"1 {note_type} de {denom}")
                    else:
                        result.append(f"{count_to_take} {note_type}s de {denom}")
        
        if remaining_quantity > 0:
         raise ValueError("El cajero automático no dispone de billetes/monedas suficientes para esta cantidad, por favor intente otra cantidad.")
        
        self.denominations_available = temp_denominations
        return result


