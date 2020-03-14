# BPP Parser

A simple parser for BPP tool based on ply(lex and yacc in Python).

## How to Use
1. Name the input file with "input.txt" and place it in folder "parser/".
2. Replace the 
```
from structure import formula, process_num, rules, bound_k
```
in checking.py with 
```
from parser.translate import formula, process_num, rules, bound_
```

- You can run parser_sample.py to check parser's output

## Input Format

## Sample
X, Y; --> All varibales      
a, b; --> All actions   
[X, a, (Y)]  
[Y, b, (X, Y)]; --> rules    
X; --> start state   
Eg(Ea(a, X + Y >= 2));  --> logic format    
7  --> bound number

## Rule Format
[ variable , action , (variable vector)]

## Logic Format
 - ! formula -> ﹁ φ
 - formula & formula -> φ ∧ φ
 - formula | formula -> φ ∨ φ
 - Ea( action , formula ) -> operator E<act>(φ)
 - Aa( action , formula ) -> operator A<act>(φ)
 - Eg( formula ) -> operator EG(φ)
 - Af( formula ) -> operator AF(φ)
 - expersion >= number -> Atom ( example: X + 2Y >= 4 ) (NO '*' between number and formula)

## Lex Analysis

### Numbers
Only positive integer is supported.

### Reserved Words

- 'Eg' -> operator EG(φ)
- 'Af' -> operator AF(φ)
- 'Ea' -> operator E<act>(φ)
- 'Aa' -> operator A<act>(φ)

### Variable Name

Variable names are composed of uppercase letters and digits, and variable names must start with a uppercase letter.

#### Example

- V √
- VAR √
- VAR01 √
- var ×
- Var ×
- VAR01SCOPE2 √

### Action Name

Action names are composed of lowercase letters and digits, and action names must start with a lowercase letter.

#### Example

- a √
- act √
- act01 √
- ACT ×
- Act ×
- act01scope2 √

### Supported Symbol

- ',' -> comma
- ';' -> semicolon
- '!' -> not
- '&' -> and
- '|' -> or
- '+' -> plus
- '-' -> minus
- '>=' -> greater or eqaul
- '(' -> left paren
- ')' -> right paren
- '[' -> left brack
- ']' -> right brack
- '{' -> left brace
- '}' -> right brace

## Grammar Analysis

- input -> variables SEMICOLON rules SEMICOLON VAR SEMICOLON eglogicformula SEMICOLON NUMBER
- variables -> VAR
- variables -> variables COMMA VAR
- actions -> ACT
- actions -> actions COMMA ACT
- rules -> rule
- rules -> rules rule
- rule -> LBRACK VAR COMMA ACT COMMA LPAREN variables RPAREN RBRACK
- eglogicformula -> formula
- formula -> atom
- formula -> LPAREN formula RPAREN
- formula -> NOT LPAREN formula RPAREN
- formula -> LPAREN formula RPAREN AND LPAREN formula RPAREN
- formula -> LPAREN formula RPAREN OR LPAREN formula RPAREN
- formula -> EA LPAREN ACT COMMA formula RPAREN
- formula -> AA LPAREN ACT COMMA formula RPAREN
- formula -> EG LPAREN formula RPAREN
- formula -> AF LPAREN formula RPAREN
- atom -> plus_expes GE NUMBER
- plus_expes -> exp
- plus_expes -> plusexpes PLUS exp
- exp -> VAR
- exp -> NUMBER VAR