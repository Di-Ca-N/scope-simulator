grammar Poodle;

parse
    : progStmts* EOF
    ;

progStmts 
    : progStmt
    | progStmt progStmts 
    ;

progStmt
    : varDeclaration NEWLINE?
    | varAssignment NEWLINE?
    | funcDef NEWLINE?
    | funcCall NEWLINE?
    ;

varDeclaration
    : 'var ' IDENTIFIER ' '? '=' ' '? mathExpr ';' 
    ;

varAssignment
    : IDENTIFIER ' '? '=' ' '? mathExpr ';'
    ;

mathExpr
    : INT 
    | IDENTIFIER
    | '(' mathExpr ')'
    | left=mathExpr op=('*'|'/') right=mathExpr
    | left=mathExpr op=('+'|'-') left=mathExpr
    ;

funcDef
    : 'function ' IDENTIFIER '(' funcArgs ')' NEWLINE* '{' progStmts '}'
    ;

funcArgs
    : 
    | (INT | IDENTIFIER)
    | (INT | IDENTIFIER) ARG_SEP (SPACE)* funcArgs
    ;

funcCall
    : IDENTIFIER '(' funcArgs ')' ';'
    ;

SPACE
    : ' ' -> skip
    ;

ARG_SEP
    : ','
    ;

funcBody
    : progStmts
    ;

IDENTIFIER 
    : [a-zA-Z][a-zA-Z0-9]*
    ;

INT
    : [0-9]+
    ;

NEWLINE
    : [\n\r]+ -> skip
    ;
