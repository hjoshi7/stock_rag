from bs4 import BeautifulSoup
import requests
from typing import List, Dict
from datetime import datetime

class ArticlePreprocessor:
    def clean_text(self, text: str) -> str:
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text(separator=' ', strip=True)

    def chunk_article(self, article: str, chunk_size: int) -> List[str]:
        words = article.split()
        return [' '.join(words[i:i+chunk_size]) 
                for i in range(0, len(words), chunk_size)]

    def format_metadata(self, article_data: Dict) -> Dict:
        return {
            'title': article_data.get('title', ''),
            'source': article_data.get('source', ''),
            'date': datetime.now().isoformat(),
            'category': article_data.get('category', 'general')
        }
