import os, time, requests, colorama, random, json ,concurrent.futures, fade, threading ;from colorama import Fore
W = Fore.LIGHTWHITE_EX
R = Fore.RED
G = Fore.LIGHTGREEN_EX
B = Fore.BLUE
M = Fore.LIGHTMAGENTA_EX
C = Fore.LIGHTCYAN_EX
Y = Fore.LIGHTYELLOW_EX
BLACK = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

GUI = """
          ╔══════════════════════════════════════════════════════╗
          ║             [>] t.me/projectnoxius [<]               ║
          ╠══════════════════════════════════════════════════════╣
          ║          ╔╗╔ ╔═╗ ═╗╔═ ╦ ╦ ╦ ╔═╗                      ║
          ║          ║║║ ║ ║ ╔╩╚╗ ║ ║ ║ ╚═╗  @rotomicora#0001    ║
          ║          ╝╚╝ ╚═╝ ╩  ╩ ╩ ╚═╝ ╚═╝                      ║
          ║    ╔════════════════════════════════════════════╗    ║
          ║ ╔══╝       [!] NOXIUS TOKEN CHECKER [!]         ╚══╗ ║
          ╠═╝            [-] Telegram: @tcp_nx [-]             ╚═╣
          ╚══════════════════════════════════════════════════════╝
"""

FADED_GUI = fade.pinkred(GUI)

VALID_TOKENS = 0
NO_VALID_TOKENS = 0
LOCKED_TOCKENS = 0
NITRO_TOKENS = 0
BILLING_TOKENS = 0
NO_LOCKED_TOKENS = 0
CPM = 0

def clsTerminal():
    os.system("cls")

with open('Tokens.txt') as tokensFile:
    allTokens = tokensFile.read().splitlines()

def printGui():
    print(FADED_GUI)

os.system("title Noxius Token Checker ^| @tcp_nx")

def getChecksPerMinut():
    global CPM
    while True:
        CPM = VALID_TOKENS + NO_VALID_TOKENS
        time.sleep(60)
        CPM = 0

def getProxy():
    global allProxys
    with open('proxys.txt') as proxyFile:
        allProxys = proxyFile.read().splitlines()
    proxy = random.choice(allProxys)
    proxy = proxy.split(":")
    proxy = proxy[0] + ":" + proxy[1]
    allProxys = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

def cleanFiles():
    with open('output/Working.txt', 'w') as workingTokensFile:
        workingTokensFile.write("")
    with open('output/NotWorking.txt', 'w') as notWorkingTokensFile:
        notWorkingTokensFile.write("")
    with open('output/Nitro.txt', 'w') as nitroTokensFile:
        nitroTokensFile.write("")
    with open('output/Billing.txt', 'w') as billingTokensFile:
        billingTokensFile.write("")
    with open('output/Locked.txt', 'w') as lockedTokensFile:
        lockedTokensFile.write("")
    with open('output/NotLocked.txt', 'w') as notLockedTokensFile:
        notLockedTokensFile.write("")

def checkToken(token):
    global VALID_TOKENS, NO_VALID_TOKENS, LOCKED_TOCKENS, NITRO_TOKENS, BILLING_TOKENS, NO_LOCKED_TOKENS
    try:
        tokenHeaders = {"authorization": token}
        if useProxys == True:
            getProxy()
            tokenRequest = requests.get("https://discordapp.com/api/v6/users/@me", headers=tokenHeaders, proxies=allProxys)
            checkJson = tokenRequest.json()
        else:
            tokenRequest = requests.get("https://discordapp.com/api/v6/users/@me", headers=tokenHeaders)
            checkJson = tokenRequest.json()

        if "username" in checkJson and "discriminator" in checkJson:
            tokenUsername = checkJson["username"] + "#" + checkJson["discriminator"]
            tokenLocked = requests.get("https://discordapp.com/api/v6/users/@me/settings", headers=tokenHeaders)
            if tokenLocked.status_code == 200:
                tokenLocked = False
            else:
                tokenLocked = True
            tokenNitro = checkJson["premium_type"]
            if tokenNitro == 0:
                tokenNitro = False
            elif tokenNitro == 2:
                tokenNitro = True
            tokenBilling = requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=tokenHeaders)
            if len(tokenBilling.json()) != 0 and tokenLocked == False:
                tokenBilling = True
            else:
                tokenBilling = False
            tokenLocked = requests.get("https://discordapp.com/api/v6/users/@me/settings", headers=tokenHeaders)
            if tokenLocked.status_code == 200:
                tokenLocked = False
            else:
                tokenLocked = True
            hiddedToken = token[0:4] + "*******" + token[24:32]

            with open('output/Working.txt', 'a') as workingTokensFile:
                workingTokensFile.write(token + "\n")
                VALID_TOKENS += 1
            if tokenNitro == True:
                with open('output/Nitro.txt', 'a') as nitroTokensFile:
                    nitroTokensFile.write(token + "\n")
                    NITRO_TOKENS += 1
            if tokenBilling == True:
                with open('output/Billing.txt', 'a') as billingTokensFile:
                    billingTokensFile.write(token + "\n")
                    BILLING_TOKENS += 1
            if tokenLocked == True:
                with open('output/Locked.txt', 'a') as lockedTokensFile:
                    lockedTokensFile.write(token + "\n")
                    LOCKED_TOCKENS += 1
            if tokenLocked == False:
                with open('output/NotLocked.txt', 'a') as notLockedTokensFile:
                    notLockedTokensFile.write(token + "\n")
                    NO_LOCKED_TOKENS += 1

            print(f"{M}[{G}VALID{M}] {Y}{hiddedToken} {M}| {BLACK}USERNAME: {Y}{tokenUsername} {M}| {BLACK}NITRO: {Y}{tokenNitro} {M}| {BLACK}BILLING: {Y}{tokenBilling} {M}| {BLACK}LOCKED: {Y}{tokenLocked}{RESET}")
        else:
            print(f"{M}[{W}INVALID{M}] {R}{token}{RESET}")
            with open('output/NotWorking.txt', 'a') as notWorkingTokensFile:
                notWorkingTokensFile.write(token + "\n")
                NO_VALID_TOKENS += 1

        os.system(f"title Noxius Token Checker ^| Valid Tokens: {VALID_TOKENS} ^| Invalid Tokens: {NO_VALID_TOKENS} ^| Nitro: {NITRO_TOKENS} ^| Locked: {LOCKED_TOCKENS}/{VALID_TOKENS} ^| Checked Tokens: {VALID_TOKENS + NO_VALID_TOKENS}/{len(allTokens)} ^| CPM: {CPM}")
    except Exception as e:
        print(f"{M}[{W}ERROR{M}] {R}{e}")

def main():
    global useProxys
    clsTerminal()
    printGui()
    cleanFiles()
    proxysEnable = input("Enable proxys (y/n) -> ")
    if proxysEnable.lower() == "y":
        useProxys = True
    else:
        useProxys = False

    num_threads = 40

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(checkToken, allTokens))

    with open('output/Working.txt') as workingTokensFile:
        workingTokensFile = workingTokensFile.read().splitlines()
    with open('output/NotWorking.txt') as notWorkingTokensFile:
        notWorkingTokensFile = notWorkingTokensFile.read().splitlines()

    print(f"{M}[{G}OK{M}] {BLACK}All Tokens Checked {M}>>> {BLACK}VALID: {Y}{len(workingTokensFile)} {M}| {BLACK}INVALID: {Y}{len(notWorkingTokensFile)} {M}| {BLACK}NITRO: {Y}{NITRO_TOKENS} {M}| {BLACK}BILLING: {Y}{BILLING_TOKENS} {M}| {BLACK}LOCKED: {Y}{LOCKED_TOCKENS}/{VALID_TOKENS} {M}| {BLACK}NOT LOCKED: {Y}{NO_LOCKED_TOKENS}{RESET}")
    os.system("pause >nul")



if __name__ == "__main__":
    main()
    threading.Thread(target=getChecksPerMinut).start()
