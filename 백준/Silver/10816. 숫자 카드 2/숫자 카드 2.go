package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func lowerBound(array []int, target int) int {
	var start, end, mid int
	end = len(array) - 1

	for start < end {
		mid = (start + end) / 2
		if array[mid] >= target {
			end = mid
		} else {
			start = mid + 1
		}
	}
	return end
}
func upperBound(array []int, target int) int {
	var start, end, mid int
	end = len(array) - 1

	for start < end {
		mid = (start + end) / 2
		if array[mid] > target {
			end = mid
		} else {
			start = mid + 1
		}
	}
	if array[end] != target {
		end--
	}
	return end
}
func main() {
	var n, m int

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	fmt.Fscanln(reader, &n)

	slice1 := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &slice1[i])

	}

	sort.SliceStable(slice1, func(i, j int) bool {
		if slice1[i] < slice1[j] {
			return true
		} else {
			return false
		}
	})
	reader.ReadString('\n') // 입력 스트림에 남아 있는 개행문자 제거

	fmt.Fscanln(reader, &m)

	slice2 := make([]int, m)

	for i := 0; i < m; i++ {
		fmt.Fscan(reader, &slice2[i])

	}

	for i := 0; i < m; i++ {
		fmt.Fprintf(writer, "%d ", upperBound(slice1, slice2[i])-lowerBound(slice1, slice2[i])+1)
	}

}
