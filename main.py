from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from playwright.async_api import async_playwright

app = FastAPI()

class ActionRequest(BaseModel):
    username: str
    password: str

async def run_playwright_actions(username, password):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()
        await page.goto("https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help")
        results.append("Navigated to BRRRR backoffice login")
        await page.wait_for_selector('input#userName', timeout=10000)
        email_field = page.locator('input#userName')
        await email_field.click()
        results.append("Clicked username field")
        await email_field.fill(username)
        results.append(f"Filled with {username}")
        pwd_input = page.locator('input#pwd')
        await pwd_input.wait_for(timeout=10000)
        await pwd_input.click()
        results.append("Clicked password field")
        await pwd_input.fill(password)
        results.append(f"Filled with {password}")
        await page.click("button#submitbutton")
        results.append("Clicked login button")
        await browser.close()
    return results

@app.post("/run-actions")
async def run_actions(request: ActionRequest):
    results = await run_playwright_actions(request.username, request.password)
    return {"status": "success", "actions": results} 