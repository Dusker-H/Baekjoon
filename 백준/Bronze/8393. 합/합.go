package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var x, sum int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()

	fmt.Fscanln(r, &x)

	for i := 1; i <= x; i++ {
		sum = sum + i
	}
	fmt.Fprintln(w, sum)
}
