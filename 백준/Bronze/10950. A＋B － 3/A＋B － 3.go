package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, a, b int
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d %d\n", &a, &b)
		fmt.Fprintf(writer, "%d\n", a+b)

	}
}
