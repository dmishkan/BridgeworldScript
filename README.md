# How It Works
In order to collect your rewards hands-free, the script goes through 2 transactions (BridgeWorld's Revealing + Restarting functions) every X hours based on what level the Recruit is.
If the Recruit is
* Level 0: loops every 8 hours
* Level 1: loops every 12 hours
* Level 2: loops every 16 hours

## How to Use
Upon opening the exe, the GUI should look like this:

![bridge1](https://user-images.githubusercontent.com/39421814/176822867-da61c3de-1396-44eb-8e33-c504d210ec05.png)

* Your hot wallet address should be input into the first slot. 
* The second slot should be your private key (can be found in MetaMask: Three Dots -> Account Details -> Export Private Key).
The private key is a necessary component to tell the transaction that you are giving it full access to process. Otherwise, it would ask for permission and the process would not be
automatic/hands-free.
* The third slot should be the tokenIDs (separated by a space) of the Recruits that you want it to automatically collect

## Example
This is what inputting a Level 0 Recruit example would look like (address and private key censored for privacy reasons):

![bridge4](https://user-images.githubusercontent.com/39421814/176823830-1647eb70-7c45-46b0-bb82-8858fa179e9c.png)

You can find your Recruit tokenID by going to the website as shown here:

![bridge5](https://user-images.githubusercontent.com/39421814/176824142-8ef174b3-3ffb-4f0a-9760-143ed0610065.jpg)

## Transaction
Once clicking "REVEAL & RESTART", visit https://arbiscan.io/address/<YOUR_ADDRESS_HERE> to see if your transactions went through. This process should repeat every x hours (check GUI for exact time). Here are the transactions from the above example:

![bridge3](https://user-images.githubusercontent.com/39421814/176824520-e5f7a4e2-4c23-4b94-9380-7e043831839c.png)

## Enjoy!
Now you can go about your day knowing you've saved time and money without worrying about having to manually collect every couple of hours. 
You can check on the NFTs you've received by going to https://trove.treasure.lol/user/<YOUR_ADDRESS_HERE> . This is what it should look like:

![treasure](https://user-images.githubusercontent.com/39421814/176825406-1e108331-e8a8-4934-bdeb-6a1d80ccd627.png)


