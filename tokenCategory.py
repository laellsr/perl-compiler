tokenCategory = {
    "COMMENT_LINE" : r'\/\/',
    "COMMENT_BLOCK" : 'COMMENT_BLOCK',
    "POD" : 'POD',
    "SIGIL_ARRAY" : '$@',
    "SIGIL_SCALAR" : '$$',
    "SIGIL_SCALAR_INDEX" : '$#',
    "SIGIL_GLOB" : '$*',
    "SIGIL_HASH" : '$%',
    "SIGIL_CODE" : '$&',
}

# from enum import Enum

# class TokenCategory(Enum):
#     COMMENT_LINE='COMMENT_LINE'
#     COMMENT_BLOCK='COMMENT_BLOCK'
#     POD='POD'

#     SIGIL_ARRAY='$@'
#     SIGIL_SCALAR='$$'
#     SIGIL_SCALAR_INDEX='$#'
#     SIGIL_GLOB='$*'
#     SIGIL_HASH='$%'
#     SIGIL_CODE='$&'

    # LEFT_BRACE_SCALAR='${'
    # LEFT_BRACE_ARRAY='@{'
    # LEFT_BRACE_HASH='%{'
    # LEFT_BRACE_GLOB='*{'
    # LEFT_BRACE_CODE='&{'

    # RIGHT_BRACE_SCALAR='$}'
    # RIGHT_BRACE_ARRAY='@}'
    # RIGHT_BRACE_HASH='%}'
    # RIGHT_BRACE_GLOB='*}'
    # RIGHT_BRACE_CODE='&}'

    # # postfix deref
    # DEREF_SCALAR='->$*'
    # DEREF_SCALAR_INDEX='->$#*'
    # DEREF_ARRAY='->@*'
    # DEREF_HASH='->%*'
    # DEREF_GLOB='->**'
    # DEREF_CODE='->&*'

    # # generated tokens
    # SCALAR_NAME='SCALAR_NAME'
    # ARRAY_NAME='ARRAY_NAME'
    # HASH_NAME='HASH_NAME'
    # GLOB_NAME='GLOB_NAME'

    # HEREDOC_END='HEREDOC_END'
    # HEREDOC_END_INDENTABLE='HEREDOC_END_INDENTABLE'

    # FORMAT='FORMAT'
    # FORMAT_TERMINATOR='.'

    # VERSION_ELEMENT='VERSION_ELEMENT'

    # NUMBER_VERSION='NUMBER_VERSION'
    # NUMBER='NUMBER'
    # NUMBER_HEX = 'NUMBER_HEX'
    # NUMBER_OCT = 'NUMBER_OCT'
    # NUMBER_BIN = 'NUMBER_BIN'

    # STRING_SPECIAL_TAB='\t'
    # STRING_SPECIAL_NEWLINE='\n'
    # STRING_SPECIAL_RETURN='\r'
    # STRING_SPECIAL_FORMFEED='\f'
    # STRING_SPECIAL_BACKSPACE='\b'
    # STRING_SPECIAL_ALARM='\a'
    # STRING_SPECIAL_ESCAPE='\e'
    # STRING_SPECIAL_ESCAPE_CHAR='\\"'

    # STRING_SPECIAL_LCFIRST='\l'
    # STRING_SPECIAL_TCFIRST='\\u'

    # STRING_SPECIAL_SUBST='\c*'
    # STRING_SPECIAL_BACKREF = '\1'

    # STRING_SPECIAL_HEX='\x'

    # STRING_SPECIAL_OCT='\o'
    # STRING_SPECIAL_OCT_AMBIGUOUS='\0'

    # STRING_SPECIAL_UNICODE='\N'
    # STRING_SPECIAL_UNICODE_CODE_PREFIX='U+'

    # STRING_CHAR_NAME='charname'

    # STRING_SPECIAL_LEFT_BRACE='"{'
    # STRING_SPECIAL_RIGHT_BRACE='}"'
    # STRING_SPECIAL_RANGE='"-'

    # STRING_SPECIAL_LOWERCASE_START='\L'
    # STRING_SPECIAL_UPPERCASE_START='\U'
    # STRING_SPECIAL_FOLDCASE_START='\F'
    # STRING_SPECIAL_QUOTE_START='\Q'
    # STRING_SPECIAL_MODIFIER_END='\E'

    # RESERVED_IF='if'
    # RESERVED_UNLESS='unless'
    # RESERVED_ELSIF='elsif'
    # RESERVED_ELSE='else'
    # RESERVED_GIVEN='given'
    # RESERVED_WHILE='while'
    # RESERVED_UNTIL='until'
    # RESERVED_FOR='for'
    # RESERVED_FOREACH='foreach'

    # RESERVED_CONTINUE='continue'
    # RESERVED_WHEN='when'
    # RESERVED_DEFAULT='default'

    # RESERVED_FORMAT='format'
    # RESERVED_SUB='sub'
    # RESERVED_ASYNC='async'
    # RESERVED_PACKAGE='package'
    # RESERVED_USE='use'
    # RESERVED_NO='no'
    # RESERVED_REQUIRE='require'

    # RESERVED_PRINT='print'
    # RESERVED_PRINTF='printf'
    # RESERVED_SAY='say'

    # RESERVED_MAP='map'
    # RESERVED_GREP='grep'
    # RESERVED_SORT='sort'

    # RESERVED_SCALAR='scalar';
    # RESERVED_EACH='each'
    # RESERVED_KEYS='keys'
    # RESERVED_VALUES='values'
    # RESERVED_DELETE='delete'
    # RESERVED_SPLICE='splice'

    # RESERVED_DEFINED='defined'
    # RESERVED_WANTARRAY='wantarray'
    # RESERvED_BLESS='bless'

    # RESERVED_POP='pop'
    # RESERVED_SHIFT='shift'

    # RESERVED_PUSH='push'
    # RESERVED_UNSHIFT='unshift'

    # RESERVED_REF='ref'
    # RESERVED_SPLIT='split'
    # RESERVED_JOIN='join'
    # RESERVED_LENGTH='length'
    # RESERVED_EXISTS='exists'

    # RESERVED_UNDEF='undef'

    # RESERVED_QW='qw'

    # RESERVED_QQ='qq'
    # RESERVED_Q='q'
    # RESERVED_QX='qx'

    # RESERVED_TR='tr'
    # RESERVED_Y='y'

    # RESERVED_S='s'
    # RESERVED_QR='qr'
    # RESERVED_M='m'

    # RESERVED_FINALLY = 'finally';
    # RESERVED_TRY = 'try';
    # RESERVED_TRYCATCH = 'TryCatch::';
    # RESERVED_CATCH = 'catch';
    # RESERVED_CATCH_WITH = 'catch_with';
    # RESERVED_EXCEPT = 'except';
    # RESERVED_OTHERWISE = 'otherwise';
    # RESERVED_CONTINUATION = 'continuation';

    # RESERVED_SWITCH='switch'
    # RESERVED_CASE='case'

    # RESERVED_MY='my'
    # RESERVED_OUR='our'
    # RESERVED_STATE='state'
    # RESERVED_LOCAL='local'

    # RESERVED_DO='do'
    # RESERVED_EVAL='eval'

    # RESERVED_GOTO='goto'
    # RESERVED_REDO='redo'
    # RESERVED_NEXT='next'
    # RESERVED_LAST='last'

    # RESERVED_RETURN='return'
    # RESERVED_EXIT='exit'


    # RESERVED_METHOD='method'
    # RESERVED_FUNC='func'
    # RESERVED_FUN='fun'
    # RESERVED_METHOD_FP='fp_method'

    # RESERVED_AFTER_FP='fp_after'
    # RESERVED_AROUND_FP='fp_around'
    # RESERVED_AUGMENT_FP='fp_augment'
    # RESERVED_BEFORE_FP='fp_before'
    # RESERVED_OVERRIDE_FP='fp_override'

    # # Operators



    # OPERATOR_X='x'

    # OPERATOR_CMP_NUMERIC='<=>'
    # OPERATOR_LT_NUMERIC='<'
    # OPERATOR_GT_NUMERIC='>'

    # OPERATOR_DEREFERENCE='->'
    # FAT_COMMA='=>'
    # COMMA=','

    # OPERATOR_HELLIP='...'
    # OPERATOR_NYI='nyi'
    # OPERATOR_FLIP_FLOP='..'
    # OPERATOR_CONCAT='.'

    # OPERATOR_PLUS_PLUS='++'
    # OPERATOR_MINUS_MINUS='--'
    # OPERATOR_POW='**'

    # OPERATOR_RE='=~'
    # OPERATOR_NOT_RE='!~'

    # OPERATOR_HEREDOC='heredoc<<'
    # OPERATOR_SHIFT_LEFT='<<'
    # OPERATOR_SHIFT_RIGHT='>>'

    # OPERATOR_AND='&&'
    # OPERATOR_OR='||'
    # OPERATOR_OR_DEFINED='//'
    # OPERATOR_NOT='!'

    # OPERATOR_ASSIGN='='

    # QUESTION='?'
    # COLON=':'

    # OPERATOR_REFERENCE='\\'

    # OPERATOR_DIV='/'
    # OPERATOR_MUL='*'
    # OPERATOR_MOD='%'

    # OPERATOR_PLUS='+'
    # OPERATOR_MINUS='-'

    # OPERATOR_BITWISE_NOT='~'
    # OPERATOR_BITWISE_AND='&'
    # OPERATOR_BITWISE_OR='|'
    # OPERATOR_BITWISE_XOR='^'

    # OPERATOR_AND_LP='and'
    # OPERATOR_OR_LP='or'
    # OPERATOR_XOR_LP='xor'
    # OPERATOR_NOT_LP='not'

    # OPERATOR_ISA='isa'

    # OPERATOR_LT_STR='lt'
    # OPERATOR_GT_STR='gt'
    # OPERATOR_LE_STR='le'
    # OPERATOR_GE_STR='ge'
    # OPERATOR_CMP_STR='cmp'
    # OPERATOR_EQ_STR='eq'
    # OPERATOR_NE_STR='ne'

    # # synthetic tokens
    # OPERATOR_POW_ASSIGN='**='
    # OPERATOR_PLUS_ASSIGN='+='
    # OPERATOR_MINUS_ASSIGN='-='
    # OPERATOR_MUL_ASSIGN='*='
    # OPERATOR_DIV_ASSIGN='/='
    # OPERATOR_MOD_ASSIGN='%='
    # OPERATOR_CONCAT_ASSIGN='.='
    # OPERATOR_X_ASSIGN='x='
    # OPERATOR_BITWISE_AND_ASSIGN='&='
    # OPERATOR_BITWISE_OR_ASSIGN='|='
    # OPERATOR_BITWISE_XOR_ASSIGN='^='
    # OPERATOR_SHIFT_LEFT_ASSIGN='<<='
    # OPERATOR_SHIFT_RIGHT_ASSIGN='>>='
    # OPERATOR_AND_ASSIGN='&&='
    # OPERATOR_OR_ASSIGN='||='
    # OPERATOR_OR_DEFINED_ASSIGN='//='

    # OPERATOR_GE_NUMERIC='>='
    # OPERATOR_LE_NUMERIC='<='
    # OPERATOR_EQ_NUMERIC='=='
    # OPERATOR_NE_NUMERIC='!='
    # OPERATOR_SMARTMATCH='~~'
    # # end of synthetic operators

    # OPERATOR_FILETEST='-t'

    # # single mid-quote. e evaluatable s///e;
    # REGEX_QUOTE='r/'
    # REGEX_QUOTE_E='re/'
    # REGEX_TOKEN='regex'

    # # paired mid-quote. e for evaluatable s{}{}e;
    # REGEX_QUOTE_OPEN='r{'
    # REGEX_QUOTE_OPEN_E='re{' # block should be interpolated as a perl script

    # REGEX_QUOTE_CLOSE='r}'
    # REGEX_MODIFIER='/m'


    # REGEX_LEFT_BRACKET = '[['
    # REGEX_RIGHT_BRACKET = ']]'
    # REGEX_LEFT_PAREN = '(('
    # REGEX_RIGHT_PAREN = '))'
    # REGEX_LEFT_BRACE = '{{'
    # REGEX_RIGHT_BRACE = '}}'
    # REGEX_POSIX_LEFT_BRACKET = '[:'
    # REGEX_POSIX_RIGHT_BRACKET = ':]'
    # REGEX_POSIX_CLASS_NAME = ':name:'
    # REGEX_CHAR_CLASS="\w"


    # STRING_CONTENT='STRING_CONTENT'
    # STRING_CONTENT_QQ='STRING_CONTENT_QQ'
    # STRING_CONTENT_XQ='STRING_CONTENT_XQ'


    # TAG='TAG'
    # TAG_END='__END__'
    # TAG_DATA='__DATA__'
    # TAG_PACKAGE='__PACKAGE__'

    # LEFT_ANGLE='LEFT_ANGLE'
    # RIGHT_ANGLE='RIGHT_ANGLE'

    # TYPE_ARRAYREF="ArrayRef"
    # TYPE_HASHREF="HashRef"

    # LEFT_BRACKET='['
    # RIGHT_BRACKET=']'

    # LEFT_PAREN='('
    # RIGHT_PAREN=')'

    # LEFT_BRACE='{'
    # RIGHT_BRACE='}'

    # SEMICOLON=';';

    # QUOTE_DOUBLE='QUOTE_DOUBLE'
    # QUOTE_DOUBLE_OPEN='QUOTE_DOUBLE_OPEN'
    # QUOTE_DOUBLE_CLOSE='QUOTE_DOUBLE_CLOSE'

    # QUOTE_SINGLE='QUOTE_SINGLE'
    # QUOTE_SINGLE_OPEN='QUOTE_SINGLE_OPEN'
    # QUOTE_SINGLE_CLOSE='QUOTE_SINGLE_CLOSE'

    # QUOTE_TICK='QUOTE_TICK'
    # QUOTE_TICK_OPEN='QUOTE_TICK_OPEN'
    # QUOTE_TICK_CLOSE='QUOTE_TICK_CLOSE'

    # # custom tokens
    # IDENTIFIER='IDENTIFIER'
    # SUB_NAME='subname'

    # BUILTIN_LIST='list'
    # BUILTIN_UNARY='unary'
    # CUSTOM_UNARY='unary_custom'
    # BUILTIN_ARGUMENTLESS='argumentless'

    # ATTRIBUTE_IDENTIFIER='ATTRIBUTE_IDENTIFIER'

    # SUB_PROTOTYPE_TOKEN='SUB_PROTOTYPE_TOKEN'

    # PACKAGE='package::name'
    # QUALIFYING_PACKAGE='package::name::'

    # HANDLE='HANDLE'
    # BLOCK_NAME='BLOCK_NAME'

    # ANNOTATION_DEPRECATED_KEY='#@deprecated'
    # ANNOTATION_RETURNS_KEY='#@returns'
    # ANNOTATION_OVERRIDE_KEY='#@override'
    # ANNOTATION_METHOD_KEY='#@method'
    # ANNOTATION_ABSTRACT_KEY='#@abstract'
    # ANNOTATION_INJECT_KEY='#@inject'
    # ANNOTATION_NO_INJECT_KEY='#@noinject'
    # ANNOTATION_TYPE_KEY='#@type'
    # ANNOTATION_NOINSPECTION_KEY='#@noinspection'
    # ANNOTATION_UNKNOWN_KEY='#@unknown'

    # # lazy parsable tokens parsed in-place
    # LP_CODE_BLOCK = "LP_CODE_BLOCK"
    # LP_CODE_BLOCK_WITH_TRYCATCH = "LP_CODE_BLOCK_WITH_TRYCATCH"
    # LP_STRING_RE = "LP_STRING_RE"
    # LP_STRING_TR = "LP_STRING_TR"
    # LP_STRING_QQ = "LP_STRING_QQ"
    # LP_STRING_QQ_RESTRICTED = "LP_STRING_QQ_RESTRICTED"
    # LP_STRING_Q = "LP_STRING_Q"
    # LP_STRING_QX = "LP_STRING_QX"
    # LP_STRING_QX_RESTRICTED = "LP_STRING_QX_RESTRICTED"
    # LP_STRING_QW = "LP_STRING_QW"
    # LP_REGEX = "LP_REGEX"
    # LP_REGEX_X = "LP_REGEX_X"
    # LP_REGEX_XX = "LP_REGEX_XX"
    # LP_REGEX_SQ = "LP_REGEX_SQ"
    # LP_REGEX_X_SQ = "LP_REGEX_X_SQ"
    # LP_REGEX_XX_SQ = "LP_REGEX_XX_SQ"