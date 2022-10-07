#test mode used to test cap distance and slew
buffer_num = 45
star_buffer_node = 100000
star_node_id = 2

out_file_name = "outfile"
input_name = "infile"

with open(out_file_name, 'w') as f:
    f.write("sourcenode 0 0\n")
    f.write("num node {}\n".format(buffer_num*2))
    for i in range(0, buffer_num*2):
        star_buffer_node =  star_buffer_node + 450000
        f.write('{} {} {}\n'.format(i+2, 0, star_buffer_node))
    f.write("num sinknode {}\n".format(1))
    f.write('{} {}\n'.format(1,1))

    #wire
    f.write("num wire {}\n".format(buffer_num +1))
    f.write("{} {} 0\n".format(0,2))
    j=0
    i = 0
    for i in range(0, buffer_num-1):
        j = j + 2
        f.write("{} {} 0\n".format(j+1, j+2))
    f.write("{} {} 0\n".format(j + 3, 1))
    f.write("num buffer {}\n".format(buffer_num))
    j = 0
    for i in range(0, buffer_num):
        j = j +2
        f.write("{} {} 0\n".format(j , j + 1))
f.close()