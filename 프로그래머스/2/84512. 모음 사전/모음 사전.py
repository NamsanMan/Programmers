def solution(word):
    dictionary = []
    alphabet_sequence = 'AEIOU'
    def dfs(current_word):
        if current_word != '':
            dictionary.append(current_word)
        if len(current_word) == 5:
            return
        
        for alphabet in alphabet_sequence:
            dfs(current_word + alphabet)
    
    dfs('')
    return dictionary.index(word) + 1