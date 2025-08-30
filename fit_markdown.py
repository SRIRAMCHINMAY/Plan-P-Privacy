import asyncio
import os
import json
import base64
from pathlib import Path
from typing import List
from crawl4ai import ProxyConfig

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, CrawlResult
from crawl4ai import RoundRobinProxyStrategy
from crawl4ai import JsonCssExtractionStrategy, LLMExtractionStrategy
from crawl4ai import LLMConfig
from crawl4ai import PruningContentFilter, BM25ContentFilter
from crawl4ai import DefaultMarkdownGenerator
from crawl4ai import BFSDeepCrawlStrategy, DomainFilter, FilterChain
from crawl4ai import BrowserConfig

async def fit_markdown():
    async with AsyncWebCrawler() as crawler:
        result: CrawlResult=await crawler.arun(
            url="https://en.wikipedia.org/wiki/Python_(programming_language)",
            config=CrawlerRunConfig(
                markdown_generator=DefaultMarkdownGenerator(
                    content_filter=PruningContentFilter()
                )
            ),
        )
        print(f"Raw: {len(result.markdown.raw_markdown)} chars")
        print(f"Fit: {len(result.markdown.fit_markdown)} chars")
async def main():
    await fit_markdown()
if __name__=="__main__":
    asyncio.run(main())