NF == 0 {
    # Skip any line that does not have data
    next
}

!initialized {
# Initialize the max and min for each column from the
# data on the first line of input that has data.
# Then immediately skip to next line.

nf = 1

for (i = 1; i <= nf; ++i)
            max[i] = min[i] = $i

initialized = 1
        next
    }

    {
# Loop over the columns to see if the max and/or min
# values need updating.

for (i = 1; i <= nf; ++i) {
if (max[i] < $i) max[i] = $i
if (min[i] > $i) min[i] = $i
    }
}

END {
    # Output max and min values for each column.

    for (i = 1; i <= nf; ++i)
#       printf("Column %d min %s max %s\n", i, min[i], max[i])
       printf(" %s  %s\n", min[i], max[i])
            }

