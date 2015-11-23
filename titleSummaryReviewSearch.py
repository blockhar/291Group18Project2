def titleSummaryReviewSearch(word, partial):
    #Uniquely combines results of two other functions
    return searchTitles(word, partial) + list(set(searchFilesSummary(word, partial)) - set(searchTitles(word, partial)))
    
