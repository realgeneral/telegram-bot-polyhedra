import httpx


from web3 import Web3

from app.utils.extra import rpcs
from app.logs import logging as logger


class Balance:
    def __init__(self, private_key, chain, ids):
        self.chain = chain
        self.private_key = private_key
        self.wallet_address = ""
        self.web3 = Web3(Web3.HTTPProvider(rpcs[self.chain]))
        self.ids = ids

    async def get_balance(self, url):

        try:
            self.wallet_address = self.web3.eth.account.from_key(self.private_key).address
            wallet_balance_wei = self.web3.eth.get_balance(Web3.to_checksum_address(self.wallet_address))
            wallet_balance_no_sum_wei = self.web3.eth.get_balance(self.wallet_address)
            wallet_balance = Web3.from_wei(wallet_balance_wei, 'ether')
            wallet_balance_no_sum = Web3.from_wei(wallet_balance_no_sum_wei, 'ether')


            if url == '':
                return [round(float(wallet_balance), 3), ""]

            # response = requests.get(url)

            async with httpx.AsyncClient() as client:
                response = await client.get(url)

            if response.status_code == 200:
                data = response.json()
                if self.ids in data:
                    to_usd = data[self.ids]['usd']
                    usd_amount = wallet_balance.__float__() * to_usd
                    return [round(float(wallet_balance), 3), round(usd_amount, 2)]
                else:
                    logger.error(f"{response.url} --- NO {self.ids} or USD")
                    return -6
            else:
                logger.error(f"{response.url} --- CODE: {response.status_code}")
                return -6

        except Exception as err:
            logger.error(f"{self.wallet_address}:{self.chain.upper()} - {err}")
            return -6
