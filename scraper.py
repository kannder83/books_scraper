import httpx
from selectolax.lexbor import LexborHTMLParser


def get_selector(name: str) -> str:
    selectors = {"next_page": ".next > a", "total_pages": ".current"}
    return selectors.get(name, "")


def fetch_page(session: httpx.Client, url: str) -> str:
    response = session.get(url)
    response.raise_for_status()
    return response.content


def get_next_page_url(content: str, base_url: str) -> str:
    parser = LexborHTMLParser(content)
    page = parser.css_first(get_selector("next_page"))
    if page:
        page_url = f"{base_url}{page.attrs.get('href', '')}"
        if "catalogue" not in page_url:
            page_url = f"{base_url}catalogue/{page.attrs.get('href', '')}"
        return page_url
    return ""


def get_total_pages(content: str) -> int:
    parser = LexborHTMLParser(content)
    page = parser.css_first(get_selector("total_pages"))
    if page:
        text = page.text(strip=True)
        if "of" in text:
            total_pages_str = text.split("of")[-1].strip()
            return int(total_pages_str)
    return None


def generate_page_urls(base_url: str, total_pages: int) -> list[str]:
    return [f"{base_url}catalogue/page-{i + 1}.html" for i in range(total_pages)]


def get_details_page(session: httpx.Client, list_urls: list) -> None:
    for page in list_urls:
        page_status = session.get(page)
        print(f"Page {page} Status code: {page_status.status_code}")


def main():
    print("Hello from books-scraper!")
    list_pages: list[str] = []
    session = httpx.Client()
    url = "http://books.toscrape.com/"
    page_content = fetch_page(session, url)
    total_pages = get_total_pages(page_content)
    if total_pages:
        print(f"Total pages found: {total_pages}")
        list_pages.extend(generate_page_urls(url, total_pages))
        get_details_page(session, list_pages)


if __name__ == "__main__":
    main()
