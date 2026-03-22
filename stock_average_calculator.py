"""Калкулатор за средна цена на акция.

Изчислява претеглена средна цена на база въведени покупки.
"""

from __future__ import annotations


def calculate_average_price(purchases: list[tuple[float, float]]) -> tuple[float, float, float]:
    """Връща (общо_акции, обща_стойност, средна_цена)."""
    if not purchases:
        raise ValueError("Трябва да има поне една покупка.")

    total_shares = 0.0
    total_cost = 0.0

    for shares, price in purchases:
        if shares <= 0:
            raise ValueError("Броят акции трябва да е положително число.")
        if price < 0:
            raise ValueError("Цената не може да е отрицателна.")

        total_shares += shares
        total_cost += shares * price

    average_price = total_cost / total_shares
    return total_shares, total_cost, average_price


def read_float(prompt: str) -> float:
    """Чете число от конзолата с базова валидация."""
    while True:
        value = input(prompt).strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Невалидно число. Опитай отново.")


def main() -> None:
    print("КАЛКУЛАТОР: Средна цена на акция")
    print("Въведи поредица от покупки (брой + цена).")

    count = int(read_float("Колко покупки искаш да въведеш? "))
    if count <= 0:
        print("Броят покупки трябва да е поне 1.")
        return

    purchases: list[tuple[float, float]] = []

    for i in range(1, count + 1):
        print(f"\nПокупка #{i}")
        shares = read_float("  Брой акции: ")
        price = read_float("  Цена за акция: ")
        purchases.append((shares, price))

    total_shares, total_cost, average_price = calculate_average_price(purchases)

    print("\n--- РЕЗУЛТАТ ---")
    print(f"Общо акции: {total_shares:.4f}")
    print(f"Обща стойност: {total_cost:.2f}")
    print(f"Средна цена на акция: {average_price:.4f}")


if __name__ == "__main__":
    main()
