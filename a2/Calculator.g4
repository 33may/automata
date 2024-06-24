grammar Calculator;

instance: expr EOF;

expr: term ((PLUS | MINUS) term)*;
term: factor ((MULT | DIV) factor)*;
factor: INT
      | FLOAT
      | '(' expr ')';

INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
WS: [ \t\r\n]+ -> skip;
