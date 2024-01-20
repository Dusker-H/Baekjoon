package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	var n, count int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	defer w.Flush()

	fmt.Fscanln(r, &n)

	slice := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscan(r, &slice[i])
	}
	count = 0
	for i := 0; i < n; i++ {
		for j := 2; j <= slice[i]; j++ {
			if slice[i]%j == 0 && slice[i] != j {
				break
			} else if j == slice[i] {
				count++
			}
		}
	}
	fmt.Fprintln(w, count)
}
