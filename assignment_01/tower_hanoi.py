def move(disk, x, y):
    print('- Pindahkan disk ke-'+str(disk)+' dari tower '+str(x)+' -> '+str(y))


tumpukan = [1,2,3,4,5]

#get 3 tumpukan teratas
top_stack = tumpukan[0:3]
print('top_stack =',top_stack)

arr_tower = [1,2,3]
tower_asal = 1
tower_tujuan = 3
arr_move = [tower_asal, tower_tujuan]

#mendapatkan tower temporary
tower_temp = list(set(arr_tower) - set(arr_move))[0]

print('Memindahkan 3 disk dari tower '+str(tower_asal)+' ke tower '+str(tower_tujuan))

#for piringan in tumpukan:
#    print('piringan ke-'+str(piringan))

# move disk index top dari asal -> tujuan
move(top_stack[0], tower_asal, tower_tujuan)

# move disk index top+1 dari asal -> temp
move(top_stack[1], tower_asal, tower_temp)

# move disk index top dari tujuan -> temp
move(top_stack[0], tower_tujuan, tower_temp)

# move disk index top+2 dari asal -> tujuan
move(top_stack[2], tower_asal, tower_tujuan)

# move disk index top dari temp -> asal
move(top_stack[0], tower_temp, tower_asal)

# move disk index top+1 dari temp -> tujuan
move(top_stack[1], tower_temp, tower_tujuan)

# move disk index top dari asal -> tujuan
move(top_stack[0], tower_asal, tower_tujuan)

#cek apakah 