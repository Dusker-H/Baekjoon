package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type coordinate struct {
	x int
	y int
}

func main() {
	var n int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()

	fmt.Fscan(r, &n)
	r.ReadString('\n')

	slice := make([]coordinate, n)

	for i := 0; i < n; i++ {
		fmt.Fscanln(r, &slice[i].x, &slice[i].y)
	}
	sort.SliceStable(slice, func(i, j int) bool {
		if slice[i].x < slice[j].x {
			return true
		} else if (slice[i].x == slice[j].x) && (slice[i].y < slice[j].y) {
			return true
		} else {
			return false
		}
	})

	for i := 0; i < n; i++ {
		fmt.Fprintf(w, "%d %d\n", slice[i].x, slice[i].y)
	}
}
