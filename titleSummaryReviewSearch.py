def titleSummaryReviewSearch(word, partial):
    Uniquely combines results of two other funcitions
    return searchTitles(word, partial) + list(set(searchReviewSummary(word, partial)) - set(searchTitles(word, partial)))
    
