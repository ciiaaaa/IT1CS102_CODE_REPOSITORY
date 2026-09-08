a = 5
b = 10
c = 15

#tt
print( a < b and c > a )

#ff
print( a > b or c < a )

#tt
print( a != b and c > b )

#tf
print( a != b and c == b) 

#ttt
print( a < b and c > a and a != c )
print( not( a < b and c > a and a != c ))