"""
News Article Text Analysis Script
==================================
A Python program designed to perform various text analysis tasks on news articles.
This script extracts valuable insights from article content including word frequency,
average word length, paragraph count, and sentence count.

Author: Tech Professional
Date: 2026
"""

import re
from collections import Counter
from typing import Optional


def count_specific_word(text: str, word: str) -> int:
    """
    Count the number of occurrences of a specific word in the text.
    
    Args:
        text (str): The text to search through
        word (str): The word to count
    
    Returns:
        int: Number of occurrences of the word (case-insensitive)
    
    Edge Cases:
        - Returns 0 if no matches are found
        - Case-insensitive matching
        - Whole word matching only (not partial matches)
    """
    if not text or not word:
        return 0
    
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    word_lower = word.lower()
    
    # Use regex to match whole words only (word boundaries)
    pattern = r'\b' + re.escape(word_lower) + r'\b'
    matches = re.findall(pattern, text_lower)
    
    return len(matches)


def identify_most_common_word(text: str) -> Optional[str]:
    """
    Identify the most common word in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        str: The most common word, or None if the text is empty
    
    Edge Cases:
        - Returns None if the text is empty
        - Case-insensitive comparison
        - Excludes punctuation from word identification
    """
    if not text or len(text.strip()) == 0:
        return None
    
    # Extract words, removing punctuation and converting to lowercase
    words = re.findall(r'\b[a-z]+\b', text.lower())
    
    if not words:
        return None
    
    # Count word frequency and find the most common
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)[0][0]
    
    return most_common


def calculate_average_word_length(text: str) -> float:
    """
    Calculate the average length of words in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        float: The average word length (excluding punctuation)
    
    Edge Cases:
        - Returns 0 if the text is empty
        - Excludes punctuation marks and special characters
        - Rounds to 2 decimal places
    """
    if not text or len(text.strip()) == 0:
        return 0.0
    
    # Extract words, removing punctuation
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    if not words:
        return 0.0
    
    # Calculate average length
    total_length = sum(len(word) for word in words)
    average = total_length / len(words)
    
    return round(average, 2)


def count_paragraphs(text: str) -> int:
    """
    Count the number of paragraphs in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        int: Number of paragraphs (separated by empty lines)
    
    Edge Cases:
        - Returns 1 if the text is empty
        - Paragraphs are defined by empty lines (blank lines) between text blocks
    """
    if not text or len(text.strip()) == 0:
        return 1
    
    # Split by empty lines to identify paragraphs
    # Filter out empty strings from the split
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text)]
    paragraphs = [p for p in paragraphs if p]
    
    return len(paragraphs) if paragraphs else 1


def count_sentences(text: str) -> int:
    """
    Count the number of sentences in the text.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        int: Number of sentences
    
    Edge Cases:
        - Returns 1 if the text is empty
        - Sentences are defined by periods (.), exclamation marks (!), and question marks (?)
    """
    if not text or len(text.strip()) == 0:
        return 1
    
    # Count sentence-ending punctuation marks
    sentence_endings = re.findall(r'[.!?]', text)
    
    return len(sentence_endings) if sentence_endings else 1


def read_article_file(filename: str) -> Optional[str]:
    """
    Read the contents of a news article file.
    
    Args:
        filename (str): The path to the article file
    
    Returns:
        str: The contents of the file, or None if file cannot be read
    """
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
    """
    Perform and display all text analysis tasks on the given text.
    
    Args:
        text (str): The article text to analyze
        article_name (str): Name of the article for display purposes
    """
    print("\n" + "=" * 70)
    print(f"TEXT ANALYSIS REPORT: {article_name}")
    print("=" * 70 + "\n")
    
    # Specific word count (example with "AI" and "technology")
    print("1. SPECIFIC WORD OCCURRENCES")
    print("-" * 70)
    search_words = ["artificial", "intelligence", "technology", "ai"]
    for word in search_words:
        count = count_specific_word(text, word)
        print(f"   Word '{word}': {count} occurrence(s)")
    
    print()
    
    # Most common word
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
    
    # Average word length
    print("3. AVERAGE WORD LENGTH")
    print("-" * 70)
    avg_length = calculate_average_word_length(text)
    print(f"   Average word length: {avg_length} characters")
    
    print()
    
    # Paragraph count
    print("4. PARAGRAPH COUNT")
    print("-" * 70)
    paragraph_count = count_paragraphs(text)
    print(f"   Total paragraphs: {paragraph_count}")
    
    print()
    
    # Sentence count
    print("5. SENTENCE COUNT")
    print("-" * 70)
    sentence_count = count_sentences(text)
    print(f"   Total sentences: {sentence_count}")
    
    print("\n" + "=" * 70 + "\n")


def main():
    """Main function to orchestrate the text analysis workflow."""
    
    print("\n" + "=" * 70)
    print("WELCOME TO THE NEWS ARTICLE TEXT ANALYSIS TOOL")
    print("=" * 70)
    print("\nThis tool analyzes news articles to extract valuable insights.\n")
    
    # Get filename from user
    filename = input("Enter the path to the article file (default: sample_article.txt): ").strip()
    
    if not filename:
        filename = "sample_article.txt"
    
    # Read the article
    print(f"\nReading article from: {filename}")
    article_text = read_article_file(filename)
    
    if article_text is None:
        print("Failed to read article. Exiting.")
        return
    
    # Display analysis
    display_article_analysis(article_text, filename)
    
    # Optional: Allow user to analyze custom text
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
