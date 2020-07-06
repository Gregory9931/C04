import asyncio
import time
from cssify import cssify

def range_(stop):
    return [i for i in range(stop)]

def print_(word):
    return word

def espere(segs):
	time.sleep(segs)

async def waitPage(page):
    jsWait = "document.readyState === 'complete' || \
              document.readyState === 'iteractive'"
    while not (await page.evaluate(jsWait)):
        await page.waitFor(1)

async def clique(page, xpath):
    await page.waitForXPath(xpath)
    await page.click(cssify(xpath))
    await waitPage(page)

async def selecione(page, xpath, opcao):
    await page.waitForXPath(xpath)
    await page.type(cssify(xpath), opcao)
    await waitPage(page)

async def opcoes(page, xpath, exceto=[]):
    options = []
    await page.waitForXPath(xpath)
    for option in (await page.xpath(xpath + "/option")):
        value = await option.getProperty("text")
        options.append(value.toString().split(":")[-1])
    return [value for value in options if value not in exceto]

async def for_clicavel(page, xpath):
    try:
        await clique(page, xpath)
        return True
    except:
        return False



