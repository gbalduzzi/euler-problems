<?php
/**********************************
 * 
 * Problem 3 from Project Euler
 * 
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 *  
 * PLEASE NOTE
 * In order to test this script you must have PHP 5.3+ installed and php-cli, to test it with a terminal.
 *
 * REGARDING THE PERFORMANCE
 * This is not the final version, as you can see I'll trace the version of every solution, so please don't think that
 * this is the best algorithm in terms of speed and code optimization, for any trouble open an issue.
 * 
 * @author Claudio Ludovico Panetta (@ludo237)
 * @author Pietro Arturo Panetta (@arturu)
 * @version 1.1.0
 **************************************/

// Starting the benchmark
$startTime = microtime();

// Our starting point is a specific number but we can play with whatever
// number we want
$number = 600851475143; 

function primeFactors($number){
	$primeFactors = array();

	$i=2;

	do {
		if ( $number % $i == 0) {
			$number /= $i;
			$primeFactors[] = $i;
		}
		else
			++$i;

	} while ($i<=$number);

	return $primeFactors;
}

// We need an array to store the prime factors
$primeFactors = primeFactors($number);

// with PHP we can use a builtin function to find the large prime factor
// but with other language you have to code it.
max($primeFactors);

// Finish the benchmark 
$endTime = microtime();
echo "Algorithm time: ". ($endTime - $startTime);
