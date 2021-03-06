σ
ΨΚη`c           @   sΣ   d  d d     YZ  d d d     YZ e   Z e e j d  e j d  e j d  e j d  e j d  e j d	  e e j d  e j d
  e j   e e j d  e e j d  e d S(   t   ListNodec           B   s    e  Z d d d   Z d   Z RS(   c         C   s   | |  _  | |  _ d  S(   N(   t   datat   next(   t   selfR   R   (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyt   __init__   s    	c         C   s   t  |  j  S(   N(   t   reprR   (   R   (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyt   __repr__	   s    N(   t   __name__t
   __module__t   NoneR   R   (    (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyR       s   t   SinglyLinkedListc           B   sG   e  Z d    Z d   Z d   Z d   Z d   Z d   Z d   Z RS(   c         C   s   d |  _ d S(   sK   
        Create a new singly-linked list.
        Takes O(1) time.
        N(   R	   t   head(   R   (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyR      s    c         C   sM   g  } |  j  } x& | r7 | j t |   | j } q Wd d j |  d S(   sV   
        Return a string representation of the list.
        Takes O(n) time.
        t   [s   , t   ](   R   t   appendR   R   t   join(   R   t   nodest   curr(    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyR      s    		c         C   s   t  d | d |  j  |  _ d S(   s]   
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        R   R   N(   R    R   (   R   R   (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyt   prepend    s    c         C   sW   |  j  s t d |  |  _  d S|  j  } x | j r@ | j } q+ Wt d |  | _ d S(   sW   
        Insert a new element at the end of the list.
        Takes O(n) time.
        R   N(   R   R    R   (   R   R   R   (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyR   '   s    		c         C   s2   |  j  } x" | r- | j | k r- | j } q W| S(   s   
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        (   R   R   R   (   R   t   keyR   (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyt   find4   s    	c         C   sw   |  j  } d } x( | r9 | j | k r9 | } | j } q W| d k rU | j |  _  n | rs | j | _ d | _ n  d S(   s\   
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        N(   R   R	   R   R   (   R   R   R   t   prev(    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyt   remove?   s    	c         C   sM   |  j  } d } d } x( | r? | j } | | _ | } | } q W| |  _  d S(   sE   
        Reverse the list in-place.
        Takes O(n) time.
        N(   R   R	   R   (   R   R   t	   prev_nodet	   next_node(    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyt   reverseR   s    				
(	   R   R   R   R   R   R   R   R   R   (    (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyR
      s   						i   t   ai*   t   Xt   thet   endt   yN(    (    (   R    R
   t   lstR   R   R   R   R   (    (    (    sR   /Users/amina_adewusi/code/pythonPlay/dataStructures/singly_linked_list_template.pyt   <module>   s$   	U	
