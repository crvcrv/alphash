alphash
=======

Unix command line tool for hashing values to ascii chars

Quickstart
=====================================

**Hash input string to default chars (lower case)**

    $ alphash --input foobar
    >>> liyyffytybcuhargzwsk
    
**Hash input to alphanumeric chars**

    $ alphash --input foobar --alphanumeric 
    >>> xYvc8QRey2EaMEVwVAOe

**Hash input to uppercase + digits**

    $ alphash --input foobar --digits --uppercase
    >>> L4SNNMTF3D41R9EKWWC6


**Hash input to alphanumeric + special chars  ( !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ )**

    $ alphash --input foobar --all
    >>> q_n\pF"@h(_h5Uhl<ET"
    
**Hash input using a seed ( either int or string )**

    $ alphash --input foobar --all --seed myseed
    >>> D!(={7IyCjn,`(>)\SIX
    
**Hash using secure input**

    $ alphash --all --seed myseed -si
    >>> Secure Input:
    >>> D!(={7IyCjn,`(>)\SIX
