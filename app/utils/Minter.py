from web3 import Web3

from app.logs import logging as logger
from app.utils.adresses import nft_addresses, nft_abi
from app.utils.extra import rpcs, scanners


class Minter:

    def __init__(self, private_key, chain, nft_name):
        self.chain = chain
        self.web3 = Web3(Web3.HTTPProvider(rpcs[self.chain]))
        self.private_key = private_key
        self.wallet_address = self.web3.eth.account.from_key(self.private_key).address
        self.nft_name = nft_name
        self.nft_address = nft_addresses[self.nft_name][self.chain]

    async def mint(self):
        try:
            logger.info(f"Адрес кошелька: {self.wallet_address}")

            contract = self.web3.eth.contract(address=Web3.to_checksum_address(self.nft_address), abi=nft_abi)
            tx = await contract.functions.mint().build_transaction(
                {
                    'from': self.wallet_address,
                    'nonce':   self.web3.eth.get_transaction_count(self.wallet_address),
                    'gasPrice':  self.web3.eth.gas_price
                }
            )

            if self.chain == 'core':
                tx['gasPrice'] = Web3.to_wei(30, 'gwei')
            elif self.chain == 'bsc':
                tx['gasPrice'] = Web3.to_wei(1, 'gwei')

            logger.info(f"32")
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            raw_tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_hash = self.web3.to_hex(raw_tx_hash)
            logger.info(f"33")
            tx_receipt = await self.web3.eth.wait_for_transaction_receipt(raw_tx_hash)
            logger.info(f"33")

            if tx_receipt.status == 1:
                logger.info(f"Минт {self.nft_name} произошел успешно.")
                return "✅"
            else:
                return -6

        except Exception as err:
            err_str = str(err)
            if "IntrinsicGas" in err_str or "intrinsic gas" in err_str or "gas required exceeds allowance" in err_str:
                logger.error(f"{self.wallet_address}:{self.chain.upper()} - не хватает газа на минт {self.nft_name}")
                return -2
            elif "max fee per gas less" in err_str:
                logger.error(f"{self.wallet_address}:{self.chain.upper()} - не хватает газа на минт {self.nft_name}")
                return -2
            elif "insufficient funds for gas" in err_str:
                logger.error(f"{self.wallet_address}:{self.chain.upper()} - не хватает газа на минт {self.nft_name}")
                return -2
            elif "claimed already" in err_str:
                logger.error(f"{self.wallet_address}:{self.chain.upper()} - claimed already {self.nft_name}")
                return -5
            else:
                logger.error(f"{self.wallet_address}:{self.chain.upper()} - {err}")
                return -6
