alphash
=======

Unix command line tool for hashing values to ascii chars

Quickstart
=====================================

**Hash input string to default chars (lower case)**

    $ alphash --input helloworld
    >>> phoognfttaykjiokfgvr
    
**Hash input to alphanumeric chars**

    $ alphash --input helloworld --alphanumeric 
    >>> RLg2fY7fuDkOnDJMjuKw

**Hash input to alphanumeric + special chars  ( !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ )**

    $ alphash --input helloworld --all
    >>> $LWM$"?%D<OuzT|a+y^X
    
**Hash input using a seed ( either int or string )**

    $ alphash --input helloworld --all --seed myseed
    >>> vfO#ZeN(0h3<k<oG{8
    
**Hash using secure input**

    $ alphash --all --seed myseed -si
    >>> Secure Input:
    >>> w)`di}J=CocCaO*T%Yg7
