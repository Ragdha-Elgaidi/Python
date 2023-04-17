# Definitions for sequences
- Let’s say we have string aaabcdefgg
- Prefix: Any string starts from the first character (n prefixes)
    - a, aa, aaa, aaab, aaabc, ….. aaabcdefgg
- Suffix: Any string sends at the last character (n suffixes)
    - g, gg, fgg, efgg, …. Aaabcdefgg
- Substring: Starts wherever and end wherever, but consecutive
    - E.g. of length 3: aaa, aab, abc, cde, def, efg, fgg. Same as subarray.
- Sub-sequence: Not consecutive but must be in order
- In order: Next letter must has bigger index
- adef, bgg, aeg, cdgg
- aeg indices: 0 5 8
- But not: gga, ed, aca
#  Membership Operators
- in operator
```py
# We call string a sequence
# str1 in str2: true IF str1 is substring of str2
name = 'ragdha'
# All prints are True
print('ragdha' in name)
print('ragdh' in name)
print('ragd' in name)
print('rag' in name)
print('ra' in name)
print('r' in name)
print('agdha' in name)
print('gdha' in name)
print('dha' in name)
print('ha' in name)
print('a' in name)
```
- not in operator
```py
name = 'ragdha'
# All prints are false
print('ragdha' not in name)
print('ragdh' not in name)
print('ragd' not in name)
print('rag' not in name)
print('ra' not in name)
print('r' not in name)
print('agdha' not in name)
print('gdha' not in name)
print('dha' not in name)
print('ha' not in name)
print('a' not in name)
```

```
