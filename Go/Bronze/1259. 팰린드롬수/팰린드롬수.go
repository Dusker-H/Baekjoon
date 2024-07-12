package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var str string
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	for true {
		fmt.Fscanln(reader, &str)
		n := len(str)

		if str == "0" {
			break
		} else if n == 1 {
			fmt.Fprintln(writer, "yes")
		}

		if str[0] == str[n-1] {
			for i := 1; i <= n-1; i++ {
				if str[i] == str[n-i-1] {
					if i >= n/2 {
						fmt.Fprintln(writer, "yes")
						break
					}
				} else {
					fmt.Fprintln(writer, "no")
					break
				}
			}
		} else {
			fmt.Fprintln(writer, "no")

		}
	}
}
