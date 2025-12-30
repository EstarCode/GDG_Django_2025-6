def get_expensive_product(prices):
    expensive_prices = []
    for price in prices:
        if price >= 100:
            expensive_prices.append(price)
    return expensive_prices


def main():
    prices = [120, 45, 300, 85, 150]
    result = get_expensive_product(prices)
    print("expensive_prices = ", result)


if __name__ == "__main__":
    main()
