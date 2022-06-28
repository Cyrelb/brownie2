from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainet-fork", "mainet-fork-dev"]
DECIMALS = 8
STARTING_PRICE = 200000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development"]


def get_account():
    if network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        account = accounts.load("cyril")
        return account


def deploy_mock():
    if len(MockV3Aggregator) <= 0:
        print("Deploying Mocks...")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks deployed...")
