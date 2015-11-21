def titleSummaryReviewSearch(word, partial):
    Uniquely combines results of two other funcitions
    return searchTitles(word, partial) + (searchReviewSummary(word, partial) - searchTitles(word, partial))
    
