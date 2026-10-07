# buggy_script.py

def calculate_total_price(base_price: float, tax_rate: float, discount: float) -> float:
    # Tax calculate kar ke total price banana
    tax_amount = base_price * tax_rate
    subtotal = base_price + tax_amount
    final_price = subtotal - discount
    return final_price

def load_cart_data() -> dict:
    # Simulating data coming from an external API payload or database
    cart = {
        "item_name": "Developer Laptop",
        "base_price": "1200.0",  # <--- Yahan ek chota sa chhupta hua bomb hai!
        "tax_rate": 0.05,
        "discount": 50.0
    }
    return cart

def main() -> None:
    data = load_cart_data()
    total = calculate_total_price(float(data["base_price"]), data["tax_rate"], data["discount"])
    print(f"Final price: {total}")

if __name__ == "__main__":
    main()