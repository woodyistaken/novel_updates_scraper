import nodriver as uc
import asyncio
from constants import BASE_URL

async def get_cf_clearance(url):
    """Extract cf_clearance using Nodriver stealth browser."""
    
    browser = await uc.start()
    page = await browser.get(url)
    
    # Wait for Cloudflare challenge to resolve
    #await asyncio.sleep(1)
    
    ua = await page.evaluate("navigator.userAgent")
    # Check if we passed the challenge
    cookies = await browser.cookies.get_all()
    
    cf_clearance = None
    for cookie in cookies:
        if cookie.name == "cf_clearance":
            cf_clearance = cookie.value
            break
    
    browser.stop()
    
    return cf_clearance,ua

# Run extraction
