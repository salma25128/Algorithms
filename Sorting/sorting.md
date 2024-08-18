
-----------------------------------------------------------------------------------------------------
**_Loop Invariant**_

https://github.com/salma25128/Algorithms/blob/d7811a04568d655ac084aa3b409ddc64385cc47f/Sorting/Insertionsort.py#L53

                                 | start |
                                 +-------+
                                     |
                                     | <--- Q (the precondition) holds here (assumption)
                                     |
         +-------------------------> | <--- P (the invariant) holds here (every time)
         |                           |
         |                           |
         |                          / \
         |                         /   \
         |                 true   /  B  \   false
         |               +<------ \     / -------->+
         |    P & B ---->|         \   /           |
         |    holds      |          \ /            | <---- P & !B  holds here
         |    here       v                         |
         |             +---+                       | <---- R (postcondition)
         |             | S |                       v       is to hold here
         |             +---+                    +------+
         |               |                      | stop |
         |               |                      +------+
         +<--------------+
