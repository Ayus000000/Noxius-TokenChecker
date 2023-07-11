# rotomicora#0001
# https://t.me/projectnoxius
import os, fade, time, requests
from colorama import Fore

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
            hiddedToken = token[0:4] + "*******" + token[24:32]
            print(f"{M}[{G}OK{M}] {BLACK}{hiddedToken}")
            with open('output/Working.txt', 'a') as workingTokensFile:
                workingTokensFile.write(token + "\n")

        else:
            print(f"{M}[{W}INVALID{M}] {R}{token}")
            with open('output/NotWorking.txt', 'a') as notWorkingTokensFile:
                notWorkingTokensFile.write(token + "\n")
    except Exception as e:
        print(f"{M}[{W}ERROR{M}] {R}{e}")

def main():
    global useProxys
    clsTerminal()
    printGui()
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


main()