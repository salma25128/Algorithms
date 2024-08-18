
-----------------------------------------------------------------------------------------------------
**_Loop Invariant**_

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
