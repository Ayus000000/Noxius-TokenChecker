# rotomicora#0001
# https://t.me/projectnoxius

import os, fade, time, requests, random, string; from colorama import Fore

W = Fore.LIGHTWHITE_EX; R = Fore.RED; G = Fore.LIGHTGREEN_EX; B = Fore.BLUE; M = Fore.LIGHTMAGENTA_EX; C = Fore.LIGHTCYAN_EX; Y = Fore.LIGHTYELLOW_EX; BLACK = Fore.LIGHTBLACK_EX; RESET = Fore.RESET

GUI = """
          ╔══════════════════════════════════════════════════════╗
          ║             [>] t.me/projectnoxius [<]               ║
          ╠══════════════════════════════════════════════════════╣
          ║          ╔╗╔ ╔═╗ ═╗╔═ ╦ ╦ ╦ ╔═╗                      ║
          ║          ║║║ ║ ║ ╔╩╚╗ ║ ║ ║ ╚═╗  @rotomicora#0001    ║
          ║          ╝╚╝ ╚═╝ ╩  ╩ ╩ ╚═╝ ╚═╝       v2.0           ║
          ║    ╔════════════════════════════════════════════╗    ║
          ║ ╔══╝       [!] NOXIUS TOKEN CHECKER [!]         ╚══╗ ║
          ╠═╝            [-] Telegram: @tcp_nx [-]             ╚═╣
          ╚══════════════════════════════════════════════════════╝
"""

VALID_TOKENS = 0
NO_VALID_TOKENS = 0

FADED_GUI = fade.pinkred(GUI)

def clsTerminal():
    os.system("cls")

with open('Tokens.txt') as tokensFile:
    allTokens = tokensFile.read().splitlines()


def printGui():
    print(FADED_GUI)

os.system("title Noxius Token Checker ^| @tcp_nx")

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

def checkToken(token):
    global workingTokensFile, notWorkingTokensFile
    try:
        tokenHeaders = {"authorization": token}
        if useProxys == True:
            getProxy()
            tokenRequest = requests.get("https://discordapp.com/api/v6/users/@me", headers=tokenHeaders, proxies=allProxys)
        else:
            tokenRequest = requests.get("https://discordapp.com/api/v6/users/@me", headers=tokenHeaders)
        if tokenRequest.status_code == 200:
            tokenRequest = tokenRequest.json()
            tokenUsername = tokenRequest["username"] + "#" + tokenRequest["discriminator"]
            tokenNitro = requests.get("https://discordapp.com/api/v6/users/@me/billing/payments", headers=tokenHeaders)
            if tokenNitro.status_code == 200:
                tokenNitro = True
            else:
                tokenNitro = False
            tokenBilling = requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=tokenHeaders)
            if tokenBilling.status_code == 200:
                tokenBilling = True
            else:
                tokenBilling = False
            tokenLocked = requests.get("https://discordapp.com/api/v6/users/@me/settings", headers=tokenHeaders)
            if tokenLocked.status_code == 200:
                tokenLocked = False
            else:
                tokenLocked = True
            hiddedToken = token[0:4] + "*******" + token[24:32]
            print(f"{M}[{G}VALID{M}] {Y}{hiddedToken} {M}| {BLACK}USERNAME: {Y}{tokenUsername} {M}| {BLACK}NITRO: {Y}{tokenNitro} {M}| {BLACK}BILLING: {Y}{tokenBilling} {M}| {BLACK}LOCKED: {Y}{tokenLocked}")
            with open('output/Working.txt', 'a') as workingTokensFile:
                workingTokensFile.write(token + "\n")
                global VALID_TOKENS
                VALID_TOKENS += 1
            if tokenNitro == True:
                with open('output/Nitro.txt', 'a') as nitroTokensFile:
                    nitroTokensFile.write(token + "\n")
            if tokenBilling == True:
                with open('output/Billing.txt', 'a') as billingTokensFile:
                    billingTokensFile.write(token + "\n")
            if tokenLocked == True:
                with open('output/Locked.txt', 'a') as lockedTokensFile:
                    lockedTokensFile.write(token + "\n")
        else:
            print(f"{M}[{W}INVALID{M}] {R}{token}")
            with open('output/NotWorking.txt', 'a') as notWorkingTokensFile:
                notWorkingTokensFile.write(token + "\n")
                global NO_VALID_TOKENS
                NO_VALID_TOKENS += 1
        os.system(f"title Noxius Token Checker ^| Valid Tokens: {VALID_TOKENS} ^| Invalid Tokens: {NO_VALID_TOKENS} ^| Checked Tokens: {VALID_TOKENS + NO_VALID_TOKENS}/{len(allTokens)}")
    except Exception as e:
        print(f"{M}[{W}ERROR{M}] {R}{e}")

def main():
    global useProxys
    clsTerminal()
    printGui()
    cleanFiles()
    print(f"{M}[{G}+{M}] {BLACK}Checking {len(allTokens)} tokens")
    proxysEnable = input(f"{M}[{Y}>>>{M}] {BLACK}Enable proxys (y/n) -{M}> {Y}")
    if proxysEnable.lower() == "y":
        useProxys = True
    else:
        useProxys = False
    for token in allTokens:
        checkToken(token)
        time.sleep(1)
    with open('output/Working.txt') as workingTokensFile:
        workingTokensFile = workingTokensFile.read().splitlines()
    with open('output/NotWorking.txt') as notWorkingTokensFile:
        notWorkingTokensFile = notWorkingTokensFile.read().splitlines()
    print(f"{M}[{Y}>{M}] {BLACK}Tokens checked -{M}> {Y}{len(allTokens)} {M}| {BLACK}Valid -{M}> {Y}{len(workingTokensFile)} {M}| {BLACK}Invalid -{M}> {Y}{len(notWorkingTokensFile)}")
    os.system("pause >nul")


main()
