import asyncio
from playwright.async_api import async_playwright
from flask import Response

import os
os.environ["PYPPETEER_CHROMIUM_REVISION"] = "1050513"
from pyppeteer.launcher import DEFAULT_ARGS
from pyppeteer.util import download_chromium, chromium_executable, check_chromium


if not check_chromium():
    print(f"Baixando o navegador na versão: {os.environ.get('PYPPETEER_CHROMIUM_REVISION', 'vazio')}")
    download_chromium()


args= [
   '--allow-running-insecure-content',
      '--autoplay-policy=user-gesture-required', 
      '--disable-component-update', 
      '--disable-domain-reliability',
      '--disable-features=AudioServiceOutOfProcess,IsolateOrigins,site-per-process',
      '--disable-print-preview',
      '--disable-setuid-sandbox',
      '--disable-site-isolation-trials',
      '--disable-speech-api',
      '--disable-web-security',
      '--disk-cache-size=33554432',
      '--enable-features=SharedArrayBuffer',
      '--hide-scrollbars',
      '--ignore-gpu-blocklist',
      '--in-process-gpu',
      '--mute-audio',
      '--no-default-browser-check',
      '--no-pings',
      '--no-sandbox',
      '--no-zygote',
      '--use-gl=swiftshader',
      '--window-size=1920,1080',
]

async def run(playwright):
    path_exc = chromium_executable()
    print(path_exc)

    chromium = playwright.chromium
    browser = await chromium.launch(
        executable_path=path_exc,
        args=DEFAULT_ARGS,
        chromium_sandbox=False,
        handle_sigint=False,
        handle_sigterm=False,
        handle_sighup=False
        )
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.google.com")
    image = await page.screenshot()
    await browser.close()
    return image

async def main():
    async with async_playwright() as playwright:
        playwright.chromium
        return await run(playwright)

def print_tela_google(request):
    image = asyncio.run(main())
    return Response(image, mimetype='image/jpeg')

