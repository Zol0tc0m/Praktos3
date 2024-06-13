from web3 import Web3
from web3.middleware import geth_poa_middleware


W3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
W3.middleware_onion.inject(geth_poa_middleware, layer=0)


address1 = Web3.to_checksum_address('0x522dCF3E6Af20643eEA2104aE6069Ce39ab7a204')
address2 = Web3.to_checksum_address('0x478529b2493fd8Eb448212d70be9fb183EA04170')
address3 = Web3.to_checksum_address('0x4Fbe7dB64b945a15cEF65052746E62Df45fC12c2')
address4 = Web3.to_checksum_address('0x1628c630dd8d30747B1Ee5d33bB3846D9206339f')
address5 = Web3.to_checksum_address('0x6e0bDbeA0e4443178EcA5acd124c72a46737a581')

balance1 = W3.eth.get_balance(address1)
balance2 = W3.eth.get_balance(address2)
balance3 = W3.eth.get_balance(address3)
balance4 = W3.eth.get_balance(address4)
balance5 = W3.eth.get_balance(address5)

print(f"{balance1}\n{balance2}\n{balance3}\n{balance4}\n{balance5}")
