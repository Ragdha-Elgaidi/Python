# Operator Associativity
- Almost all the operators have left-to-right associativity
- 10 - 6 + 3 ⇒ (10 - 6) + 3 ⇒ 4 + 3 = 7
- Exponent operator ** has right-to-left associativity in Python
- 2 ** 3 ** 4 ⇒ 2 ** (3 ** 4) = 2 ** 81 = 2417851639229258349412352Operator Associativity
- Almost all the operators have left-to-right associativity
- 10 - 6 + 3 ⇒ (10 - 6) + 3 ⇒ 4 + 3 = 7
- Exponent operator ** has right-to-left associativity in Python
- 2 ** 3 ** 4 ⇒ 2 ** (3 ** 4) = 2 ** 81 = 2417851639229258349412352Order of Evaluation
- (2 ** 10) / (2 + 3 * 4) 
- Which expression will be evaluated first? (2 ** 10) ? (2 + 3 * 4)?
- The left operand is always evaluated before the right operand
- Same for function arguments
- (1+2) ** (3-1) ** (4-2)
- Left to right evaluation for every expression
- Right to left associativity to compute final results
#### Precedence vs Associativity vs Order of Evaluation
- Operator precedence specifies the order of operations in expressions that contain more than one operator
 ( e.g. * before +)
- Associativity is about how to group operands (if operations has the same priority)
- But first, we need to evaluate operands/subexpressions
- Order of evaluation is about the order of evaluating the operands
- Always left first
