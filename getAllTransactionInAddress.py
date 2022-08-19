from web3 import Web3
import json
from web3.middleware import geth_poa_middleware

bsc_testnet = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
account_address = '0x5A8E6d0642D9E0875A0886903f069622177DE04c'
account_private_key = '5b584e5eeb23b603661569b04509c7bd2394b4fb5ef5011f698dccf33b041777'

web3 = Web3(Web3.HTTPProvider(bsc_testnet))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  #  Inject poa middleware

print("----------------------------------------------------")
#print("Block : ",block)
def transactionChecker(block_number):
    block = web3.eth.getBlock(block_number)
    if (block is not None and block.transactions is not None) :
        for txHash in block.transactions :
            tx = web3.eth.getTransaction(txHash)
            print("*****************************************") 
            print("Transaction from: ",tx["from"])
            print("Transaction to: ",tx["to"])   
            print("Value : ",web3.fromWei(tx["value"],'ether'))      

