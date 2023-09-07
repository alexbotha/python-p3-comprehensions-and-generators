#!/usr/bin/env python3

import ipdb

def return_evens(num_list):
   return [number for number in num_list if number % 2 == 0]

def make_exclamation(sentence_list):
    return [s + "!" for s in sentence_list]