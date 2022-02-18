import json
from matplotlib.pyplot import fill
from numpy import diff
from web3 import Web3
from tkinter import *
from time import *
import threading
import abi

root = Tk()
root.title('Bridgeworld Script v0.0.1')

label1 = Label(root, text='Address')
label1.pack()
e1 = Entry(root, width=50, bg='black', fg='white', insertbackground='white')
e1.pack()
e1.focus_set()

label2 = Label(root, text='Private Key')
label2.pack()
e2 = Entry(root, width=50, bg='black', fg='white', insertbackground='white')
e2.pack()

label3 = Label(root, text='Token IDs (separate with space)')
label3.pack()
e3 = Entry(root, width=50, bg='black', fg='white', insertbackground='white')
e3.pack()

label5 = Label(root, text="00:00:00")
label5.pack(side=RIGHT)

arbitrum_mainnet = "https://speedy-nodes-nyc.moralis.io/374ac32c40e6a89aa0abe6c2/arbitrum/mainnet" #WILL THIS WORK WHEN RAN ON SOMEONE ELSE'S PC? (worked for travis)
web3 = Web3(Web3.HTTPProvider(arbitrum_mainnet))
print(web3.isConnected())
treasure_address = Web3.toChecksumAddress('0xda3cad5e4f40062ceca6c1b979766bc0baed8e33') #reveal treasure/restart address
contract_abi = json.loads(abi.treasure_abi)
contract = web3.eth.contract(address=treasure_address, abi=contract_abi)

def execute_transactions(address, private_key, token_ids, difficulties):

    main_address = Web3.toChecksumAddress(address)
    
    #If one is ready to reveal, they all are. If fails, return and try again in next time period
    try:
        contract.functions.isQuestReadyToReveal(token_ids[0]).call()
    except:
        print("Not ready to reveal; returned")
        return
    
    chunks_of_3 = [token_ids[x:x+3] for x in range(0, len(token_ids), 3)]
    for chunk in chunks_of_3:

        # token_quest_tx = contract.functions.revealTokensQuests(chunk).buildTransaction({
        #     'gas': 700000,
        #     'gasPrice': web3.toWei(web3.eth.gasPrice/10**8, 'gwei'),
        #     'from': main_address,
        #     'nonce': web3.eth.get_transaction_count(main_address)
        #     })

        # signed_tx = web3.eth.account.sign_transaction(token_quest_tx, private_key)
        # tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # try:
        #     txn_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=5000)
        # except Exception:
        #     print("Transaction 1 failed: timeout", chunk)
        #     return

        # print("revealTokensQuests() tokenIDs + transaction hash:", chunk, web3.toHex(tx_hash))

        #diffs = [difficulties.pop(0) for i in range(len(chunk))]
        #loops = [contract.functions.tokenIdToNumberLoops(id).call() for id in chunk]
        #MAYBE?? could be calling too fast? test in a for loop later. not a transaction so should be instant
        #could be better to have user just update difficulties in UI between 8 hour time periods

        # restart_token_tx = contract.functions.restartTokenQuests(chunk,diffs,loops).buildTransaction({
        #     'gas': 1200000,
        #     'gasPrice': web3.toWei(web3.eth.gasPrice/10**8, 'gwei'),
        #     'from': main_address,
        #     'nonce': web3.eth.get_transaction_count(main_address)
        #     })
        
        # signed_tx2 = web3.eth.account.sign_transaction(restart_token_tx, private_key)
        # tx_hash2 = web3.eth.send_raw_transaction(signed_tx2.rawTransaction)

        # try:
        #     txn_receipt = web3.eth.wait_for_transaction_receipt(tx_hash2, timeout=5000)
        # except Exception:
        #     print("Transaction 2 failed: timeout", chunk)
        #     return

        # print("restartTokenQuests() tokenIDs + transaction hash:", chunk, web3.toHex(tx_hash2))
        pass

def countDown(token_ids, difficulties):
    global timer
    timer = 29100 #Default 8 Hours, 5 minutes


    hardest = max(difficulties)
    if (hardest == 0): timer = 29100 #8 hours, 5 min
    elif (hardest == 1): timer = 43500 #12 hours, 5 min
    elif (hardest == 2): timer = 57900 #16 hours, 5 min

    for i in range(timer):
        mins, secs = divmod(timer, 60) 
        hours, mins = divmod(mins, 60)
        counter = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(counter)
        label5.configure(text=counter)
        timer -= 1
        sleep(1)

    print("DONE")
    onClick()


def onClick():
    address = e1.get()
    private_key = e2.get()
    token_ids = [int(id) for id in e3.get().split()]
    difficulties = [contract.functions.tokenIdToQuestDifficulty(id).call() for id in token_ids]

    e1.config(state='disabled')
    e2.config(state='disabled')

    button.config(state='disabled')

    # execute_transactions(address, private_key, token_ids, difficulties)

    cd_thread = threading.Thread(target=countDown, args=(token_ids, difficulties, ))
    cd_thread.daemon = True
    cd_thread.start()
    print("WORKING WHILE TIMER WORKING")


button = Button(root, text='REVEAL & RESTART', command=onClick)
button.pack(fill='x')

root.resizable(width=False, height=False)
root.mainloop()

# addy = 0xac938bDfC6fF1223221Be77cdbbB7BCa1e745249
# pk = c9f1b502639a7c8063543aba7a205789ff556fd4582593a1a8f434d7b0d20229
# 13774 10308 15127
# 0 0 0
