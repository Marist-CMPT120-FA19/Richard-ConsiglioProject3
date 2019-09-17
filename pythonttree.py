tree_height = eval(input ("How tall do you want your tree to be? (only positive numbers)"))
o=int(tree_height)
h = " "
x=.5
while (tree_height>0):

    print (tree_height*h, int (x*2)*"#")
    x=x+1
    tree_height=tree_height-1
print(o*h , "#")
