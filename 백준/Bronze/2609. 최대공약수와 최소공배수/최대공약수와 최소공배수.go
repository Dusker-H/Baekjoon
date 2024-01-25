package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var x, y, i int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()

	fmt.Fscanf(r, "%d %d", &x, &y)

	if x > y {
		i = y
		for (x%i != 0) || (y%i != 0) {
			i--
		}
		x = x / i
		y = y / i
	} else {
		i = x
		for (x%i != 0) || (y%i != 0) {
			i--
		}
		x = x / i
		y = y / i
	}
	fmt.Fprintln(w, i)
	fmt.Fprintln(w, i*x*y)

}
