#!/usr/bin/env python
"""
Copyright (c) 2014, <47bytes@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.
"""
import argparse
import getpass
import hashlib
import logging
import sys
import string
import random

LOG = logging.getLogger(__name__)

VERSION = '1.21'

def string_or_int(value):
    try:
        return int(value)
    except ValueError:
        return string_to_number(value)

def string_to_number(value):
    """
    takes string and makes an hashed int out of it
    """
    return int(hashlib.sha512(value.encode()).hexdigest(), 16)

def biggest_list_index_in_number(n, chars):
    """
    takes a number and splits it up in parts of usable indices for chars list
    """
    numbers = list(str(n))
    number = ''
    i = 0
    erg_list = []
    tmp_number_list = []

    while True:
        LOG.debug('new while run-----')

        last_item_popped = numbers.pop(0) #get first number

        LOG.debug('last item {0}'.format(last_item_popped))

        tmp_number_list.append(last_item_popped) 

        LOG.debug('tmp_list after insert {0}'.format(tmp_number_list))

        # is the current number still smaller then the biggest index of chars?
        if len(chars) > int(''.join(tmp_number_list)):
            # are there still numbers to pop?
            if numbers:
                continue
            else:
                erg_list.append(''.join(tmp_number_list))
                break
        else:
            # one item popped to many
            LOG.debug('-----one item to many-----')
            LOG.debug('append {0}'.format(''.join(tmp_number_list[:-1])))

            erg_list.append(''.join(tmp_number_list[:-1])) # append number before last pop to list
            numbers.insert(0,last_item_popped) # undo pop

            tmp_number_list = list() # empty
    return [int(e) for e in erg_list]

def main():
    desc = """Hashes input and returns an alphanumeric value.\n\n\tThis programm is licenced under the 'Modified BSD License'.\n\tCopyright (c) 2014, <47bytes@gmail.com> \n\tAll rights reserved."""
    parser = argparse.ArgumentParser(
        prog='alphash',
        description=desc,
        formatter_class = argparse.RawDescriptionHelpFormatter,
    )
    input_group = parser.add_mutually_exclusive_group(required=True)

    input_group.add_argument('-si', '--secure-input', help='Secure input', required=False, action='store_true', default=False)
    input_group.add_argument('-i','--input', help='String to convert', required=False, default='')

    parser.add_argument('-s', '--seed', help='use this seed to improve (pseudo)random generation of the result string. can be either int or string. default seed is 104053', default=104053, type=string_or_int)
    parser.add_argument('--length', help='length of result string. default length is 20', default=20, type=int)

    parser.add_argument('-lc','--lowercase', help='use lowercase chars. default True', required=False, action='store_true', default=False)
    parser.add_argument('-uc','--uppercase', help='use uppercase chars. default False', required=False, action='store_true', default=False)
    parser.add_argument('-d','--digits', help='use digits. default False', required=False, action='store_true', default=False)
    parser.add_argument('-sc','--special-chars', help='use spechial chars. default False', required=False, action='store_true', default=False)
    parser.add_argument('--alphanumeric', help='shortcut for -lc -uc -d', action='store_true', required=False, default=False)
    parser.add_argument('-a','--all', help='shortcut for -lc -uc -d -sc', action='store_true', required=False, default=False)

    parser.add_argument('-V', '--version', action='version', version='%(prog)s {v}'.format(v=VERSION))
    args = vars(parser.parse_args())
    chars = ''

    if args['all']:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    elif args['alphanumeric']:
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    else:
        if args['lowercase']:
            chars += string.ascii_lowercase
        if args['uppercase']:
            chars += string.ascii_uppercase
        if args['digits']:
            chars += string.digits
        if args['special_chars']:
            chars += string.punctuation
        if not chars:
            # default to lowercase
            chars += string.ascii_lowercase

    if args['secure_input']:
        value = getpass.getpass('Secure Input: ')
    else:
        value = args['input']

    chars = list(chars)

    seed = args['seed']
    old_seed = seed

    num = string_to_number(value)
    indices = biggest_list_index_in_number(num, chars)
    result = list()

    for i in indices:
        old_seed = seed
        seed = seed << i
        seed = seed ^ int(hashlib.sha1(str(old_seed**i).encode()).hexdigest(), 16)#old_seed

        seed = int(hashlib.sha512(str(seed).encode()).hexdigest(), 16)

        random.seed(seed)
        random.shuffle(chars)

        result.append(chars[i])

    r = ''.join(result)
    length = args['length']

    print(r[:length])

    return 0

if __name__ == '__main__':
    alpha = main()

    sys.exit(alpha)