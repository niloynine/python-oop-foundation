1️⃣ In a normal list

Search → O(n)
(Simple, but slow for large data)

2️⃣ In a sorted list + binary search

Search → O(log n)
(Faster, but insertion becomes expensive → O(n))

3️⃣ In a dictionary (hash table)

Search → O(1) average
(Fastest lookup)

🎯 Now Real Engineering Thinking

Every data structure has trade-offs:

Structure	Search	    Insert	Keep Sorted?

List    	O(n)	    O(1)*	No
Sorted List	O(log n)	O(n)	Yes
Dictionary	O(1)	    O(1)	No

🔥 Stack Unwinding:

code:

def f(n):
    if n == 0:
        return
    f(n-1)
    print(n)

f(3)

explaination:

f(3)
 → calls f(2)
      → calls f(1)
           → calls f(0)
                → returns
           → print(1)
      → print(2)
 → print(3)

 Because even though f(0) returns immediately,
the earlier function calls are still waiting.

Once f(0) finishes,
the stack starts unwinding,
and each call prints its number.

Code Order	     Output Order
print → recurse	decreasing
recurse → print	increasing

If input shrinks by division:

Recurrence	     Complexity
T(n) = T(n/2)	     O(log n)
T(n) = T(n/2)+n	O(n)
T(n) = 2T(n/2)	     O(n)
T(n) = 2T(n/2)+n	O(n log n)

🎯 Quick Summary
Recurrence	     Complexity
T(n) = T(n/2)	     O(log n)
T(n) = 2T(n/2)	     O(n)
T(n) = 2T(n/2)+n	O(n log n)
T(n) = 2T(n-1)	     O(2^n)