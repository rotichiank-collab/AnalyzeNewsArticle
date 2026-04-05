# News Article Text Analysis Tool

## Overview

A comprehensive Python script for analyzing news articles and extracting valuable insights through text analysis tasks.

## Files Included

### 1. **pythonAssessment.py** (Main Script)

The primary Python module containing all text analysis functions and the interactive CLI interface.

### 2. **sample_article.txt**

A sample news article about Artificial Intelligence used for demonstration and testing.

## Implemented Functions

### `count_specific_word(text: str, word: str) -> int`

Counts the number of occurrences of a specific word in the text.

- **Parameters:** Text to search and word to count
- **Returns:** Integer count (case-insensitive, whole-word matching)
- **Edge Case:** Returns 0 if no matches found

### `identify_most_common_word(text: str) -> Optional[str]`

Identifies the most frequently occurring word in the text.

- **Parameters:** Text to analyze
- **Returns:** String (most common word) or None
- **Edge Case:** Returns None if text is empty

### `calculate_average_word_length(text: str) -> float`

Calculates the average length of words, excluding punctuation.

- **Parameters:** Text to analyze
- **Returns:** Float rounded to 2 decimal places
- **Edge Case:** Returns 0.0 if text is empty

### `count_paragraphs(text: str) -> int`

Counts the number of paragraphs in the text (separated by empty lines).

- **Parameters:** Text to analyze
- **Returns:** Integer paragraph count
- **Edge Case:** Returns 1 if text is empty

### `count_sentences(text: str) -> int`

Counts the number of sentences based on punctuation marks (. ! ?).

- **Parameters:** Text to analyze
- **Returns:** Integer sentence count
- **Edge Case:** Returns 1 if text is empty

### `read_article_file(filename: str) -> Optional[str]`

Reads the contents of a file with proper error handling.

- **Parameters:** Path to article file
- **Returns:** File contents or None if error occurs

### `display_article_analysis(text: str, article_name: str) -> None`

Performs all analysis tasks and displays formatted results.

## Usage

### Basic Usage

```bash
python pythonAssessment.py
```

When prompted, enter the path to your article file (default: `sample_article.txt`)

### Programmatic Usage

```python
from pythonAssessment import count_specific_word, identify_most_common_word
from pythonAssessment import calculate_average_word_length, count_paragraphs, count_sentences

text = "Your article text here..."

# Count specific word
count = count_specific_word(text, "technology")

# Find most common word
common = identify_most_common_word(text)

# Get average word length
avg_length = calculate_average_word_length(text)

# Count paragraphs and sentences
paras = count_paragraphs(text)
sents = count_sentences(text)
```

## Sample Output

```
======================================================================
TEXT ANALYSIS REPORT: sample_article.txt
======================================================================

1. SPECIFIC WORD OCCURRENCES
----------------------------------------------------------------------
   Word 'artificial': 3 occurrence(s)
   Word 'intelligence': 3 occurrence(s)
   Word 'technology': 2 occurrence(s)
   Word 'ai': 5 occurrence(s)

2. MOST COMMON WORD
----------------------------------------------------------------------
   Most common word: 'the'
   Frequency: 7 times

3. AVERAGE WORD LENGTH
----------------------------------------------------------------------
   Average word length: 6.51 characters

4. PARAGRAPH COUNT
----------------------------------------------------------------------
   Total paragraphs: 5

5. SENTENCE COUNT
----------------------------------------------------------------------
   Total sentences: 16
```

## Design Features

### Text Analysis Accuracy

- Case-insensitive word matching with whole-word boundaries
- Proper punctuation handling and exclusion
- Regex patterns for robust text processing

### Efficiency & Readability

- Modular function design for single responsibility
- Clear variable names and comprehensive docstrings
- Efficient algorithms using Python's built-in libraries (re, Counter)

### Functions & Variables

- Proper type hints (Optional, float, int, str)
- Descriptive function names following Python conventions
- Well-named variables that clearly indicate their purpose

### Accuracy

- Precise word counting with whole-word matching
- Accurate paragraph detection using empty line separation
- Reliable sentence counting with proper punctuation detection

### Best Practices

- Follows PEP 8 style guide
- Comprehensive error handling
- Docstrings for all functions
- Type hints for clarity
- Main function pattern with `if __name__ == "__main__"`

### User Experience

- Interactive CLI with clear prompts
- Formatted output for easy reading
- File error handling with user-friendly messages
- Option to analyze multiple articles

## Testing Recommendations

1. Test with the provided `sample_article.txt`
2. Test with empty files
3. Test with files containing special characters
4. Test with very large articles
5. Test with articles in different formats

## Dependencies

- Python 3.6+ (uses f-strings and type hints)
- No external dependencies required (uses only standard library)

## Future Enhancements

- Add sentiment analysis
- Include keyword extraction
- Support for multiple languages
- Generate visualization reports
- Export results to CSV/JSON
