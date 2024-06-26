grammar html;

document
    : doctype? (html | element*) EOF
    ;

doctype
    : '<!DOCTYPE html>'
    ;

html
    : '<html>' head body '</html>'
    ;

head
    : '<head>' element* '</head>'
    ;

body
    : '<body>' element* '</body>'
    ;

element
    : tag_open (content | element)* tag_close
    | self_closing_tag
    | single_tag
    ;

tag_open
    : '<' tag_name (attribute)* '>'
    ;

tag_close
    : '</' tag_name '>'
    ;

self_closing_tag
    : '<' tag_name (attribute)* '/>'
    ;

single_tag
    : '<' tag_name (attribute)* '>'
    ;

attribute
    : TEXT '=' VALUE
    ;

content
    : (TEXT | KNOWN_TAG)+
    ;

tag_name
    : KNOWN_TAG | TEXT
    ;

KNOWN_TAG
    : 'html' | 'head' | 'title' | 'base' | 'link' | 'meta' | 'style' | 'script' | 'noscript' |
      'body' | 'section' | 'nav' | 'article' | 'aside' | 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6' |
      'header' | 'footer' | 'address' | 'main' | 'p' | 'hr' | 'pre' | 'blockquote' | 'ol' | 'ul' |
      'li' | 'dl' | 'dt' | 'dd' | 'figure' | 'figcaption' | 'div' | 'a' | 'em' | 'strong' | 'small' |
      's' | 'cite' | 'q' | 'dfn' | 'abbr' | 'ruby' | 'rt' | 'rp' | 'data' | 'time' | 'code' | 'var' |
      'samp' | 'kbd' | 'sub' | 'sup' | 'i' | 'b' | 'u' | 'mark' | 'bdi' | 'bdo' | 'span' | 'br' |
      'wbr' | 'ins' | 'del' | 'img' | 'iframe' | 'embed' | 'object' | 'param' | 'video' | 'audio' |
      'source' | 'track' | 'canvas' | 'map' | 'area' | 'svg' | 'math' | 'table' | 'caption' |
      'colgroup' | 'col' | 'tbody' | 'thead' | 'tfoot' | 'tr' | 'td' | 'th' | 'form' | 'fieldset' |
      'legend' | 'label' | 'input' | 'button' | 'select' | 'datalist' | 'optgroup' | 'option' |
      'textarea' | 'keygen' | 'output' | 'progress' | 'meter' | 'details' | 'summary' | 'menuitem' |
      'menu'
    ;


TEXT
    : [a-zA-Z0-9_:.,%$!?;@#&*()-]+
    ;

VALUE
    : '"' ('\\' . | ~('\\'|'"'))* '"'
    ;



WS
    : [ \t\r\n]+ -> skip
    ;
