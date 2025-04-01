from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from project_example.client import Client

class Transactions:

    def __init__(self, client: Client):
        self.client = client

    def approve(self):
        return f'{self.client.private_key} далею approve'

    def sing_transaction(self):
        return f'{self.client.private_key} подписываю транзакцию'
