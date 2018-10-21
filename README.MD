Testing for the chess application

# Business domain tests
## Valid moves 
### For each piece is their general type of movement supported
### Single and Double advancement for pawns at first movement

## Invalid moves
1. restrictions on pawn movement to single advancement after 1st movement
2. passing through own pieces (rooks, bishops, should not pass through pawns)

## Capturing
1. Support for catupring opponents pieces
2. Inability to self capture

## board status
1. limitations of statelessness
2. piece count checks

## Special movements
1. castling
2. capturing en-passen
3. pawn promotions
4. check and check mate 

# API Contract issues
## limitations to the protocol
1. inability to distinguish some moves because of support for type + end position, not start position
2. 

# Engine errors
## lack of support for valid movements
##
