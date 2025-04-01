from project_example.client import Client


def main():
    client = Client(private_key='111', rpc='arbitrum')

    print(client.private_key)
    print(client.wallet.get_balance())
    print(client.transaction.sing_transaction())


if __name__ == "__main__":
    main()
