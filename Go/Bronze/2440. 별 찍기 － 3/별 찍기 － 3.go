package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var x int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()

	fmt.Fscanln(r, &x)

	for i := x; i > 0; i-- {
		for j := i; j > 0; j-- {
			fmt.Fprint(w, "*")
		}
		fmt.Fprintln(w, "")
	}

}
