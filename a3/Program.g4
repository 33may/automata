grammar Program;

program: line* EOF;

line: ((assignment ';') | condition | (increase ';') | whileLoop | returnStmt);

assignment: VARIABLE '=' val;

condition: block;

increase: VARIABLE '++';

block: ifBlock elifBlock* elseBlock?;

ifBlock: 'if' '(' logicalExpression ')' '{' body '}';

elifBlock: 'elif' '(' logicalExpression ')' '{' body '}';

elseBlock: 'else' '{' body '}';

whileLoop: 'while' '(' logicalExpression ')' '{' body '}';

body: line*;

returnStmt: 'return ' val;

logicalExpression: (val LOGICAL val) | BOOLEAN;

val: VARIABLE | INT;

BOOLEAN: 'True' | 'False';
VARIABLE: [a-zA-Z]+;
LOGICAL: '>' | '<' | '>=' | '<=' | '==';
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
WS: [ \t\r\n]+ -> skip;
