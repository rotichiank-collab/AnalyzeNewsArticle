import re
from collections import Counter
from typing import Optional


def count_specific_word(text: str, word: str) -> int:
   
    if not text or not word:
        return 0
    
    
    text_lower = text.lower()
    word_lower = word.lower()
    
    
    pattern = r'\b' + re.escape(word_lower) + r'\b'
    matches = re.findall(pattern, text_lower)
    
    return len(matches)


def identify_most_common_word(text: str) -> Optional[str]:
   
    if not text or len(text.strip()) == 0:
        return None
    
    
    words = re.findall(r'\b[a-z]+\b', text.lower())
    
    if not words:
        return None
    
   
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)[0][0]
    
    return most_common


def calculate_average_word_length(text: str) -> float:
   
    if not text or len(text.strip()) == 0:
        return 0.0
    
    
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    if not words:
        return 0.0
    
    
    total_length = sum(len(word) for word in words)
    average = total_length / len(words)
    
    return round(average, 2)


def count_paragraphs(text: str) -> int:
    
    if not text or len(text.strip()) == 0:
        return 1
    
   
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text)]
    paragraphs = [p for p in paragraphs if p]
    
    return len(paragraphs) if paragraphs else 1


def count_sentences(text: str) -> int:
    
    if not text or len(text.strip()) == 0:
        return 1
    
    
    sentence_endings = re.findall(r'[.!?]', text)
    
    return len(sentence_endings) if sentence_endings else 1


def read_article_file(filename: str) -> Optional[str]:
   
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None


def display_article_analysis(text: str, article_name: str = "Article") -> None:
   
    print("\n" + "=" * 70)
    print(f"TEXT ANALYSIS REPORT: {article_name}")
    print("=" * 70 + "\n")
    
   
    print("1. SPECIFIC WORD OCCURRENCES")
    print("-" * 70)
    search_words = ["artificial", "intelligence", "technology", "ai"]
    for word in search_words:
        count = count_specific_word(text, word)
        print(f"   Word '{word}': {count} occurrence(s)")
    
    print()
    
    
    print("2. MOST COMMON WORD")
    print("-" * 70)
    most_common = identify_most_common_word(text)
    if most_common:
        frequency = count_specific_word(text, most_common)
        print(f"   Most common word: '{most_common}'")
        print(f"   Frequency: {frequency} times")
    else:
        print("   No words found in the text.")
    
    print()
    
   
    print("3. AVERAGE WORD LENGTH")
    print("-" * 70)
    avg_length = calculate_average_word_length(text)
    print(f"   Average word length: {avg_length} characters")
    
    print()
    
    
    print("4. PARAGRAPH COUNT")
    print("-" * 70)
    paragraph_count = count_paragraphs(text)
    print(f"   Total paragraphs: {paragraph_count}")
    
    print()
    
    
    print("5. SENTENCE COUNT")
    print("-" * 70)
    sentence_count = count_sentences(text)
    print(f"   Total sentences: {sentence_count}")
    
    print("\n" + "=" * 70 + "\n")


def main():
    
    
    print("\n" + "=" * 70)
    print("WELCOME TO THE NEWS ARTICLE TEXT ANALYSIS TOOL")
    print("=" * 70)
    print("\nThis tool analyzes news articles to extract valuable insights.\n")
    
    
    filename = input("Enter the path to the article file (default: sample_article.txt): ").strip()
    
    if not filename:
        filename = "sample_article.txt"
    
    
    print(f"\nReading article from: {filename}")
    article_text = read_article_file(filename)
    
    if article_text is None:
        print("Failed to read article. Exiting.")
        return
    
   
    display_article_analysis(article_text, filename)
    
    
    print("=" * 70)
    while True:
        analyze_more = input("\nWould you like to analyze another article? (yes/no): ").strip().lower()
        
        if analyze_more in ['yes', 'y']:
            filename = input("Enter the path to the article file: ").strip()
            if filename:
                article_text = read_article_file(filename)
                if article_text:
                    display_article_analysis(article_text, filename)
        elif analyze_more in ['no', 'n']:
            print("\nThank you for using the Text Analysis Tool. Goodbye!\n")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
