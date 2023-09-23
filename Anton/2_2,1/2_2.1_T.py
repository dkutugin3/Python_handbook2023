def solution():
    overall_weight = int(input())
    overall_price = int(input())
    price_1 = int(input())
    price_2 = int(input())

    weight_1 = ((overall_price * overall_weight) / price_1 - (price_2 * overall_weight) / price_1) / (
                1 - price_2 / price_1)
    weight_2 = overall_weight - weight_1

    print(round(weight_1), round(weight_2))


def main():
    solution()


if __name__ == "__main__":
    main()
