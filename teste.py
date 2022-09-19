import re
print( re.fullmatch(r'^\s*\((\s*(("|\')([^\3]+|\\\3)\3|[\x7f-\xff][a-zA-Z0-9_\x7f-\xff])\s*,?)*\s*\)', '("Lets do it!", \'Perl lexer is ready?\')') )