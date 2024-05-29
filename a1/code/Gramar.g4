


grammar Gramar;

names: (transaction (';' transaction)*) EOF;

transaction: person operation;

person: name '('age ',' phone')';

name: firstName lastName;

operation: type ammount;

firstName: STRING;
lastName: STRING;
type: STRING;
ammount: DIGITS;
age: DIGITS;
phone: PHONE;

DIGITS: [0-9]+;
STRING: [a-zA-Z]+;
PHONE: [+0-9]+;
WS: [ \t\r\n]+ -> skip;
