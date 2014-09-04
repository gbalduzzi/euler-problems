import java.util.ArrayList;
import java.util.List;

/**
 * Problem 1 from Project Euler
 * If we list all the natural numbers below 10 that are multiples of 3 and 5, we get 3, 5, 6 and 9. The sum of these multipes is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * 
 * This file is made with Eclipse using Java SE 1.6.x on Linux.
 * 
 * PLEASE NOTE
 * In order to work you should have Java SDK installed on your machine
 * 
 * REGARDING THE PERFORMANCE
 * This is not the final version of this algorithm, I'll trace the version of every solution. For any suggest of improvments please
 * open an issue or a pull request.
 * 
 * @author Claudio Ludovico Panetta (@Ludo237)
 * @version 1.0.0
 *
 */

public class Problem_1 {

	 public static double arraySum(List<Integer> multiples) {
		 final int len = multiples.size();
        if (len == 0) {
        	return 0;
        }
        final double val = multiples.get(0).doubleValue();
        if (len == 1) {
        	return val;
    	}
        // help future compilers recognize tail recursion
        return val + arraySum(multiples.subList(1, len));
    }
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		// We need to store the variable to scale the algorithm
		final int size = 1000;
		double total = 0;
		// Create an array to keep the multiples of 3 and 5
		List<Integer> multiples = new ArrayList<Integer>(); //no fixed size mentioned
		// Iterate trough the size of our test
		for(int i = 0; i < size; i++) {
			// Grab the numbers that are multiples of 3 or 5
			if((i % 3 == 0) || (i % 5 == 0) ) {
				multiples.add(i);
			}
		}
		// Since ONLY Java 8 has got something to sum the array values I want
		// to keep this source compatible with previous version.
		// I will create my own function.
		total = arraySum(multiples);
	}

}
