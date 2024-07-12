package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, max, min int
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscanln(reader, &n)

	var slice = make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &slice[i])
	}

	max = slice[0]
	min = slice[0]

	for _, list := range slice {
		if max < list {
			max = list
		} else if min > list {
			min = list
		}

	}
	fmt.Printf("%d %d\n", min, max)
}
