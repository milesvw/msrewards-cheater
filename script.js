import puppeteer from "puppeteer";
import randomWords from "random-words"

// Launch a visible browser window to log in, then save the cookies
async function login() {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();

  await page.goto('https://bing.com');

  const sleep = ms => new Promise(r => setTimeout(r, ms));
  while (true) {
    if (page.url() == 'https://rewards.bing.com/') {
      break;
    }
    await sleep(1000);
  }

  const cookies = await page.cookies();

  await browser.close();

  return cookies;
}

// Save the cookies of the logged in page
const cookies = await login();

// Generate a URL searching Bing with a random word
function url() {
  let url = 'https://bing.com/search?q=' + randomWords();
  return url;
}

// Loads the cookies to log in, then starts racking up points!
async function main() {
  const browser = await puppeteer.launch({headless: true});
  const timer = ms => new Promise(res => setTimeout(res, ms));
  const page = await browser.newPage();

  // Load the cookies into the browser to log in
  await page.setCookie(...cookies);

  // Open search tabs for desktop points
  for (let i = 0; i <= 35; i++) {
    const page = await browser.newPage();

    await page.goto(url());

    await timer(1000);

    await page.close();
  }

  // Open search tabs for mobile points
  for (let i = 0; i <= 25; i++) {
    const page = await browser.newPage();

    // Emulate a phone to get mobile points
    const device = puppeteer.devices['iPhone X'];
    await page.emulate(device);

    await page.setUserAgent('Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.7 Mobile/15E148 Safari/605.1.15');

    await page.goto(url());

    await timer(1000);

    await page.close();
  }

  await browser.close();
}
main();