package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	reader := bufio.NewReader(os.Stdin)

	fmt.Fscanln(reader, &n)
	slice := make([]int, n)

	for i := 1; i <= n; i++ {
		slice[i-1] = i
	}

	for len(slice) > 1 {
		slice = append(slice[2:len(slice)], slice[1])
	}

	fmt.Println(slice[0])

}
