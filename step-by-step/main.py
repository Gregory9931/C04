import json
import sys

sys.path.append('code')
import code_generator as code_g
import atomizer as atom
from functions_file import *
import functions_file

import time
from pyppeteer import launch




# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('http://www.in.gov.br/web/guest/inicio')

#     steps = __import__('diario_oficial_uniao_steps')
#     await steps.execute_steps(page = page)

#     await browser.close()
#     return


with open('tests/recipe_examples.json') as file:
    recipe = json.load(file)

with open('diario_oficial_uniao_steps.py', 'w+') as file:
    print(code_g.generate_code(recipe["all_cases"]['recipe'], functions_file), '\n\n\n\n')
    print(code_g.generate_code(atom.extend(recipe["all_cases"]['recipe'])[0], functions_file), '\n\n\n\n')

#asyncio.get_event_loop().run_until_complete(main())







