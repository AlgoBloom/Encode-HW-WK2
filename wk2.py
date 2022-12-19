# Previously funded account is used to fund new account
# My address: BSTDOSCCPYN3AZNRGBX3VO4XBEAH2TKCGKYZPMYIIRNYAFHJZGNASJMOEI
# My private key: cYGCLpViChb078xonSF43x/IUQvdFlI0jPeD30DZCwIMpjdIQn4bsGWxMG+6u5cJAH1NQjKxl7MIRFuAFOnJmg==
# My passphrase: comfort anxiety nuclear citizen below airport leisure smooth public major rose worth mother stamp tribe bitter medal cotton wink wealth like wagon aware abandon witness

from algosdk import account, mnemonic
from algosdk.v2client import algod

# creates an account and prints info
def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

def first_transaction_example(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)
