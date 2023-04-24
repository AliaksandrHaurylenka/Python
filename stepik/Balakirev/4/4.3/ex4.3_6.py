m = ['#до', 'ре', 'ми', '#фа', 'соль', 'ля', 'си']
# num_notes = list(map(int, input().split()))
# print(*num_notes)
#
# noutes = f"{m[num_notes[0] - 1]} {m[num_notes[1] - 1]} {m[num_notes[2] - 1]}"
# print(noutes)

one_note, two_note, three_note = map(int, input().split())
# print(one_note, two_note, three_note)

# noutes = f"{m[one_note - 1]} {m[two_note - 1]} {m[three_note - 1]}"
noutes = [m[one_note - 1], m[two_note - 1], m[three_note - 1]]
print(*noutes)

# res = () if m[0]
# res = ('#до' if 'фа') if 'до' in noutes else ()
