def ListSearch(needle, key, haystack):
    for index in range(len(haystack)):
        if haystack[index][key] == needle: return index
    
    return None