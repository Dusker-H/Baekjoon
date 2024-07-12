package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func main() {

	var n, m, max, sum int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()

	fmt.Fscanf(r, "%d %d\n", &n, &m)
	slice := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscan(r, &slice[i])
	}
	slices.Sort(slice)

	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				sum = slice[i] + slice[j] + slice[k]
				if sum <= m && sum >= max {
					max = sum
				} else if sum > m {
					break
				}
			}

		}
	}

	fmt.Fprintln(w, max)
}
