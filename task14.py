def is_palindrome(word1, word2):
  if len(word1) != len(word2):
    return False

  if word1[:] == word2[::-1]:
    print('This word is palindrome')
  else:
    print('This word is not palindrome')

is_palindrome('raki', 'ikar')
is_palindrome('ogar', 'raki')