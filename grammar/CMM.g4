//Adapted from CST-301-RS-T7-C--Grammar.docx

grammar CMM;

//Program ------> VarDeclList FunDeclList 
program: varDeclList funDeclList;

//VarDeclList --> epsilon 
//VarDecl VarDeclList
varDeclList: varDecl*;

//VarDecl ------> Type id ;
//Type id [ num] ; 
varDecl: type ID ('[' NUM ']')? ';' ;

//FunDeclList --> FunDecl 
funDeclList: funDecl*;

//FunDecl FunDeclList
//FunDecl ------> Type id ( ParamDecList ) Block
funDecl: type ID '(' paramDeclList? ')' block;

//ParamDeclList --> epsilon 
//ParamDeclListTail 
//ParamDeclListTail --> ParamDecl 
//ParamDecl, ParamDeclListTail 
paramDeclList: paramDecl (',' paramDecl)*;

//ParamDecl ----> Type id
//Type id[]
paramDecl: type ID;

//Block --------> { VarDeclList StmtList } 
block: '{' varDeclList? stmtList? '}';

//Type ---------> int
//char
type: 'int' | 'char';

//StmtList -----> Stmt 
//Stmt StmtList 
stmtList: stmt+;

//Stmt ---------> ;
//Expr ; 
//return Expr ;
//read id ;
//write Expr ;
//writeln ;
//break ;
//if ( Expr ) Stmt else Stmt
//while ( Expr ) Stmt 
//Block
stmt: ';' 
    | expr ';' 
    | 'return' expr ';' 
    | 'read' ID ';' 
    | 'write' expr ';' 
    | 'writeln' ';' 
    | 'break' ';' 
    | 'if' '(' expr ')' stmt ('else' stmt)? 
    | 'while' '(' expr ')' stmt 
    | block;

//Expr ---------> Primary 
//UnaryOp Expr
//Expr BinOp Expr
//id = Expr 
//id [ Expr ] = Expr 
expr: primary | unaryOp expr | expr binOp expr | ID '=' expr | ID '[' expr ']' '=' expr;

//Primary ------> id
//num 
//( Expr )
//id ( ExprList )
//id [ Expr ] 
primary: ID | NUM | '(' expr ')' | ID '(' exprList ')' | ID '[' expr ']';

//ExprList -----> epsilon 
//ExprListTail 
//ExprListTail --> Expr 
//Expr , ExprListTail
exprList: expr (',' expr)*;

//UnaryOp ------> - | !
unaryOp: '-' | '!';

//BinOp --------> + | - | * | / | == | != | < | <= | > | >= | && | ||
binOp: '+' | '-' | '*' | '/' | '==' | '!=' | '<' | '<=' | '>' | '>=' | '&&' | '||';

// Tokens
ID: [a-zA-Z]+;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;

// Keywords
IF: 'if';
ELSE: 'else';
WHILE: 'while';
RETURN: 'return';
READ: 'read';
WRITE: 'write';
WRITELN: 'writeln';
BREAK: 'break';

// Types
INT: 'int';
CHAR: 'char';

// Operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
EQUALS: '=';
EQUALS_EQUALS: '==';
NOT_EQUALS: '!=';
LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';

// Symbols
SEMI: ';';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
